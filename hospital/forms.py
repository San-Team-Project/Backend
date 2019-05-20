from django import forms
from .models import Hospital
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class HospitalForm(forms.ModelForm):
  class Meta:
    model = Hospital
    fields = '__all__'

  #  def __init__(self, *args, **kwargs):
  #       super().__init__(*args, **kwargs)
  #       self.helper = FormHelper()
  #       self.helper.form_method = 'post'
  #       self.helper.add_input(Submit('submit', 'Save person'))



