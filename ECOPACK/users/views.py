from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CustomUser
    fields = ['id','username', 'email', 'name', 'surname',]
    template_name = 'profile.html'
    update_url = 'profile.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', args="1")




