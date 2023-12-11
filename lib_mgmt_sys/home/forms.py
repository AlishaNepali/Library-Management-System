from django import forms
from .models import Author, Book


# DjnagoForm
class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()



#ModelForm
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'