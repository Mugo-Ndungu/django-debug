from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,About,Wedo,WeCanHelp,OurServices,ApeaMembership,JoinUs,PublicPolicy,MyWorkplace,ApeaMember


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'about': About.objects.all(),
        'posts': Post.objects.all(),
        'apeamember': ApeaMember.objects.all(),
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)


def index(request):
    a = About.objects.all()
    context = {
        'about': a,
        'title': 'Home',
        'wedo': Wedo.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)



def wedo(request):

    context = {
        'title': 'Wedo',
        'wedo': Wedo.objects.all(),
        'wehelp': WeCanHelp.objects.all(),
        'services': OurServices.objects.all(),
        'work': MyWorkplace.objects.all(),
    }

    return render(request, 'blog/wedo.html', context)


def membership(request):
    return render(request, 'blog/membership.html', {'title': 'membership'})


def join(request):
    return render(request, 'blog/join.html', {'title': 'join'})



def sign(request):
    return render(request, 'blog/sign.html', {'title': 'sign'})


def weare(request):
    return render(request, 'blog/weare.html', {'title': 'weare'})


def structure(request):
    return render(request, 'blog/structure.html', {'title': 'weare'})

