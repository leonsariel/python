from urllib import request

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm, UserInfoForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
from clientForm.models import ClientInfo
from django.core.urlresolvers import reverse
import json, names, random
from users.globalVar import alist


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LogoutView(View):
    def get(self, request):
        logout(request)
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse("login"))


class IndexView(View):
    def get(self, request):
        # clients = ClientInfo.objects.filter(caseWorker_id=request.user.id)
        currentUser = UserProfile.objects.get(id=request.user.id)
        # getTree(currentUser)
        mlist, slist, clist, clientList = getPostList(currentUser)
        regionList, totalList, lowList, avgList, highList = regionCountList(currentUser)
        print("this is region list: ", regionList)

        # sum of low average and high for knob
        sum_list = [sum(lowList), sum(avgList), sum(highList)]
        percent_list = []
        # if currentUser.role != "Case Worker":
        for i in sum_list:
            try:
                p = round(i / sum(totalList) * 100, 1)
                percent_list.append(p)
            except ZeroDivisionError:
                percent_list = [50, 20, 30]
                sum_list = [1, 2, 3]

        postCodeList = []
        if currentUser.role == "Manager":
            return render(request, "index.html",
                          {'sList': json.dumps(slist), 'cList': json.dumps(clist), 'region': json.dumps(regionList),
                           'clientList': json.dumps(clientList),
                           'totalList': json.dumps(totalList), 'lowList': json.dumps(lowList),
                           'avgList': json.dumps(avgList), 'highList': json.dumps(highList),
                           'sumList': json.dumps(sum_list), 'perList': percent_list})

        if currentUser.role == "Supervisor":
            return render(request, "index.html",
                          {'sList': json.dumps(slist), 'cList': json.dumps(clist), 'region': json.dumps(regionList),
                           'clientList': json.dumps(clientList),
                           'totalList': json.dumps(totalList), 'lowList': json.dumps(lowList),
                           'avgList': json.dumps(avgList), 'highList': json.dumps(highList),
                           'sumList': json.dumps(sum_list), 'perList': percent_list})

        if currentUser.role == "Case Worker":
            percent_list = [50, 20, 30]
            sum_list = [1, 2, 3]
            # return render(request, "index.html",
            #               {'region': json.dumps(regionList), 'postList': json.dumps(postCodeList),
            #                'totalList': json.dumps(totalList), 'lowList': json.dumps(lowList),
            #                'avgList': json.dumps(avgList), 'highList': json.dumps(highList),
            #                'sumList': json.dumps(sum_list), 'perList': percent_list})
            return render(request, "base.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # client = ClientInfo.objects.filter(clientID="147147")
                    if user.isRegister:
                        return HttpResponseRedirect(reverse("index"))
                    else:
                        return HttpResponseRedirect(reverse("userInfo"))
                        # return render(request, "index.html",{"clients":client})
                else:
                    return render(request, "login.html", {"msg": "user is not activated! Please check your email"})
            else:
                return render(request, "login.html", {"msg": "username and password are not matched!"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html",
                              {"register_form": register_form, "msg": "User is already exist,please try another Email"})

            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name

            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            print("test modify")
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email,
                                                               "msg": "Your Password is not matched!Please ensure you enter the same password!"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


class UserInfoView(View):
    def get(self, request):
        users = UserProfile.objects.all().exclude(role="Case Worker")
        currentUser = UserProfile.objects.get(id=request.user.id)
        if currentUser.isRegister:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "userInfo.html", {"users": users})

    def post(self, request):
        userInfoForm = UserInfoForm(request.POST)

        if userInfoForm.is_valid():
            user = UserProfile.objects.get(id=request.user.id)
            lastName = request.POST.get("userLastName", "")
            firstName = request.POST.get("userFirstName", "")
            postCode = request.POST.get("userPostCode", "")
            postCode = postCode.replace(" ", "")
            program = request.POST.get("program", "")
            site = request.POST.get("site", "")
            region = request.POST.get("region", "")
            role = request.POST.get("role", "")
            reportTo = request.POST.get("reportTo", "")

            user.lastName = lastName
            user.firstName = firstName
            user.postCode = postCode
            user.region = region
            user.site = site
            user.role = role
            user.program = program
            user.isRegister = True
            user.reportTo = reportTo

            user.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("index"))


