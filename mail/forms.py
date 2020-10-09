from django import forms
from . models import FormM
from django import forms


class Subscribe(forms.ModelForm):

	class Meta:
		model = FormM
		fields = ['email','Subject','Message']

