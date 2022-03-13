from dataclasses import field, fields
from pyexpat import model
from django import forms
from CRUDOperation.models import EmpModel

class Empforms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields="__all__"