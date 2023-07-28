from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect



class Home(ListView):
    template_name = 'index.html'
    model = Post
    # ordering = ['-id']
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    
class PostView(DetailView):
    template_name = 'postDetails.html'
    model = Post
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context['cat_menu'] = cat_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context
    
class WritePost(CreateView):
    model = Post
    form_class = PostForm
    # fields = ('title', 'body')
    template_name = 'createPost.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'
    # fields = ['title', 'title_tag', 'body']
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('Home')
    
class AddCategory(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'addCategory.html'
    
    
def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats)
    return render(request, 'category.html', {'cats': cats.title(), 'category_post': category_post})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('PostView', args=[str(pk)]))
    