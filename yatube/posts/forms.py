from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        error = 'Поле "Текст поста" должно быть заполнено'
        if data == '':
            raise forms.ValidationError(error)
        return data
