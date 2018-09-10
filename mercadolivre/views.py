from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import random
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . import models
import operator
from . import forms
import datetime

class RegisterUser(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'cadastrousuario.html'

class CreateProduto(CreateView):
    model = models.Produto
    template_name = 'cadastroproduto.html'
    success_url = reverse_lazy('home')
    form_class = forms.AddProdutoForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = models.User.objects.get(id=self.request.user.pk)
        obj.save()
        return super(CreateProduto, self).form_valid(form)

class Home(ListView):
    model = models.Produto
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        kwargs['produtos'] = models.Produto.objects.all()
        print ( kwargs['produtos'])
        return super(Home, self).get_context_data(**kwargs)