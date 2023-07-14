from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_details.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_details(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_details.html', {'category': category})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_details.html', {'author': author})
