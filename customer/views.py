from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from customer.models import UserLogin, user_register,UserLogin
from customer.models import Createaccount
from customer.models import Createaccountuser
from customer.models import create_nominee
from customer.models import create_reference
from customer.models import create_documents
from customer.models import PaymentDetailsTable
from customer.models import accountpayTable
from customer.models import payeedetailsTable







def createaccount(request):
    return render(request,'customer/createaccount/createaccount.html')

def documentupload(request):
    return render(request,'customer/documentupload/documentupload.html')

def landingpage(request):
    return render(request,"customer/landingpage/landingpage.html")

def nominee(request):
    return render(request,'customer/nominee/nominee.html')

def references(request):
    return render(request,'customer/references/references.html')

def user(request):
    return render(request,'customer/user/user.html')

def loginform(request):
    return render(request,'customer/loginform/loginform.html')

def customerdash(request):
    return render(request,'customer/bankadm.html')

def payment(request):
    return render(request,'customer/payment.html')

def payment(request):
    return render(request,'customer/payment.html')

def paymentconfirm(request):
    return render(request,'customer/paymentconfirm.html')

def createaccountuser(request):
    return render(request,'customer/createaccountuser.html')



class login_check(APIView):  
     def post(self, request):
         username = request.POST['username']
         password = request.POST['pass']
         if username == 'test':
            return JsonResponse({"status":"pass"})
         else:
             return JsonResponse({"status":"fail"})
         

def signupform(request):
    return render(request,'customer/signupform/signupform.html')

class login_check(APIView):
    def post(self, request):
        username = request.POST['user']
        password = request.POST['password']
        if username == 'test':
            return JsonResponse({"status": "pass"})
        else:
            return JsonResponse({"status": "fail"})


class create_user(APIView):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        utype = request.POST['utype']

        usr = user_register()

        usr.user_name = username
        usr.email = email
        usr.password = password
        usr.role = utype 
        usr.save()
        
        return JsonResponse({"status": "pass"})
    
    

class update_account_details(APIView):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        mob = request.POST['mobile']
        utype = request.POST['utype']
        message = request.POST['message']
        Createaccount.objects.filter(mobile_no = mob).update(user_name=username, email=email,utype=utype, message=message ) 
        return JsonResponse({"status": "pass"})



from django.views.generic.base import TemplateView

class view_user(TemplateView):
    template_name = "view_user.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = user_register.objects.all()
        context['user_data'] = user_data
        context["currentuser"] = self.request.session.get("user_data")
        return context

#FOR ADMIN  
class create_account(APIView):
    def post(self,request):

        user_name = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        utype = request .POST['utype']
        message = request .POST['message']
        balance = request .POST['balance']

        acc = Createaccount()

        acc.user_name = user_name
        acc.mobile_no = mobile
        acc.email = email
        acc.utype = utype
        acc.message = message
        acc.balance = balance

        acc.save()

        return JsonResponse({"status" : "pass"})
    
class view_account(TemplateView):
    template_name = "view_account.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = Createaccount.objects.all()
            context = {'userdata':user_data}
            return context
    
#FOR USER
class create_account_user(APIView):
    def post(self,request):

        user_name = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        utype = request .POST['utype']
        message = request .POST['message']
        

        acc = Createaccountuser()

        acc.user_name = user_name
        acc.mobile_no = mobile
        acc.email = email
        acc.utype = utype
        acc.message = message
        

        acc.save()

        return JsonResponse({"status" : "pass"})
    
class view_account_user(TemplateView):
    template_name = "view_account_user.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = Createaccountuser.objects.all()
            context = {'userdata':user_data}
            return context
    

        
class deleteuser(APIView):
     def post(self,request):
        name = request.POST['username']
        UserLogin.objects.filter(username=name).delete()
        return JsonResponse({"status":"pass"})
     

class removeuser(APIView):
     def post(self,request):
        name = request.POST['username']
        user_register.objects.filter(user_name=name).delete()
        return JsonResponse({"status":"pass"})
     
class deleteaccount(APIView):
     def post(self,request):
        name = request.POST['username']
        Createaccount.objects.filter(user_name=name).delete()
        return JsonResponse({"status":"pass"})
     
class deletedocuments(APIView):
     def post(self,request):
        name = request.POST['username']
        create_documents.objects.filter(photo=name).delete()
        return JsonResponse({"status":"pass"})
     
class deletenominee(APIView):
     def post(self,request):
        name = request.POST['username']
        create_nominee.objects.filter(name=name).delete()
        return JsonResponse({"status":"pass"})
     
class deletereference1(APIView):
     def post(self,request):
        name = request.POST['name']
        create_reference.objects.filter(name=name).delete()
        return JsonResponse({"status":"pass"})

     

class create_nominee_details(APIView):
    def post(self,request):
        name = request.POST['username']
        date = request.POST['date']
        mobile = request.POST['mobile']
        relationship = request.POST['relationship']
        address = request.POST['address']

        nom = create_nominee()

        nom.name = name
        nom.mobile_no = mobile
        nom.relationship = relationship
        nom.date = date
        nom.address = address
        nom.save()
        return JsonResponse({"status":"pass"})

class view_nominee(TemplateView):
    template_name = "view_nominee.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = create_nominee.objects.all()
            context = {'userdata':user_data}
            return context
    
