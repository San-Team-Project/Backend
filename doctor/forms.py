from django import forms
from .models import Settings, Doctor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from tinymce import TinyMCE


# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


# class SettingsForm(forms.ModelForm):
#     receive_newsletter = forms.BooleanField()

#     class Meta:
#         model = Settings


# class DoctorForm(forms.ModelForm):

#     about = forms.CharField(
#         widget=TinyMCEWidget(
#             attrs={'required': False, 'cols': 30, 'rows': 10}
#         )
#     )

#     timing = forms.CharField(
#         widget=TinyMCEWidget(
#             attrs={'required': False, 'cols': 30, 'rows': 10}
#         )
#     )
#     class Meta:
#         model = Doctor
#         fields = ('name', 'slug', 'email', 'phone','specialization','photo','about','documents',
#         'address','city','state','country','hospital','hospitallink','portfoliolink','availabel',
#         'timing','experiance')


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class  DoctorForm(forms.ModelForm):
    about = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    timing = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Doctor
        fields = ('name', 'slug', 'email', 'phone','specialization','photo','about','documents',
        'address','city','state','country','hospital','hospitallink','portfoliolink','availabel',
        'timing','experiance')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


