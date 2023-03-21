
from django import forms
from django.forms import TextInput, Textarea
from .models import Feedback

class FeedbackCreateForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """

    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')
        widgets = {
            'subject': TextInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Username'
                }),
            'email': TextInput(attrs={
                'class': "form-control", 
                'style': '',
                'placeholder': 'email / Telegram / vk / instagram'
                }),
            'content': Textarea(attrs={
                'class': 'from-control',
                'style': '',
                'placeholder': 'Опишите Ваши впечатления / замечания / предложения'
            })
        }

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})