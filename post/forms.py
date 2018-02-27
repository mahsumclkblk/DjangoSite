from django import forms
from .models import Post
from django.contrib.auth.models import User
class DetailForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(DetailForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={"class":"form-control"}
        self.fields["interested_1"].widget.attrs["rows"]=15
        self.fields["interested_2"].widget.attrs["rows"]=15
        self.fields["interested_3"].widget.attrs["rows"]=15
        self.fields["who"].widget.attrs["rows"]=15
        self.fields["what_to_do"].widget.attrs["rows"]=15

    class Meta:
        model=Post
        fields=['title','image1','who','what_to_do','interested_1','img1','interested_2','img2','interested_3','img3',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=100, required=True,widget=forms.PasswordInput(attrs={"class": "form-control"}))

class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
        ]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        return password2
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}
        
class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields =["first_name","last_name","username","email"]

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}
