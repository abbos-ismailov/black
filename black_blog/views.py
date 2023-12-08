from django.shortcuts import render
from .models import Blog


# Create your views here.
def HomePage(request):
    data = Blog.objects.filter(is_active=True).order_by("-update_at")[:12]
    for i in data:
        i.body = i.body[0:300]
    context = {"blog_home": data}
    return render(request, "index.html", context)
