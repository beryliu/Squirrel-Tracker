from django.forms import ModelForm
from .models import Squirrel

class Form(ModelForm):

    class Meta:
        model = Squirrel
        fields = '__all__'
