from .models import Blog, CategoryPost, Navbar, SiteTitle, SocialNetwork, Intervyu, Podcast

def BlogView(request):
    blog_data = Blog.objects.all().order_by("-create_at")[:10]

    context = {
        "last_news": latest_news[1:],
        "last_new": latest_news[0],
    }

    return context
