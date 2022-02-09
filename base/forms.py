from django import forms
from .models import Announcement, IstekOneri, Person, Contact,Responser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

GENDER_CHOICES = (
    ('E', 'Erkek'),
    ('K', 'Kadın'),
)


class AddForm(forms.ModelForm):
    tcno = forms.CharField(max_length=11, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : 43221365370'}))
    name_surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Aren Durmaz'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,)
    birth_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : 18.06.1987'}))
    job = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Öğretmen'}))
    birth_city = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Darende,Malatya'}))
    father = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Ahmet'}))
    mother = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Ayşe'}))
    son = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Mehmet'}))
    daughter = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Aylin'}))
    living_city = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Örn : Nilüfer,Bursa'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'mehmet.ali@gmail.com'}))

    class Meta:
        model = Person
        exclude = ['user']


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    email = forms.EmailField(min_length=6, max_length=20, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    password = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))



class ContactForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control"}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control"}))
    desc = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control"}))

    class Meta:
        model = Contact
        fields = "__all__"


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Responser
        fields='__all__'



class AnnouncementForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",'id':'title'}))
    desc = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",'id':'desc'}))
    class Meta:
        model = Announcement
        fields = "__all__"


class IstekOneriForm(forms.ModelForm):
    adsoyad = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",'id':'title'}))
    acıklama = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",'id':'desc'}))
    numara = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','id':'numara','placeholder':'Örneğin : 05352595045','maxlength':'11'}))
    class Meta:
        model = IstekOneri
        fields = "__all__"
