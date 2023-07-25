from django import forms
from models.Donations import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = (
            '__all__'
        )