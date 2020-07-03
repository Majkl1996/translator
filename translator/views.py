from django.views import View
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from googletrans import Translator


# from .models import Product, Category
from .forms import LoginForm, UserLoginForm, TranslateForm


class HomeView(View, LoginRequiredMixin):
    def get(self, request):
        return render(request, "home.html", locals())

class TranslateView(View):
    def get(self, request):
        # form = TranslateForm()
        return render(request, "translate.html")

    def post(self, request):
        text = self.request.POST['getInputText']
        # form = TranslateForm(request.POST)
        # if form.is_valid():
        #     text = form.cleaned_data.get('input_text')
        translator = Translator()
        transl_result = translator.translate(text, dest='pl', src='nl')
        #     form.add_error(None, transl_result.text)
        # transl_result
        return render(request, "translate.html")


class DictionaryView(View):
    def get(self, request):
        return render(request, "dictionary.html", locals())

class UploadView(View):
    def get(self, request):
        return render(request, "upload.html", locals())


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "user_login.html", {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():  # uruchomienie walidacji
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    return redirect(reverse('home'))
                else:
                    form.add_error(None, "Konto nie jest aktywne")
            else:
                # user is None
                form.add_error(None, "Nieprawidłowy login lub hasło")
        return render(request, "user_login.html", {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))