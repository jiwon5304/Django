from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, CreateView, UpdateView, \
    DeleteView
    
## list
# 1)
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100

post_list = PostListView.as_view()

# 2)
# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)

#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })
    
## detail 
# 1)직접 구현시
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # DoesNotExist 예외처리 방법 1
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
    
#     # DoesNotExist 예외처리 방법 2
#     post = get_object_or_404(Post, pk=pk)
    
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#         'object': post,
#     })

# 2)장고 기본 제공 
post_detail = DetailView.as_view(model=Post)

post_archive = ArchiveIndexView.as_view(
	model=Post, 
    date_field='created_at',
    paginate_by=1
 )
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)