class SelectUserView(View):
    def get(self, request):
        currentUser = UserProfile.objects.get(id=request.user.id)

        role = currentUser.role
        if role == "Regional Director":
            user3 = UserProfile.objects.all().filter(role="Manager")
            user2 = UserProfile.objects.all().filter(role="Supervisor")
            user1 = UserProfile.objects.all().filter(role="Case Worker")
            c = {}
            b = {}
            for u in user3:
                user2 = findChild(u.id)
                c[u] = [user for user in user2]
            print(c)
            for n in user2:
                user1 = findChild(n.id)
                b[n] = [un for un in user1]
            dic = formatDic(c, b)
            print(dic)
            return render(request, "selectUser.html",
                          {"dic": dic, "user3": user3, "user1": user1, "director": "director"})


        elif role == "Manager":
            sPostList = []
            cPostList = []
            user2 = UserProfile.objects.all().filter(role="Supervisor")
            user1 = UserProfile.objects.all().filter(role="Case Worker")
            c = {}
            b = {}
            for n in user2:
                user1 = findChild(n.id)
                b[n] = [un for un in user1]
            print("this is b", b)
            for i, j in alist.items():
                sPostList.append(i.postCode)
                for k in j:
                    cPostList.append(k.postCode)

            return render(request, "selectUser.html", {"dic": b})
        elif role == "Supervisor":
            user1 = findChild(currentUser.id)

            return render(request, "selectUser.html", {"user1": user1})
        else:

            return render(request, "select.html", {})

    def post(self, request):
        uid = request.POST.get("uid", "")
        clients = ClientInfo.objects.filter(caseWorker_id=uid)
        return render(request, "select.html", {
            "clients": clients
        })


def getPostList(user):
    mPostList = []
    sPostList = []
    cPostList = []
    caseIDList = []
    clientPostList = []
    if user.role == "Manager":

        for i, j in alist.items():
            sPostList.append(i.postCode)
            for k in j:
                cPostList.append(k.postCode)
                caseIDList.append(k.id)
        clients = ClientInfo.objects.filter(caseWorker__in=caseIDList)
        for i in clients:
            clientPostList.append(i.postCode)
    if user.role == "Supervisor":
        allchild = findChild(user.id)
        for all in allchild:
            cPostList.append(all.postCode)
            caseIDList.append(all.id)
        clients = ClientInfo.objects.filter(caseWorker__in=caseIDList)
        for i in clients:
            clientPostList.append(i.postCode)
    return mPostList, sPostList, cPostList, clientPostList


def createTestUser():
    fName = names.get_first_name()
    lName = names.get_last_name()
    postCode = ['T4N0A6', 'T4N0C8', 't4n0k5', 't5a0k3', 't5a0b6', 't6J2k7', 't1y1p4', 't1y1l8', 't2v5B7']
    region = "North"
    site = "North 92"
    report = [8, 11]
    reportTo = random.choice(report)
    p = random.choice(postCode)
    user = UserProfile()

    user.site = site
    user.region = region

    user.firstName = fName
    user.lastName = lName
    user.username = fName + lName + "@gmail.com"
    user.isRegister = 1
    user.postCode = p
    user.role = 'Case Worker'
    user.program = "OPG"
    user.email = fName + lName + "@gmail.com"
    user.reportTo = reportTo
    user.password = "123123"
    user.save()

    num = random.randint(1, 20)
    per = [20, 40, 60, 80, 100]
    for i in range(num):
        client = ClientInfo()
        cfName = names.get_first_name()
        clName = names.get_last_name()
        post = random.choice(postCode)
        knob = random.choice(per)
        knob2 = random.choice(per)
        knob3 = random.choice(per)
        knob4 = random.choice(per)
        total = knob * 0.15 + knob2 * 0.35 + knob3 * 0.20 + knob4 * 0.30
        if (total < 40):
            rating = "low";
        elif (total >= 40 and total < 80):
            rating = "avg";
        elif (total >= 80):
            rating = "high";
        client.knob = knob
        client.knob2 = knob2
        client.knob3 = knob3
        client.knob4 = knob4
        client.rating = rating
        client.firstName = cfName
        client.postCode = post
        client.lastName = clName
        client.caseWorker_id = user.id
        client.status = "open"
        client.region = user.region
        client.site = user.site
        client.save()
    user.save()


#
# createTestUser()

