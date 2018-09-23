from django import forms
from . import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
class AddProdutoForm(forms.ModelForm):
  datafim = forms.DateField(widget=AdminDateWidget)
  class Meta:
    model = models.Produto
    fields = ['nome', 'descricao', 'datafim', 'lancemin']
