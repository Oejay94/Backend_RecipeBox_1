
from django import forms
from django.db import models
from django.contrib.auth.models import User
from recipeBox.models import Author, Recipe


class Add_Author(forms.Form):
    name = forms.CharField(label="Author Name", max_length=100)
    bio = forms.CharField(widget=forms.Textarea)


class Add_Recipe(forms.Form):
    title = forms.CharField(label="Recipe Title", max_length=2000)
    time = forms.CharField(
        label="Cooking Time (includes prep time)", max_length=2000)
    description = forms.CharField(label="Description", max_length=2000)
    instructions = forms.CharField(label="Instructions", max_length=2000)
    # talk to db to get a query set (generates a dropdown of all objects)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


class Edit_Form(forms.Form):
    title = forms.CharField(max_length=2000)
    time = forms.CharField(max_length=2000)
    description = forms.CharField(max_length=2000)
    instructions = forms.CharField(max_length=2000)
