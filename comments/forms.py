from django import forms
from .models import Comment,AnswerComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body')

class AnswerCommentForm(forms.ModelForm):
    class Meta:
        model = AnswerComment
        fields = ('body')