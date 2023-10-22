from django.contrib import admin
from django.urls import path ,include
from romic_employee import views as user_view
from romic_employee import views  
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', views.login, name='blog_login'),
    path('logout', views.logout, name='blog_logout'),


    path('activityupload', views.activity_image_view, name='image_upload'),
    path('activity_images', views.display_activity_image, name = 'acitivity_images'),
    path('showactivity',views.showactivity, name = 'show activities'),
    path('editactivity/<int:id>', views.editactivity, name = 'edit acitivity'),  
    path('updateacitivity/<int:id>', views.updateacitivity, name = 'update acitivity'),  
    path('deleteactivity/<int:id>', views.destroyactivity, name = 'delete activity'),



    path('causeupload', views.cause_image_view, name='image_upload'),
    path('cause_images', views.display_cause_image, name = 'cause_images'),
    path('showcause',views.showcause, name = 'show causes'),
    path('editcause/<int:id>', views.editcause, name = 'edit cause'),  
    path('updatecause/<int:id>', views.updatecause, name = 'update cause'),  
    path('deletecause/<int:id>', views.destroycause, name = 'delete cause'),


    path('serviceupload', views.service_image_view, name='service_upload'),
    path('service_images', views.display_service_image, name = 'service_images'),
    path('showservice',views.showservice, name = 'show services'),
    path('editservice/<int:id>', views.editservice, name = 'edit service'),  
    path('updateservice/<int:id>', views.updateservice, name = 'update service'),  
    path('deleteservice/<int:id>', views.destroyservice, name = 'delete service'),

    path('emp', views.emp),  
    path('show',views.show, name = 'show employee'),  
    path('employeeimages', views.display_employee_image, name = 'display_employee'),
    path('edit/<int:id>', views.edit, name = 'edit employee'),  
    path('update/<int:id>', views.update, name = 'update employee'),  
    path('delete/<int:id>', views.destroy, name = 'delete employee'),


    path('blog', views.blog),  
    path('showblog',views.showblog, name = 'show blog'), 
    path('displayblog', views.displayblog, name = 'display_blogs'), 
    path('editblog/<int:id>', views.editblog, name = 'edit blog'),  
    path('updateblog/<int:id>', views.updateblog, name = 'update blog'),  
    path('deleteblog/<int:id>', views.destroyblog, name = 'delete blog'), 

    path('partner', views.partner_image_view),  
    path('showpartner',views.showpartner, name = 'show partner'), 
    path('displaypartner', views.display_partner_image, name = 'display_partners'), 
    path('editpartner/<int:id>', views.editpartner, name = 'edit partner'),  
    path('updatepartner/<int:id>', views.updatepartner, name = 'update partner'),  
    path('deletepartner/<int:id>', views.destroypartner, name = 'delete partner'),


    path('blog', views.blog),  
    path('showblog',views.showblog, name = 'show blog'), 
    path('displayblog', views.displayblog, name = 'display_blogs'), 
    path('editblog/<int:id>', views.editblog, name = 'edit blog'),  
    path('updateblog/<int:id>', views.updateblog, name = 'update blog'),  
    path('deleteblog/<int:id>', views.destroyblog, name = 'delete blog'),



    path('about', views.about),  
    path('showabout',views.showabout, name = 'show about'),
    path('', views.showuserabout ), 
    path('editabout/<int:id>', views.editabout, name = 'editabout'),  
    path('updateabout/<int:id>', views.updateabout, name = 'updateabout'),  
    path('deleteabout/<int:id>', views.destroyabout, name = 'deleteabout'), 


    path('contact', views.contact),  
    path('dashboard',views.showcontact, name = 'dashboard'),  
    path('editcontact/<int:id>', views.editcontact, name = 'edit contact'),  
    path('updatecontact/<int:id>', views.updatecontact, name = 'update contact'),  
    path('deletecontact/<int:id>', views.destroycontact, name = 'delete contact'), 









]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)