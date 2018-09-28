"""
Definition of urls for periject.
"""

from django.conf.urls import include, url
from django.contrib import admin
#from periject.account import 
from periject.account import urls
from periject.account import views
from periject.Dashboard import views
from periject.grc import views
from periject.proj import views
from periject.supplier import views
from django.urls import path
from periject.proj import urls
from periject.todo import urls
from periject.assurance import views 
#from periject.Dashboard import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^account/',include('periject.account.urls',namespace='account')),
    url(r'^account/',include('django.contrib.auth.urls')),
    url(r'^dashboard/$',views.DashBoard.as_view(),name='dashboard'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    #url(r'^projects/$',views.ProjectsPage.as_view(),name='projects'),
    url(r'^suppliers/$',views.SupplierPage.as_view(),name='suppliers'),
    url(r'^grc/$',views.GRCPage.as_view(),name='grc'),
    url(r'^support/$',views.SupportPage.as_view(),name='support'),
   # url(r'session_security/', include('session_security.urls')),
   #url(r'^projects/newproject/$',views.CreateNewProject.as_view(),name='newproject'),
   #url(r'^projects/newproject/newassurance/$',views.CreateNewAssurance.as_view(),name='newassurance'),
   #url(r'^projects/newproject/newsupplier/$',views.CreateNewSupplier.as_view(),name='newsupplier'),
   #url(r'^projects/newproject/newgrc/$',views.CreateNewGRC.as_view(),name='newgrc'),  
   path('newproject/', include('periject.todo.urls', namespace="todo")),
   url(r'^assurance/$',views.AssurancePage.as_view(),name='assurance'),
]
