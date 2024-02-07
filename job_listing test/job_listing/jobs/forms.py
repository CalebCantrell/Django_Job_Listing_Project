from django import forms
from .models import Job

class JobSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'description', 'location', 'requirements', 'app_deadline']

class JobApplicationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Email Address")
    resume = forms.FileField(label="Upload Resume (PDF only)", help_text="Please upload a PDF file")