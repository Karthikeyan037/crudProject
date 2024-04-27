from django import forms
from crudApp.models import employee

# Create your forms here.
class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        #exclude = ('mail_add',)
    
