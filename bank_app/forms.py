from django import forms
from .models import Account, Material

class AccountForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    class Meta:
        model = Account
        exclude = ['district', 'branch']  # Exclude district and branch from the form

    address = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 200px; height: 40px;'}))
    account_type_choices = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
        # Add more choices as needed
    ]

    account_type = forms.ChoiceField(choices=account_type_choices, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    materials_provide = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

# from django import forms
# from .models import Account
#
# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = '__all__'

#
# from django import forms
# from .models import Account, District, Branch, Material
#
# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         exclude = ['district', 'branch']
#
#     district = forms.ModelChoiceField(queryset=None, required=True)
#     branch = forms.ModelChoiceField(queryset=None, required=True)
#
#     def __init__(self, *args, **kwargs):
#         super(AccountForm, self).__init__(*args, **kwargs)
#         self.fields['district'].queryset = District.objects.all()
#         self.fields['branch'].queryset = Branch.objects.none()
