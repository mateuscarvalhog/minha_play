from django.forms import ModelForm
from .models import Faixa

class FaixaForm(ModelForm):
    class Meta:
        model = Faixa
        fields = '__all__'