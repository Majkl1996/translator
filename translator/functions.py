from django.contrib.auth.models import User
from googletrans import Translator

# Funkcja do rejestracji nowego użytkownika
def create_user(login, email, password):
    login = # pobierz z formularza
    email = # pobierz z formularza
    password =  # pobierz z formularza
    user = User.objects.create_user(login, email, password)


def translation(text):
    text =
    translator = Translator()
    transl_result = translator.translate(text, dest='pl')
    return transl_result

