from django import forms
from ..models import Sermon

class Sermon(forms.ModelForm):
	class Meta:
		model = Testimonial
		fields = '__all__'
	sermon_id = forms.CharField(required=True)
	sermon_upload_date = forms.DateField(required=True)
	sermon_date = forms.DateField(required=False)
	sermon_title = forms.CharField(required=True, max_length=100)
	sermon_description = forms.CharField(required=True, max_length=1000)
	sermon_content = forms.CharField(required=True, max_length=20000)
	sermon_author = forms.CharField(required=True, max_length=70)
	sermon_location = forms.CharField(required=False, max_length=70)
class TestimonialEntry(forms.Form):
        sermon_date = forms.DateField(required=False)
        sermon_title = forms.CharField(required=True, max_length=100)
        sermon_description = forms.CharField(required=True, max_length=1000)
        sermon_content = forms.CharField(required=True, max_length=20000)
        sermon_author = forms.CharField(required=True, max_length=70)
        sermon_location = forms.CharField(required=False, max_length=70)
