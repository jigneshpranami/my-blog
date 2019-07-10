from django import forms
from .models import Opinion,Comment

class OpinionForm(forms.ModelForm):
	class Meta:
		model=Opinion
		fields=('title','text',)
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)