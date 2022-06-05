from django import forms
from .models import Announs


class AnnounsForm(forms.ModelForm):

    class Meta:
        model = Announs
        fields = ('header', 'Author', 'text',)

        widgets = {
            "header": forms.TextInput(attrs ={
                'class':'form-control',
                'placeholder':'Заголовок обьявления'
            }),
            "Author": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст обьявления'
            })
        }