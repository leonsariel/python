from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from formtools.wizard.views import WizardView, SessionWizardView
from .forms import ClientForm1, ClientForm2
from .models import UserProfile, ClientInfo, CaseIntensityRating


import logging
logr = logging.getLogger(__name__)

# Create your views here.


class ClientFormView(SessionWizardView):
    template_name = "new-cir.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return render_to_response('new-cir.html',{})


def process_form_data(form_list):
    pass


class ClientInfoView(View):
    def get(self,request):
        clientFormOne = ClientForm1()
        clientFormTwo = ClientForm2()
        clients = ClientInfo.objects.filter(caseWorker_id=request.user.id)
        low = clients.filter(rating="low").count()
        avg = clients.filter(rating="avg").count()
        high = clients.filter(rating="high").count()
        return render(request, "new-cir.html",{'clientFormOne':clientFormOne, 'clientFormTwo':clientFormTwo,
                                               'clients':clients, 'low':low, 'avg':avg, 'high':high,})

    def post(self,request):
        form1 = ClientForm1(request.POST)
        form2 = ClientForm2(request.POST)
        if form1.is_valid and form2.is_valid():
            clientID = request.POST.get("clientID", "")
            if ClientInfo.objects.filter(clientID=clientID):
                return render(request, "register.html", {"register_form":form1, "msg":"User is already exist,please try another Email"})

            # pass_word = request.POST.get("password", "")
            client = ClientInfo()
            cir = CaseIntensityRating()


            #get post data
            clientID = request.POST.get("clientID", "")
            firstName = request.POST.get("firstName", "")
            lastName = request.POST.get("lastName", "")
            postCode = request.POST.get("postCode", "")
            status = request.POST.get("status", "")
            knob = request.POST.get("knob", "")
            knob2 = request.POST.get("knob2", "")
            knob3 = request.POST.get("knob3", "")
            knob4 = request.POST.get("knob4", "")


            k1 = knob.strip(' %')
            k2 = knob2.strip(' %')
            k3 = knob3.strip(' %')
            k4 = knob4.strip(' %')
            totle = float(k1)* 0.15 + float(k2) * 0.35 + float(k3) * 0.20 + float(k4) * 0.30;
            if totle < 20:
                rating = "low"
            elif 20<=totle and totle < 80:
                rating = "avg"
            elif totle>=80:
                rating = "high"

            #save to DB
            currentID = request.user.id
            currentUser = UserProfile.objects.get(id=currentID)
            client.site = currentUser.site
            client.region = currentUser.region
            client.clientID = clientID
            client.firstName = firstName
            client.lastName = lastName
            client.postCode = postCode
            client.status = status
            client.caseWorker_id = request.user.id
            client.knob = knob
            client.knob2 = knob2
            client.knob3 = knob3
            client.knob4 = knob4
            client.rating = rating


            cir.clientID = clientID
            cir.knob = knob
            cir.knob2 = knob2
            cir.knob3 = knob3
            cir.knob4 = knob4
            cir.rating = rating
            client.save()
            cir.save()

            return render(request, "index.html")
        else:
            return render(request, "new-cir.html", {})



# edit client info
class EditClientView(View):
    def get(self,request):
        return render(request, "edit-cir.html")

    def post(self,request):
        form1 = ClientForm1(request.POST)
        form2 = ClientForm2(request.POST)
        cid = request.session.get('clientIDSession')
        print("this is " + cid)


        if form1.is_valid and form2.is_valid():
            clientID = request.POST.get("clientID", "")
            if ClientInfo.objects.filter(clientID=clientID):
                client = ClientInfo.objects.get(clientID=cid)
                cir = CaseIntensityRating.objects.get(clientID=cid)

                currentID = request.user.id
                currentUser = UserProfile.objects.get(id = currentID)
                # get post data
                firstName = request.POST.get("firstName", "")
                lastName = request.POST.get("lastName", "")
                postCode = request.POST.get("postCode", "")
                status = request.POST.get("status", "")
                knob = request.POST.get("knob", "")
                knob2 = request.POST.get("knob2", "")
                knob3 = request.POST.get("knob3", "")
                knob4 = request.POST.get("knob4", "")

                # save to DB
                currentID = request.user.id
                currentUser = UserProfile.objects.get(id=currentID)
                client.site = currentUser.site
                client.region = currentUser.region
                client.firstName = firstName
                client.lastName = lastName
                client.postCode = postCode
                client.status = status
                client.caseWorker_id = request.user.id

                cir.knob = knob
                cir.knob2 = knob2
                cir.knob3 = knob3
                cir.knob4 = knob4
                client.save()
                cir.save()
                return render(request, "index.html",{})

            else:
                ClientInfo.objects.get(clientID=cid).delete()
                CaseIntensityRating.objects.get(clientID=cid).delete()
                client = ClientInfo()
                cir = CaseIntensityRating()
                #get post data
                clientID = request.POST.get("clientID", "")
                firstName = request.POST.get("firstName", "")
                lastName = request.POST.get("lastName", "")
                postCode = request.POST.get("postCode", "")
                status = request.POST.get("status", "")
                knob = request.POST.get("knob", "")
                knob2 = request.POST.get("knob2", "")
                knob3 = request.POST.get("knob3", "")
                knob4 = request.POST.get("knob4", "")



                #save to DB
                client.clientID = clientID
                client.firstName = firstName
                client.lastName = lastName
                client.postCode = postCode
                client.status = status
                client.caseWorker_id = request.user.id
                cir.clientID = clientID
                cir.knob = knob
                cir.knob2 = knob2
                cir.knob3 = knob3
                cir.knob4 = knob4
                client.save()
                cir.save()

            return render(request, "select.html")
        else:
            return render(request, "edit-cir.html", {})







# select client and fetch info
class SelectClientView(View):
    def get(self, request):
        clients = ClientInfo.objects.filter(caseWorker_id=request.user.id)
        return render(request, "select.html", {
            "clients": clients
        })

    def post(self, request):
        cid = request.POST.get("cid", "")
        client = ClientInfo.objects.get(clientID=cid)
        cir = CaseIntensityRating.objects.get(clientID=cid)
        # pass session
        request.session['clientIDSession'] = cid
        return render(request, "edit-cir.html",{
            "client": client,
            "cir": cir
        })

