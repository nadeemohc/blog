from django import forms
from .models import UserProfile

style = 'form-control'

class Signup(forms.ModelForm):
    con_pass = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': style,
                'placeholder': "Re-enter your password"
            }
        ),
        label='Confirm Password'
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'gender', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                        'class': style,
                        'placeholder': "Enter the username"
                        }),
            'gender': forms.Select(attrs={
                    'class': style,
                    }),
            'email': forms.EmailInput(attrs={
                    'class': style,
                    'placeholder': 'Enter your E-mail'
                    }),
            'password': forms.PasswordInput(attrs={
                'class': style,
                'placeholder':'Enter the password',
            })
        }

    def conf_pass_check(self):
        password = self.cleaned_data.get('password')  # Fix the typo here
        con_pass = self.cleaned_data.get('con_pass')

        if password and con_pass and password != con_pass:
            raise forms.ValidationError("Password does not match")

        return con_pass

class loginform(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': style,
                'placeholder': 'Enter the username'
            }),
            'password':forms.PasswordInput(attrs={
                'class': style,
                'placeholder': 'Enter the password'
            })
        }