class CreateReference(APIView):
    def post(self,request):
        name = request.POST['username']
        addresss = request.POST['address']
        mobile = request.POST['mobile']
        message = request .POST['message']
        ref1 = create_reference()
        ref1.name = name
        ref1.mobile_no = mobile
        ref1.address1 = addresss
        ref1.message = message
        ref1.save()
        
        return JsonResponse({"status":"pass"})
    
class view_reference(TemplateView):
    template_name = "view_reference.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = create_reference.objects.all()
            context = {'userdata':user_data}
            return context
    
class create_user_documents(APIView):
    def post(self,request):
        photo = request.POST['photo']
        aadhar_card = request.POST['aadhar']
        pan_card = request.POST['pan']
        doc = create_documents()
        doc.photo = photo
        doc.aadhar_card = aadhar_card
        doc.pan_card = pan_card
        doc.save()
        return JsonResponse({"status":"pass"})
    
class view_documents(TemplateView):
    template_name = "view_documents.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = create_documents.objects.all()
            context = {'userdata':user_data}
            return context
    
class user_login_view(APIView):
    def post(self,request):
        username = request.POST['username']
        password= request.POST['pass']
        log = UserLogin()
        log.username = username
        log.password = password
        log.save()
        return JsonResponse({"status":"pass"})
    
class view_login(TemplateView):
    template_name = "view_login.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = UserLogin.objects.all()
            context = {'userdata':user_data}
            return context  

# class view_accountadmin(TemplateView):
#     template_name = "viewaccountadmin.html"

#     def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             user_data = Createaccount.objects.all()
#             context = {'userdata':user_data}
#             return context

class logincheck(APIView):
    def post(self, request):
        user_name = request.POST['username']
        password = request.POST['pass']
        #acc_name = request.POST['user_name']
        ent = user_register.objects.filter(user_name=user_name,password=password).values()
        # ubalance = Createaccount.objects.filter(user_name=acc_name ).values()
        if(len(ent) > 0):
            request.session["userdata"] = ent[0]["user_name"]
            # request.session["userbalance"]=ubalance[0]["user_name"]
            return JsonResponse({"status":"pass", "user_name": ent[0]["user_name"], "role": ent[0]["role"], "pass": ent[0]["password"],"email": ent[0]["email"]})
        else:
            return JsonResponse({"status":"fail"})
        
class UserProfileView(TemplateView):
    model = user_register
    template_name = "profile.html" 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        user = user_register.objects.get(user_name=username)
        balance = Createaccount.objects(user_name=username)
        print(balance)
        context['currentuser'] = user.user_name
        context['email'] = user.email
        context['password'] = user.password
        # context['balance']=balance.balance

        
        return context
    
class UserDashboardView(TemplateView):
    model = user_register()
    print("im here ****")
    template_name = "bankadm.html" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        #ubalance = self.request.session.get("userbalance")
        user = user_register.objects.get(user_name=username)
        #balance = Createaccount.objects.get(user_name=ubalance)
        context['currentuser'] = user.user_name
        # context['balance']=balance.balance       
        return context
    
class AdminDashboardView(TemplateView):
    model = user_register
    template_name = "index.html" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("userdata")
        #ubalance = self.request.session.get("userbalance")
        user = user_register.objects.get(user_name=username)
        #balance = Createaccount.objects.get(user_name=ubalance)
        context['currentuser'] = user.user_name
        # context['balance']=balance.balance       
        return context
        
class accountpaydetails(APIView):
    def post(self, request):
        accountName = request.POST['cardholdername']
        accountNumber=request.POST['cardnumber']
        ifsc=request.POST['ifsc']
        amount = request.POST['amount']

        crs = accountpayTable()

        crs.account_Name=accountName
        crs.account_Number=accountNumber
        crs.ifsc=ifsc
        crs.amount=amount

        crs.save()

        return JsonResponse({"status":"pass"})
    
class accountpayview(TemplateView):
    template_name =  'accountpay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = accountpayTable.objects.all()
        context = {"user_data": user_data}
        return context
    
class payment_detailsview(TemplateView):
    template_name =  'payment_detailsview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = accountpayTable.objects.all()
        context = {"user_data": user_data}
        return context
    
class UserPaymentView(TemplateView):
    model = accountpayTable
    template_name = "paymentconfirm.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accountname = self.request.session.get("accountdata")
        user = accountpayTable.objects.get(account_Name=accountname)
        context['amount'] = user.amount

        return context
    
class payeedetails(APIView):
    def post(self, request):
        accountName = request.POST['cardholdername']
        accountNumber=request.POST['cardnumber']
        ifsc=request.POST['ifsc']
        bankname = request.POST['bankname']

        crs = payeedetailsTable()

        crs.account_Name=accountName
        crs.account_Number=accountNumber
        crs.ifsc=ifsc
        crs.bankname=bankname
        crs.save()
        
        return JsonResponse({"status":"pass"})
        
class payeecheck(APIView):
    def post(self, request):
        accountName = request.POST['cardholdername']
        ent = payeedetailsTable.objects.filter(account_Name=accountName).values()
        if(len(ent) > 0):
            request.session["accountdata"] = ent[0]["account_Name"]
            return JsonResponse({"status":"pass", "account_Name": ent[0]["account_Name"]})
        else:
            return JsonResponse({"status":"fail"})
    
class payeedetailsview(TemplateView):
    template_name =  'payeeform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = payeedetailsTable.objects.all()
        context = {"user_data": user_data}
        return context
    
class payeetableview(TemplateView):
    template_name =  'payeedetailsview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = payeedetailsTable.objects.all()
        context = {"user_data": user_data}
        return context


    


