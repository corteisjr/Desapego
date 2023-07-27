from django import forms
from doeja.models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = (
            'name_of_object',
            'description',
            # 'status',
            'picture',
            'category',
        )
        widgets = {
            'category': forms.SelectMultiple(attrs={'class': 'materialize-select'}),
        }