from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for adding a comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)
