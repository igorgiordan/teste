from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta

now = datetime.now()

#Produto
#Leilao
#Oferta

class Produto(models.Model):
    kindchoice = (
        (1, 'Ativo'),
        (2, 'Não ativo')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', verbose_name='user')
    nome = models.CharField(max_length=150, verbose_name='nome')
    descricao = models.TextField(verbose_name='Descrição')
    datafim = models.DateField(auto_now=False, verbose_name='Data final')
    lancemin = models.FloatField(default=0, verbose_name='lance mínimo')
    status = models.IntegerField(choices=kindchoice, verbose_name="tipo", default=1)

    def __str__(self):
     return self.nome
    
    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

class Oferta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user5', verbose_name='user')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto', verbose_name='produto')
    oferta = models.FloatField(default=0, verbose_name='oferta')

    def __str__(self):
     return "Oferta"
    
    class Meta:
        verbose_name = 'oferta'
        verbose_name_plural = 'ofertas'
