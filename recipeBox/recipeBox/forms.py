
from django import forms
from django.db import models
from recipeBox.models import Author


class Add_Author(forms.Form):
    name = forms.CharField(label="Author Name", max_length=100)
    bio = forms.CharField(widget=forms.Textarea)

class Add_Recipe(forms.Form):
    title = forms.CharField(label="Recipe Title", max_length=2000)
    time = forms.CharField(label="Cooking Time (includes prep time)", max_length=2000)
    description = forms.CharField(label="Description", max_length=2000)
    instructions = forms.CharField(label="Instructions", max_length=2000)
    # talk to db to get a query set (generates a dropdown of all objects)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

