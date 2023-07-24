from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'input-field, left-align'}),
        label="Usuário"
        )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={'class': 'input-field,left-align'}
        ),
        required=True, 
        label='Senha'
    )
    
class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email  = forms.CharField(required=True)
    password = forms.CharField(max_length=32)
    role = forms.ChoiceField(
        choices=(
            (2, 'Doador'),
            (3, 'Receptor'),
        ),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True,
        label='',
    )