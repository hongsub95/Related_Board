from django.forms import ModelForm
from .models import Board

class BoardCreateForm(ModelForm):
    class Meta:
        model = Board
        fields = ["title","content"]