from django import forms

from . import models

class AddProdutoForm(forms.ModelForm):
  
  class Meta:
    model = models.Produto
    fields = ['nome', 'descricao', 'datafim', 'lancemin']