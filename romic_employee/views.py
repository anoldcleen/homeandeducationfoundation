from django.shortcuts import render, redirect  
from django.urls import reverse
from django.http import HttpResponse
from romic_employee.forms import EmployeeForm  ,AboutForm ,ContactForm ,DonateForm ,BlogForm ,CauseForm ,ServiceForm ,ActivityForm ,PartnerForm ,MemberForm ,LoginForm
from romic_employee.models import Employee  ,About  ,Contact ,Blog ,Donation ,Cause ,Service ,Activity ,Partner ,Member 
from django.template import Context
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from django.contrib import auth



def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'login.html')


def cause_image_view(request):
 
    if request.method == 'POST':
        form = CauseForm(request.POST, request.FILES)
 
        if form.is_valid():
            try:  
               form.save()
               return redirect('/showcause')
         
            except:  
                pass              
    else:
        form = CauseForm()
    return render(request, 'cause_image_form.html', {'form': form})

def showcause(request):  
    causes = Cause.objects.all()  
    return render(request,'showcauses.html',{'cause_images':causes}) 
 
 
def display_cause_image(request):
 
    if request.method == 'GET':
        causes = Cause.objects.all()
        return render(request, 'display_cause_images.html',{'cause_images': causes})

def editcause(request, id):  
    cause = Cause.objects.get(id=id)  
    return render(request,'editcause.html', {'cause_images':cause})  

def updatecause(request, id):  
    cause = Cause.objects.get(id=id)  
    form = CauseForm(request.POST, instance = cause)  
    if form.is_valid():  
        form.save()  
        return redirect("/showcause")  
    return render(request, 'editcause.html', {'cause_image': cause})  

def destroycause(request, id):  
    cause = Cause.objects.get(id=id)  
    cause.delete()  
    return redirect("/showcause") 







def activity_image_view(request):
 
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
 
        if form.is_valid():
            try:  
               form.save()
               return redirect('/showactivity')
         
            except:  
                pass              
    else:
        form = ActivityForm()
    return render(request, 'activity_image_form.html', {'form': form})

def showactivity(request):  
    actvitities = Activity.objects.all()  
    return render(request,'showactivity.html',{'activity_images':actvitities}) 
 
 
def display_activity_image(request):
 
    if request.method == 'GET':
        actvitities = Activity.objects.all()
        return render(request, 'display_activity_images.html',{'activity_images': actvitities})

def editactivity(request, id):  
    actvitity = Actvitity.objects.get(id=id)  
    return render(request,'editactivity.html', {'activity_image':actvitity})  

def updateacitivity(request, id):  
    actvitity = Activity.objects.get(id=id)  
    form = ActivityForm(request.POST, instance = actvitity)  
    if form.is_valid():  
        form.save()  
        return redirect("/showactivity")  
    return render(request, 'editactivity.html', {'activity_image': actvitity})  

def destroyactivity(request, id):  
    actvitity = Activity.objects.get(id=id)  
    actvitity.delete()  
    return redirect("/showactivity")  



def service_image_view(request):
 
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
 
        if form.is_valid():
            try:  
               form.save()
               return redirect('/showservice')
         
            except:  
                pass              
    else:
        form = ServiceForm()
    return render(request, 'service_image_form.html', {'form': form})


def showservice(request):  
    services = Service.objects.all()  
    return render(request,'showservice.html',{'service_images':services}) 
 
 
def display_service_image(request):
    if request.method == 'GET':
        services = Service.objects.all()
        return render(request, 'display_service_images.html',{'service_images': services})

def editservice(request, id):  
    service = Service.objects.get(id=id)  
    return render(request,'editservice.html', {'service_images':service})  

def updateservice(request, id):  
    service = Service.objects.get(id=id)  
    form = ServiceForm(request.POST, instance = service)  
    if form.is_valid():  
        form.save()  
        return redirect("/showservice")  
    return render(request, 'editservice.html', {'service_images': service})  

def destroyservice(request, id):  
    service = Service.objects.get(id=id)  
    service.delete()  
    return redirect("/showservice") 







def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def display_employee_image(request):

    if request.method == 'GET':
        employees = Employee.objects.all()
        return render(request, 'display_employee_images.html',{'employees': employees})

def show(request):  
    employees = Employee.objects.all()  
    return render(request,'show.html',{'employees':employees}) 

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  



def blog(request):
    if request.method == "POST":  
        form = BlogForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showblog')  
            except:  
                pass  
    else:  
        form = BlogForm()  
    return render(request,'blog.html',{'form':form}) 

def showblog(request):  
    blogs = Blog.objects.all()  
    return render(request,'showblog.html',{'blogs':blogs})


def displayblog(request):
 
    if request.method == 'GET':
        blogs = Blog.objects.all()
        return render(request, 'displayblog.html',{'blogs': blogs}) 


