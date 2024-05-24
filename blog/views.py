# views.py
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Tag
from django.shortcuts import render



class HomePageView(TemplateView):
    template_name = 'accounts/home.html'

class PostListView(ListView):
        model = Post
        template_name = 'blog/post_list.html'
        context_object_name = 'posts'
        paginate_by = 5  # Number of posts per page

    
        def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                return Post.objects.filter(title__icontains=query)
            else:
                return Post.objects.all().order_by('-created_at')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['query'] = self.request.GET.get('q', '')
            return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title  
        return context
    
class TaggedPostListView(ListView):
         
        model = Post
        template_name = 'blog/tagged_post_list.html'
        context_object_name = 'posts'

        def get_queryset(self):
            tag_slug = self.kwargs.get('tag_slug')
            tag = Tag.objects.filter(slug=tag_slug).first()
            return Post.objects.filter(tags=tag)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tag'] = Tag.objects.filter(slug=self.kwargs.get('tag_slug'))
            return context