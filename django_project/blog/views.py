from django.shortcuts import render


posts = [
  {
    'author': 'Jason',
    'title': 'Post 1',
    'content': 'First Post!',
    'date_posted': 'February 9, 2026'
  },
  {
    'author': 'Cornelius',
    'title': 'Post 2',
    'content': "I'm a fish!",
    'date_posted': 'February 9, 2026'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html',{'title':"about"})

