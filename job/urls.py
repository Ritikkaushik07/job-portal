"""
URL configuration for job project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('index1/', views.SignupPage1, name='signup1'),
    path('login/', views.LoginPage, name='login'),
    path('login1/', views.LoginPage1, name='login1'),
    path('home/', views.HomePage, name='home' ), 
    path('home1/', views.HomePage1, name='home1' ),
    path('logout/', views.logoutPage ,name='logout'),
    path('profile1/', views.Profile1 ,name='profile1'),
    path('pedit/',views.Pedit, name='pedit'),
    path('add/',views.ADD, name='add'),
    path('edit/',views.Edit, name='edit'),
    path('update/<str:id>',views.Update, name='update'),
    path('delete/<str:id>',views.Delete, name='delete'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('applications/', views.Applications, name='applications' ),
    path('apply-to-job/<str:id>', views.apply_to_job, name='apply-to-job' ),

]
