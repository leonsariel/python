# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '11/15/2017 2:17 PM'

from users.models import UserProfile

global alist
alist = {}


def setting(request):
    try:
        currentUser = UserProfile.objects.get(id=request.user.id)

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

            print("this is b ", b)

            dic = formatDic(a, b)
            print("dictionary ", dic)
            return {"dic": dic, "user3": user3, "user1": user1, "director": "director", "currentUser": currentUser}


        elif role == "Manager":

            user2 = UserProfile.objects.all().filter(role="Supervisor").filter(reportTo=request.user.id)
            for u in user2:
                user1 = findChild(u.id)
                alist[u] = [user for user in user1]
            print("org ", alist)
            # user1 = UserProfile.objects.filter(role="1").filter(reportTo__in=user2)
            return {"user2": user2, "sList": alist, "manager": "manager", "currentUser": currentUser}
        elif role == "Supervisor":

            allChild = findChild(request.user.id)

            return {"allChild": allChild, "supervisor": "supervisor"}
    except (TypeError, UserProfile.DoesNotExist):
        if request.user:
            current_user = request.user
            currentUser = {"currentUser": current_user}
            return currentUser
        else:
            pass

    return currentUser


def findChild(id):
    allChild = UserProfile.objects.all().filter(reportTo=id)
    return allChild

# change the format to [a:x]
def formatDic(a, b):
    for key in a:
        for n in b:
            for k, v in b.items():
                if (k in a[key]):
                    l = (a[key].index(k))
                    a[key][l] = {k: v}
                    print({k: v})
                    print("\n")

            break
    return a
