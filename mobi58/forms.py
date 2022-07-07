from django import forms
from .models import Transporter

class AddTransporterForm(forms.ModelForm):
    class Meta:
        model= Transporter
        fields= ["transporter_name", "email", "mobile", "address","pan_no","pan_file","gst_no","gst_file","cin_no","cin_file"]