from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    asunto = forms.CharField(label="Asunto", max_length=100)
    mensaje = forms.CharField(label="¿Qué quieres decirnos?", widget=forms.Textarea)