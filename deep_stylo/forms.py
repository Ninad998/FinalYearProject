# coding=utf-8
from __future__ import unicode_literals

from django import forms
from models import Result

# Create your forms here.

class QueryForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ('doc_id', 'authorList',)

    def clean(self):
        form_doc_id = self.cleaned_data.get('doc_id')
        form_authorList = self.cleaned_data.get('authorList')
        form_authorList = form_authorList + ", "
        authorList = form_authorList.split(",")
        if len(authorList) > 1:
            if authorList[len(authorList) - 1] != "" and authorList[len(authorList) - 1] > 0:
                #Remove space element in list
                if " " in authorList:
                    authorList = space_remover(authorList)

                # Remove blank element in list
                if "" in authorList:
                    authorList = blank_remover(authorList)

                if len(authorList) > 1:
                    form_authorList = ', '.join([str(auth) for auth in authorList])
                    self.data[u'authorList'] = form_authorList
                    self.cleaned_data[u'authorList'] = form_authorList
                else:
                    raise forms.ValidationError("Author List too short")
            else:
                raise forms.ValidationError("Author List input incorrect")
        else:
            raise forms.ValidationError("Author List too short")
        super(QueryForm, self).clean()

def space_remover(authorList):
    if " " in authorList:
        authorList.remove(" ")
        return space_remover(authorList)
    else:
        return authorList

def blank_remover(authorList):
    if "" in authorList:
        authorList.remove("")
        return blank_remover(authorList)
    else:
        return authorList