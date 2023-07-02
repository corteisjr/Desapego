from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'input-field'}),
        label="Usuário"
        )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={'class': 'input-field'}
        ),
        required=True, 
        label='Senha'
    )