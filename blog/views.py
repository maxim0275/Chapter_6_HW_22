from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

import blog
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'publication_flag']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(publication_flag=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_of_views += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'publication_flag']
    template_name = 'blog/blog_form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog:blog_detail', args=(self.object.pk,))


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
