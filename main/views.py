from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import (
    Guide,
    CommunityPost,
    Comment,
    Phrase
)


def home(request):

    total_guides = Guide.objects.count()

    total_posts = CommunityPost.objects.count()

    total_phrases = Phrase.objects.count()

    context = {
        'total_guides': total_guides,
        'total_posts': total_posts,
        'total_phrases': total_phrases
    }

    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')


def dashboard(request):

    context = {
        'guides_count': Guide.objects.count(),
        'posts_count': CommunityPost.objects.count(),
        'phrases_count': Phrase.objects.count()
    }

    return render(request, 'main/dashboard.html', context)


def guides(request):

    query = request.GET.get('q')

    category = request.GET.get('category')

    guides = Guide.objects.all()

    if query:
        guides = guides.filter(title__icontains=query)

    if category:
        guides = guides.filter(category=category)

    categories = Guide.objects.values_list(
        'category',
        flat=True
    ).distinct()

    context = {
        'guides': guides,
        'categories': categories
    }

    return render(request, 'main/guides.html', context)


def community(request):

    posts = CommunityPost.objects.all().order_by('-created_at')

    context = {
        'posts': posts
    }

    return render(request, 'main/community.html', context)


@login_required
def create_post(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        content = request.POST.get('content')

        CommunityPost.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        return redirect('/community/')

    return render(request, 'main/create_post.html')


@login_required
def add_comment(request, post_id):

    post = get_object_or_404(
        CommunityPost,
        id=post_id
    )

    if request.method == 'POST':

        content = request.POST.get('content')

        Comment.objects.create(
            user=request.user,
            post=post,
            content=content
        )

    return redirect('/community/')


def phrases(request):

    phrases = Phrase.objects.all()

    context = {
        'phrases': phrases
    }

    return render(request, 'main/phrases.html', context)