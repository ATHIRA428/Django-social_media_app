from django.shortcuts import render,redirect
from . forms import AddPost,Profile,AddCommentForm
from model_setup . models import Post,Profile,Comment,Like
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForms
# Create your views here.



def addpost(request):
    form = AddPost()
    if request.method == 'POST':
        form = AddPost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    
    context = {
        'form': form
    }
    
    return render(request, 'addpost.html', context)



def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPost(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'update_post.html', context)    

def posts(request):
    posts = Post.objects.all()
    for post in posts:
        return render(request, 'post.html', {'post': posts})



def profile(request):
    profiles=Profile.objects.all()
    context={
        'profiles':profiles
    }
    return render(request,'profile.html',context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('/')

    context = {
        'post': post,
    }

    return render(request, 'delete_post.html', context)



def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = AddCommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    
    return render(request, 'post_detail.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = AddCommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    
    return render(request, 'post_detail.html', context)


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    try:
        like = Like.objects.get(user=user, post=post)
        post.count -= 1
        like.delete()
    except Like.DoesNotExist:
        like = Like(user=user, post=post)
        like.save()
        post.count += 1
    post.save()
    return redirect('post')




@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForms(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForms(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})











