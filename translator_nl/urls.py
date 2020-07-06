"""translator_nl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from translator import views as transl

urlpatterns = [
    path('ajax/', transl.AjaxView.as_view(), name="ajax"),
    path('admin/', admin.site.urls),
    path('login/', transl.UserLoginView.as_view(), name="login"),
    path('register/', transl.registerPage, name="register"),
    path('home/', transl.HomeView.as_view(), name="home"),
    path('translate/', transl.TranslateView.as_view(), name="translate"),
    path('translation/', transl.TranslationView.as_view(), name="translation"),
    path('dictionary/', transl.DictionaryView.as_view(), name="dictionary"),
    path('upload/', transl.UploadView.as_view(), name="upload"),
]
