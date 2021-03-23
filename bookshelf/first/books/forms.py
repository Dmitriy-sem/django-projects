from django import forms
from .models import Book, Comment


class NewBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].empty_label = 'Категория'

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image', 'subcategory']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название книги'}),
            'author': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Автор книги'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Описание'}),
            'image': forms.FileInput(attrs={'class': 'image-input'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating', ]
        widgets = {
            'rating': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'max': 5, 'min': 0,
                                             'placeholder': 'Рейтинг(от 0 до 5)'}),
            'content': forms.Textarea(attrs={'class': 'form-control',  'placeholder': 'Добавьте Ваш комментарий'}),
        }


