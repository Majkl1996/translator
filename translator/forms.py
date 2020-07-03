from django import forms
from django.core.validators import EmailValidator, URLValidator, validate_email, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# from .models import SCHOOL_CLASS, GRADES, PIZZA_SIZES, Student, SchoolSubject, Toppings, Message, StudentNotice
import datetime
# from .validators import validate_static_range, validate_female_name


def year_choices():
    current_year = datetime.date.today().year
    return [(r, r) for r in range(current_year - 100, current_year - 5)]

def estimate_student_year():
    return datetime.date.today().year - 19

def students_last_name():
	return Student.objects.all().order_by('last_name').values_list('last_name','last_name')

def subjects_names():
	return SchoolSubject.objects.all().order_by('name').values_list('name', 'name')

def toppings_names():
	return Toppings.objects.all().order_by('name').values_list('id', 'name')


class StudentSearchForm(forms.Form):
	last_name = forms.CharField(label='Nazwisko studenta', max_length=100)

class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=16)
    password = forms.CharField(label='Hasło', max_length=32, widget=forms.PasswordInput)

class TranslateForm(forms.Form):
    input_text = forms.CharField(label="Wprowadź text")

class PersonForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=48)
    last_name = forms.CharField(label='Nazwisko', max_length=64)
    #email = forms.CharField(label='Email', max_length=112, validators=[validate_email])
    email = forms.CharField(label='Email', max_length=112, validators=[EmailValidator()])
    #email = forms.CharField(label='Email', max_length=112, widget=forms.EmailInput, validators=[EmailValidator()])
    www = forms.CharField(label='Ulubiona strona www', max_length=256, validators=[URLValidator()])



class UserLoginForm(forms.Form):
    username = forms.CharField(label = 'Login')
    password = forms.CharField(label = 'Hasło', widget = forms.PasswordInput)


class UserCreateForm(forms.ModelForm):
    password2 = forms.CharField(label = 'Password (again)', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            msg = 'Podane hasła są różne'
            self._errors['password2'] = self.error_class([msg])
            del self.cleaned_data['password2']

            '''
            Dla non-field error:
            from django.forms.forms import NON_FIELD_ERRORS
            form._errors[NON_FIELD_ERRORS] = form.error_class(['komunikat'])
            '''

        return self.cleaned_data


class UserResetPasswordForm(forms.Form):
    password = forms.CharField(label = 'Hasło', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Hasło (ponownie)', widget = forms.PasswordInput)

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError(
                    'Podane hasła są różne'
                )
