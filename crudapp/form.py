from django.forms import ModelForm
from .models import GradeStudent


class courseform (ModelForm):
    class Meta:
        model = GradeStudent
        fields = '__all__'
