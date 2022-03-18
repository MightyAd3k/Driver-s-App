from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import LoginForm, CreateUserForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'form.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return HttpResponse('Error')
        return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        retrieved_value = super().form_valid(form)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return retrieved_value