# count report for bar chart
def regionCountList(role):
    total_list = []
    low_list = []
    avgList = []
    highList = []
    if role.role == "Regional Director":
        site = ["Calgary 251", "Edmonton 300", "Edmonton 111", "North 92", "South 120"]
        for x in site:
            if role.region not in x:
                site.remove(x)

        for r in site:
            if role.region not in r:
                site.remove(r)
            else:
                clients = ClientInfo.objects.filter(site=r)
                total_list.append(clients.count())
                low_list.append(clients.filter(rating="low").count())
                avgList.append(clients.filter(rating="avg").count())
                highList.append(clients.filter(rating="high").count())
        return site, total_list, low_list, avgList, highList

    elif role.role == "Manager":
        supervisors = UserProfile.objects.filter(reportTo=role.id)
        name_list = []
        total_list = []
        low_list = []
        avgList = []
        highList = []
        for s in supervisors:
            sName = s.firstName + " " + s.lastName
            name_list.append(sName)
            case_worker = ""
            total, low, avg, high = 0, 0, 0, 0
            case_worker = UserProfile.objects.filter(reportTo=s.id)
            for c in case_worker:
                total = total + ClientInfo.objects.filter(caseWorker=c.id).count()
                low = low + ClientInfo.objects.filter(rating="low").filter(caseWorker=c.id).count()
                avg = avg + ClientInfo.objects.filter(rating="avg").filter(caseWorker=c.id).count()
                high = high + ClientInfo.objects.filter(rating="high").filter(caseWorker=c.id).count()
            low_list.append(low)
            avgList.append(avg)
            highList.append(high)
            total_list.append(total)
        print("this is name list: ", name_list)
        return name_list, total_list, low_list, avgList, highList
    elif role.role == "Supervisor":
        name_list = []
        total_list = []
        low_list = []
        avgList = []
        highList = []
        caseWorkers = UserProfile.objects.filter(reportTo=role.id)
        for c in caseWorkers:
            name = c.firstName + " " + c.lastName
            name_list.append(name)
            total = ClientInfo.objects.filter(caseWorker=c.id).count()
            low = ClientInfo.objects.filter(caseWorker=c.id).filter(rating="low").count()
            avg = ClientInfo.objects.filter(caseWorker=c.id).filter(rating="avg").count()
            high = ClientInfo.objects.filter(caseWorker=c.id).filter(rating="high").count()
            total_list.append(total)
            low_list.append(low)
            avgList.append(avg)
            highList.append(high)
        return name_list, total_list, low_list, avgList, highList
    elif role.role == "Case Worker":
        name_list = []
        total_list = []
        low_list = []
        avgList = []
        highList = []

        total = ClientInfo.objects.filter(caseWorker=role.id).count()
        low = ClientInfo.objects.filter(caseWorker=role.id).filter(rating="low").count()
        avg = ClientInfo.objects.filter(caseWorker=role.id).filter(rating="avg").count()
        high = ClientInfo.objects.filter(caseWorker=role.id).filter(rating="high").count()
        total_list.append(total)
        low_list.append(low)
        avgList.append(avg)
        highList.append(high)
        return name_list, total_list, low_list, avgList, highList


def getTree(currentUser):
    # currentUser = UserProfile.objects.get(id=request.user.id)
    role = currentUser.role
    if role == "Regional Director":
        user3 = UserProfile.objects.all().filter(role="Manager")
        user2 = UserProfile.objects.all().filter(role="Supervisor")
        user1 = UserProfile.objects.all().filter(role="Case Worker")
        a = {}
        b = {}
        for u in user3:
            user2 = findChild(u.id)
            a[u] = [user for user in user2]
        print("this is ", a)
        for n in user2:
            user1 = findChild(n.id)
            b[n] = [un for un in user1]

        dic = formatDic(a, b)
        print("dictionary ", dic)
        return {"dic": dic, "user3": user3, "user1": user1, "director": "director", "currentUser": currentUser}
    elif role == "Manager":
        user2 = UserProfile.objects.all().filter(role="Supervisor").filter(reportTo=currentUser.id)
        for u in user2:
            user1 = findChild(u.id)
            alist[u] = [user for user in user1]
        print("alist ", alist)
        # user1 = UserProfile.objects.filter(role="1").filter(reportTo__in=user2)
        return {"user2": user2, "sList": alist, "manager": "manager", "currentUser": currentUser}
    elif role == "Supervisor":
        allChild = findChild(request.user.id)
        return {"allChild": allChild, "supervisor": "supervisor"}
    return currentUser


def findChild(id):
    allChild = UserProfile.objects.all().filter(reportTo=id)
    return allChild


def formatDic(a, b):
    for key in a:
        for n in b:
            for k, v in b.items():
                if (k in a[key]):
                    l = (a[key].index(k))
                    a[key][l] = {k: v}

            break
    return a
