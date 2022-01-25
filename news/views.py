from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.db.models import Q


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 9


def searchResults(request):

    post = Post.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please type something in")
                return redirect(reverse('searchResults'))

            queries = Q(title__icontains=query) | Q(content__icontains=query)
            post = post.filter(queries)


            if not post:            
                messages.error(request, "We could't find any posts by that name!")

    context = {
        'post': post,
        'search_term': query,
    }

    return render(request, 'searchResults.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        commenter = request.user
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True


        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "commenter": str(commenter),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been posted.')
        
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


def delete_comment(request, comment_id):
    """ To delete comments """
    commentx = get_object_or_404(Comment, pk=comment_id)
    commentx.delete()

    messages.success(request, "Your comment has been removed successfully")
    return redirect(reverse('home'))


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def tech(request):
    post = Post.objects.all()
    techpost = post.filter(category__name__contains="Tech")

    context = {
        "techpost": techpost,
    }

    return render(request, 'tech.html', context)


def world(request):
    post = Post.objects.all()
    worldpost = post.filter(category__name__contains="World")

    context = {
        "worldpost": worldpost,
    }

    return render(request, 'world.html', context)

def sport(request):
    post = Post.objects.all()
    sportpost = post.filter(category__name__contains="Sport")

    context = {
        "sportpost": sportpost,
    }

    return render(request, 'sport.html', context)


def business(request):
    post = Post.objects.all()
    businesspost = post.filter(category__name__contains="Business")

    context = {
        "businesspost": businesspost,
    }

    return render(request, 'business.html', context)


def travel(request):
    post = Post.objects.all()
    travelpost = post.filter(category__name__contains="Travel")

    context = {
        "travelpost": travelpost,
    }

    return render(request, 'travel.html', context)


def media(request):
    post = Post.objects.all()
    mediapost = post.filter(category__name__contains="Media")

    context = {
        "mediapost": mediapost,
    }

    return render(request, 'media.html', context)


def breaking(request):
    post = Post.objects.all()
    breakingpost = post.filter(category__name__contains="Breaking")

    context = {
        "breakingpost": breakingpost,
    }

    return render(request, 'breaking.html', context)
