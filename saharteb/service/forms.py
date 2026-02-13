from django import forms
from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = [
            "name",
            "phone",
            "service",
            "requested_date",
            "doctor",
            "translator",
            "description",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "الاسم الكامل",
                'name': 'name'
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "009",
                'name':'phone'
            }),
            "service": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "الخدمة",
                'name': 'service'
            }),
            "requested_date": forms.DateInput(attrs={
                    "type": "date",
                    "class": "form-control",
                    'name': 'requested_date'
                }),
            "doctor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "پزشک (در صورت انتخاب)",
                'name': 'doctor'
            }),
            "translator": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "مترجم (در صورت نیاز)",
                'name': 'translator',
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "توضیحات تکمیلی",
                "rows": 4,
                'name': 'description'
            }),
        }
