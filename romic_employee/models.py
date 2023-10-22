from django.db import models
from django.contrib.auth.models import User



class Cause(models.Model):
    causetitle = models.CharField(max_length=50,default = '')
    causedescription = models.TextField(default = '')
    cause_main_img1 = models.ImageField(upload_to='images/',default = '')
    cause_main_img2 = models.ImageField(upload_to='images/',default = '')
    cause_main_img3 = models.ImageField(upload_to='images/',default = '')
    cause_main_img4 = models.ImageField(upload_to='images/',default = '')
    cause_main_img5 = models.ImageField(upload_to='images/',default = '')
    cause_main_img6 = models.ImageField(upload_to='images/',default = '')
    class Meta:  
        db_table = "cause" 


class Service(models.Model):
    servicecategory = models.CharField(max_length=50,default = '', blank=True )
    servicetitle = models.CharField(max_length=50,default = '', blank=True )
    servicedescription1 = models.TextField(default = '',blank=True )
    servicedescription2 = models.TextField(default = '',blank=True )
    servicedescription3 = models.TextField(default = '',blank=True )
    service_main_img = models.ImageField(upload_to='images/', blank=True )
  
    
    class Meta:  
        db_table = "service" 



class Employee(models.Model):    
    ename = models.CharField(max_length=100,default = '')  
    eemail = models.EmailField(default = '')  
    econtact = models.CharField(max_length=15,default = '')
    edescription = models.TextField(default = '')

    class Meta:  
        db_table = "employee" 


class Contact(models.Model):  
    commentname = models.CharField(max_length=100, default = '') 
    commentemail = models.EmailField(default = '') 
    commentsubject = models.TextField(default = '')  
    commentmessage = models.TextField(default = '') 
    class Meta:  
        db_table = "contact" 


class Respond(models.Model):  
    respondmessage = models.TextField(default = '') 
    class Meta:  
        db_table = "response" 


class Donation(models.Model):  
    dname = models.CharField(max_length=100 ,default = '') 
    damount = models.CharField(max_length=100 ,default = '') 
    dtype = models.CharField(max_length=15 ,default = '')
    dcause = models.CharField(max_length=15 ,default = '')  
           
    class Meta:  
        db_table = "donation" 


class Blog(models.Model):  
    btitle = models.CharField(max_length=100,default = '')  
    bauthor = models.CharField(max_length = 100, default='') 
    bdescription = models.TextField(default = '') 
    byoutubelink = models.TextField(default = '') 
       
    class Meta:  
        db_table = "blog" 

        

class About(models.Model):  
    projectname = models.CharField(max_length=100 ,default = '',blank=True) 
    mission = models.TextField(default = '',blank=True)
    vision = models.TextField(default = '',blank=True)
    objective1 = models.TextField(default = '',blank=True)
    objective2 = models.TextField(default = '',blank=True) 
    objective3 = models.TextField(default = '',blank=True) 
    objective4 = models.TextField(default = '',blank=True) 
    objective5 = models.TextField(default = '',blank=True)
    testimonial1 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialrole1 = models.CharField(max_length=100,default = '',blank=True  ) 
    testimonialdecription1 = models.TextField(default = '',blank=True)
    testimonial2 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialrole2 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialdecription2 = models.TextField(default = '',blank=True)
    testimonial3 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialrole3 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialdecription3 = models.TextField(default = '',blank=True)
    testimonial4 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialrole4 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialdecription4 = models.TextField(default = '',blank=True)
    testimonial5 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialrole5 = models.CharField(max_length=100,default = '',blank=True) 
    testimonialdecription5 = models.TextField(default = '',blank=True) 
    location1 = models.CharField(max_length=100,default = '',blank=True) 
    location2 = models.CharField(max_length=100,default = '',blank=True  )
    contact1 = models.CharField(max_length=100,default = '',blank=True) 
    contact2 = models.CharField(max_length=100,default = '',blank=True  )
    Amount1 = models.CharField(max_length=100,default = '',blank=True  )
    Amount2 = models.CharField(max_length=100,default = '',blank=True  )
    Amount3 = models.CharField(max_length=100,default = '',blank=True  )
    Amount4 = models.CharField(max_length=100,default = '',blank=True  )
    Amount5 = models.CharField(max_length=100,default = '',blank=True  )
    Amount6 = models.CharField(max_length=100,default = '',blank=True  )
    status1 = models.CharField(max_length=100,default = '',blank=True  )
    status2 = models.CharField(max_length=100,default = '',blank=True  )
    status3 = models.CharField(max_length=100,default = '',blank=True  )
    status4 = models.CharField(max_length=100,default = '',blank=True  )
    status5 = models.CharField(max_length=100,default = '',blank=True  )
    status6 = models.CharField(max_length=100,default = '',blank=True  )
    genderequity = models.CharField(max_length=100,default = '',blank=True  )
    skills = models.CharField(max_length=100,default = '',blank=True  )
    education = models.CharField(max_length=100,default = '',blank=True  )
    climatechange = models.CharField(max_length=100,default = '',blank=True  )
    livelihoods = models.CharField(max_length=100,default = '',blank=True  )
    sustainabledevelopment = models.CharField(max_length=100,default = '',blank=True  )




    class Meta:  
        db_table = "about" 




class Partner(models.Model):  
    partnername = models.CharField(max_length=100,default = '',blank=True)  
    partnerdescription = models.TextField(default = '',blank=True) 
    partner_main_img = models.ImageField(upload_to='images/' , default = '')   
  
    class Meta:  
        db_table = "partner" 


class Member(models.Model):  
    membername = models.CharField(max_length=100,default = '',blank=True) 
    memberemail = models.EmailField(default = '')  
    memberusername = models.ImageField(upload_to='images/' , default = '')   
  
    class Meta:  
        db_table = "member" 



class Activity(models.Model):
    activitytitle = models.CharField(max_length=50,default = '')
    activitydescription = models.TextField(default = '')
    activity_main_img1 = models.ImageField(upload_to='images/',default = '' )
    activity_main_img2 = models.ImageField(upload_to='images/',default = '') 
    activity_main_img3 = models.ImageField(upload_to='images/',default = '' ) 
    activity_main_img4 = models.ImageField(upload_to='images/', default = '') 
    activity_main_img5 = models.ImageField(upload_to='images/', default = '')  
    activity_main_img6 = models.ImageField(upload_to='images/', default = '')

    class Meta:  
        db_table = "activity" 