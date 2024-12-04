from django import forms
from hospital_admin.models import HospitalAdmin,Article

class HospitalAdminForm(forms.ModelForm):
    class Meta:
        model = HospitalAdmin
        fields = '__all__'



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =  '__all__'