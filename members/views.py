from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from Blogonit.models import UserProfile
from .forms import SignUpForm, EditProfileForm

class UserRegistry(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editProfile.html'
    success_url = reverse_lazy('Home')
    
    def get_object(self):
        return self.request.user
    
class ShowUserProfile(DetailView):
    model = UserProfile
    template_name = "registration/profile.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ShowUserProfile, self).get_context_data(*args, **kwargs)
        the_page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = the_page_user
        return context

class EditUserProfile(generic.UpdateView):
    model = UserProfile
    template_name = "registration/edit_profile.html"