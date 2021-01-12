from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authorization.forms import RegisrationForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import auth
from authorization.models import UserProfile, User
from authorization.forms import LoginForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print(form)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse_lazy('animal_shelter:index'))
        context = {'message': f"Имя пользователя или пароль указаны не верно"}
        return render(request, 'login.html', context)

    else:
        context = {'form': AuthenticationForm()}
        return render(request, 'login.html', context)


# register/ класс регистрации пользователя
class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        auth.login(self.request, auth.authenticate(username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)

def register(request):
    if request.method == 'POST':

        form = RegisrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            auth.login(request, auth.authenticate(username=username, password=raw_password))
            context = {
                'trigger': True,
                'message': 'Регистрация успешно завершена'
            }
            return HttpResponseRedirect(reverse_lazy('animal_shelter:index'))

        context = {
            'trigger': False,
            'message': 'Регистрация не завершена',
            'form': RegisrationForm(),
        }
        return render(request, 'registration.html', context)
    else:
        context = {'form': RegisrationForm()}
        return render(request, 'registration.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm()
        print(form)
        print(form.is_valid())
        if form.is_valid():
        # print(form)
        # print(form.save(commit=False))
            instance = form.save(commit=False)
            # print(instance)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse_lazy('animal_shelter:index'))
        context = {
            'form': UserProfileForm(),
        }
        return render(request, 'profile.html', context)
    else:
        context = {
            'form': UserProfileForm()
        }
        return render(request, 'profile.html', context)


