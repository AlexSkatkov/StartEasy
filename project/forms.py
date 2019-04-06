from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'customer','pro','goals','problems','connection','yearly_work_plan','cost_and_prodactivity')

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','deadline', 'customer','pro','goals','problems','connection','yearly_work_plan','cost_and_prodactivity','user1','user2','user3','user4','client')
