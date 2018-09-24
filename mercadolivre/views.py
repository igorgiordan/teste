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
from datetime import date
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
        return HttpResponseRedirect('/')
    def get_context_data(self, **kwargs):
        data = date.today()
        data2 = date.fromordinal(data.toordinal()+1)
        kwargs['data'] = str(data2)
        return super(CreateProduto, self).get_context_data(**kwargs)

class Home(ListView):
    model = models.Produto
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        kwargs['produtos'] = models.Produto.objects.filter(status=1)
        data = date.today()
        produtos = models.Produto.objects.filter(status=1)
        for x in produtos:
            if (data > x.datafim) or (data == x.datafim):
                models.Produto.objects.filter(id=x.id).update(status=2)
        return super(Home, self).get_context_data(**kwargs)

class ExibirProduto(DetailView):
    model = models.Produto
    template_name = 'produto.html'
    maximo2 = None
    def get(self, request, pk):
        oferta = 0
        if(len(self.request.GET)):
            oferta = float(self.request.GET['oferta'])
        produto = models.Produto.objects.get(id = pk)
        oferta_user = models.Oferta.objects.filter(user=models.User.objects.get(id=self.request.user.pk), produto=produto)
        ofertas = models.Oferta.objects.filter(produto=produto)
        aux = []
        for x in ofertas:
            aux.append(x.oferta)
        if (len(aux)):
            maximo = max(aux)
        else:
            maximo = 0
        if (len(oferta_user)):
            if (oferta > float(produto.lancemin)) and (oferta > float(maximo)):
                models.Oferta.objects.filter(user=models.User.objects.get(id=self.request.user.pk), produto=produto).update(oferta=oferta)
        else:
            if (oferta > float(produto.lancemin)) and (oferta > float(maximo)):
                obj = models.Oferta.objects.create(user=models.User.objects.get(id=self.request.user.pk), produto=produto, oferta=oferta)
                obj.save()
        self.maximo2 = maximo
        return super(ExibirProduto, self).get(request, pk)
    def get_context_data(self, **kwargs):
        kwargs['maximo'] = self.maximo2
        return super(ExibirProduto, self).get_context_data(**kwargs)
        
class Lance(ListView):
    model = models.Oferta
    template_name = 'lance.html'
    success_url = reverse_lazy('home')
    def get(self, request):
        return super(Lance, self).get(request, pk)

class AllLances(ListView):
    model = models.Oferta
    template_name = 'all-lances.html'
    id1 = None
    def get(self, request, pk):
        self.id1 = pk
        return super(AllLances, self).get(request, pk)
    def get_context_data(self, **kwargs):
        ofertas = models.Oferta.objects.all()
        of = []
        for x in ofertas:
            if (int(x.produto.id) == int(self.id1)):
                of.append(x)
        kwargs['ofertas'] = of
        maximo2 = []
        if (len(of)):
            for x in of:
                maximo2.append(x.oferta)
            kwargs['maximo'] = max(maximo2)
            usermax = models.Oferta.objects.get(oferta = max(maximo2))
            kwargs['usermax'] = usermax.user
        else:
            kwargs['maximo'] = ' - '
            kwargs['usermax'] = 'Ninguém'
        return super(AllLances, self).get_context_data(**kwargs)

class Bought(ListView):
    model = models.Oferta
    template_name = 'comprados.html'
    def get_context_data(self, **kwargs):
        ofertas_user2 = models.Oferta.objects.filter(user=models.User.objects.get(id=self.request.user.pk))
        ofertas_user = []
        for x in ofertas_user2:
            if x.produto.status == 2:
                ofertas_user.append(x)
        arrematados = []
        for oferta in ofertas_user:
            produto = oferta.produto.id
            lances = []
            aux = models.Oferta.objects.filter(produto = produto)
            for x in aux:
                lances.append(x.oferta)
            lance_max = max(lances)
            lance_user = models.Oferta.objects.get(id = oferta.id, user=models.User.objects.get(id=self.request.user.pk))
            lance_user2 = lance_user.oferta
            print(lance_user2)
            if lance_max == lance_user2:
                arrematados.append(oferta)
        kwargs['arrematados'] = arrematados
        return super(Bought, self).get_context_data(**kwargs)