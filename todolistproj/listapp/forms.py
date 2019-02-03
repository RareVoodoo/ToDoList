from django import forms
from .models import Record


class ListForm(forms.ModelForm):
	class Meta:
		model = Record
		fields = ['text']