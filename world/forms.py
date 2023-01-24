
from django.contrib.gis import forms


from .models import Memory


class AddMemoryForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'description', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'location': forms.OSMWidget
        }

