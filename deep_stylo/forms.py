# coding=utf-8
from __future__ import unicode_literals

from django import forms
from models import Result

# Create your forms here.

class QueryForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ('doc_id', 'authorList',)