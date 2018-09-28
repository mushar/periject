from django.conf.urls import url
from django.contrib.auth import views as auth_views
from periject.account import views

app_name = 'account'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.SignUp.as_view(),name='signup'),
    ]

