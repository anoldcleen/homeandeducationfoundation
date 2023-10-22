from django import forms  
from romic_employee.models import Employee  ,About ,Contact ,Blog ,Cause  ,Service ,Activity ,Donation ,Partner ,Member 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class MemberForm(forms.ModelForm):
 
    class Meta:
        model = Member
        fields = "__all__" 


class ActivityForm(forms.ModelForm):
 
    class Meta:
        model = Activity
        fields = "__all__" 

 
class CauseForm(forms.ModelForm):
 
    class Meta:
        model = Cause
        fields = "__all__" 

 
class ServiceForm(forms.ModelForm):
 
    class Meta:
        model = Service
        fields = "__all__" 


class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

    
class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Blog  
        fields = "__all__"  


class CauseForm(forms.ModelForm):  
    class Meta:  
        model = Cause  
        fields = "__all__"  


class AboutForm(forms.ModelForm):  
    class Meta:  
        model = About  
        fields = "__all__" 
        


class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = "__all__" 


class DonateForm(forms.ModelForm):  
    class Meta:  
        model = Donation  
        fields = "__all__" 


class PartnerForm(forms.ModelForm):  
    class Meta:  
        model = Partner  
        fields = "__all__" 



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']