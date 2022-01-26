from django.shortcuts import render

# Create your views here.

def starting_page(request):  #path("")
    return render(request, "blog/index.html")


def posts(request):  #path("posts")
    return render(request, "blog/all-posts.html")


def post_details(request):  #path("posts/<slug:slug>")
    pass