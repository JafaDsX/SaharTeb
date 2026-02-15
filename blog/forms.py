
from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-secondary text-white',
                'placeholder': 'اسمك',
                'name': 'name',
                'style': 'background: #191c44 !important;',
                'id': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-secondary text-white',
                'placeholder': 'بريدك الإلكتروني',
                'name': 'email',
                'id': 'email',
                'style': 'background: #191c44 !important;',


            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control border-secondary text-white',
                'placeholder': 'اكتب تعليقك هنا...',
                'name': "content",
                'id': 'content',
                'style': 'background: #191c44 !important;',

            }),
        }
