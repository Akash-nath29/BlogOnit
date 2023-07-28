from django import forms
from .models import Post, Category

# choices = [('entertainment', 'entertainment'), ('sports', 'sports'), ('coding', 'coding')]
choices = Category.objects.all().values_list('name', 'name')

tag_list = []

for item in choices:
    tag_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border-3'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control border-3'}),
            'author': forms.TextInput(attrs={'class': 'form-control border-3', 'value':"", 'id':"name", "type":"hidden"}),
            # 'author': forms.Select(attrs={'class': 'form-control border-3'}),
            'category': forms.Select(choices=tag_list, attrs={'class': 'form-control border-3'}),
            'body': forms.Textarea(attrs={'class': 'form-control border-3'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control border-3'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border-3'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control border-3'}),
            'body': forms.Textarea(attrs={'class': 'form-control border-3'}),
        }