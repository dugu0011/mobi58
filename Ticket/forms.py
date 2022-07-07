from pyexpat import model
from tkinter import Widget
from .models import *
from django import forms
from django.utils.text import slugify
from django.forms import RadioSelect, fields, ModelForm


from .models import RaiseTicket


class RaiseTicketForm(ModelForm):
    class Meta:
        model=RaiseTicket
        fields=('category','subcategory','img','subject','msg','priority', 'Type')
        widgets = {'Type': forms.RadioSelect(attrs={
            'class' : 'form-check-input radio'
        })}
        


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=('message',)    