def editblog(request, id):  
    blog = Blog.objects.get(id=id)  
    return render(request,'editblog.html', {'blog':blog})  

def updateblog(request, id):  
    blog = Blog.objects.get(id=id)  
    form = BlogForm(request.POST, instance = blog)  
    if form.is_valid():  
        form.save()  
        return redirect("/showblog")  
    return render(request, 'editblog.html', {'blog': blog})  

def destroyblog(request, id):  
    blog = Blog.objects.get(id=id)  
    blog.delete()  
    return redirect("/showblog")  






def about(request):  
    if request.method == "POST":  

        form = AboutForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showabout')  
            except:  
                pass  
    else:  
        form = AboutForm()  
    return render(request,'about.html',{'form':form})  

def showabout(request):  
    abouts = About.objects.all()  
    return render(request,'showabout.html',{'abouts':abouts}) 

def editabout(request, id):  
    about = About.objects.get(id=id)  
    return render(request,'editabout.html', {'about':about})  

def updateabout(request, id):  
    about = About.objects.get(id=id)  
    form = AboutForm(request.POST, instance = about)  
    if form.is_valid():  
        form.save()  
        return redirect("/showabout")  
    return render(request, 'editabout.html', {'about': about})  

def destroyabout(request, id):  
    about = About.objects.get(id=id)  
    about.delete()  
    return redirect("/showabout")  







def contact(request):  
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/aboutrocaf')  
            except:  
                pass  
    else:  
        form = ContactForm()  
    return render(request,'contactus.html',{'form':form}) 

def showcontact(request):  
    contacts = Contact.objects.all()  
    return render(request,'showcontactus.html',{'contacts':contacts}) 


def editcontact(request, id):  
    contact = Contact.objects.get(id=id)  
    return render(request,'editcontactus.html', {'contact':contact})  

def updatecontact(request, id):  
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/showcontact")  
    return render(request, 'editcontact.html', {'contact': contact})  

def destroycontact(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/dashboard")  




def member(request):  
    if request.method == "POST":  
        form = MemberForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showmember')  
            except:  
                pass  
    else:  
        form = MemberForm()  
    return render(request,'member.html',{'form':form}) 

def showmember(request):  
    members = Member.objects.all()  
    return render(request,'showmember.html',{'members':members}) 


def editmember(request, id):  
    member = Member.objects.get(id=id)  
    return render(request,'editmember.html', {'member':member})  

def updatemember(request, id):  
    member = Member.objects.get(id=id)  
    form = MemberForm(request.POST, instance = member)  
    if form.is_valid():  
        form.save()  
        return redirect("/showmember")  
    return render(request, 'editmember.html', {'member': member})  

def destroymember(request, id):  
    member = Member.objects.get(id=id)  
    member.delete()  
    return redirect("/showmember") 





def donate(request):  
    if request.method == "POST":  
        form = DonateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showdonate')  
            except:  
                pass  
    else:  
        form = DonateForm()  
    return render(request,'donation.html',{'form':form}) 

def showdonate(request):  
    donations = Donation.objects.all()  
    return render(request,'showdonations.html',{'donations':donations}) 

def editdonate(request, id):  
    donation = donation.objects.get(id=id)  
    return render(request,'editdonate.html', {'donation':donation})  

def updatedonate(request, id):  
    donation = Donate.objects.get(id=id)  
    form = DonateForm(request.POST, instance = donation )  
    if form.is_valid():  
        form.save()  
        return redirect("/showdonate")  
    return render(request, 'editdonate.html', {'donation': donation})  

def destroydonate(request, id):  
    donation = Donation.objects.get(id=id)  
    donation.delete()  
    return redirect("/showdonate")  








def partner_image_view(request):
 
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
 
        if form.is_valid():
            try:  
               form.save()
               return redirect('/showpartner')
         
            except:  
                pass              
    else:
        form = PartnerForm()
    return render(request, 'partner_image_form.html', {'form': form})

def showpartner(request):  
    partners = Partner.objects.all()  
    return render(request,'showpartner.html',{'partner_images':partners}) 

 
def display_partner_image(request):
 
    if request.method == 'GET':
        partners = Partner.objects.all()
        return render(request, 'display_partner_images.html',{'partner_images': partners})

def editpartner(request, id):  
    partner = Partner.objects.get(id=id)  
    return render(request,'editpartner.html', {'partner_images':partner})  

def updatepartner(request, id):  
    partner = Partner.objects.get(id=id)  
    form = PartnerForm(request.POST, instance = partner)  
    if form.is_valid():  
        form.save()  
        return redirect("/showpartner")  
    return render(request, 'editpartner.html', {'partner_image': partner})  

def destroypartner(request, id):  
    partner = Partner.objects.get(id=id)  
    partner.delete()  
    return redirect("/showpartner") 


def showuserabout(request):  
    abouts = About.objects.all() 
    return render(request, "userabout.html",{'abouts':abouts})




def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)








