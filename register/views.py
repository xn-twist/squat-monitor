from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegistrationForm


class Index(generic.TemplateView):
    template_name = 'register/login.html'


class Registration(generic.View):
    form_class = RegistrationForm
    template_name = "register/registration.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('twister:index')

        return render(request, self.template_name, {'form': form})
