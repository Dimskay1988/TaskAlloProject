from django import forms
from .models import Announs, ImagePost


class AnnounsForm(forms.ModelForm):

    class Meta:
        model = ImagePost
        fields = ('header', 'Author', 'text', 'image_content')

        widgets = {
            "header": forms.TextInput(attrs ={
                'class':'form-control',
                'placeholder':'Заголовок обьявления'
            }),
            "Author": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст обьявления'
            }),
            "image_content": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Загрузите изображение'
            })
        }