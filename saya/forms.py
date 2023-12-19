from django import forms
from .models import DaftarForm

gender =( 
    ("1", "Laki-Laki"), 
    ("2", "Perempuan"), 
) 

class DaftarForm(forms.ModelForm):
    class Meta:
        model = DaftarForm
        fields = "__all__"
    judul = forms.CharField(max_length=200)
    konten = forms.ChoiceField(choices= gender)
    date = forms.DateField()
