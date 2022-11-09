from django.shortcuts import render, redirect
from . models import Post, Comment
from django.http import HttpResponse
from . forms import PostForm


def home(request):
	all_posts = Post.objects.all()

	context = {'all_posts': all_posts}
	return render(request, 'home.html', context)


def delete_post(request, pk):
	if request.method == 'DELETE':
		deleted_post = Post.objects.get(pk=pk)
		deleted_post.delete()
		return HttpResponse('<p style="color: red;"> Post deleted </p>')


def create_post(request):
	if request.method == 'POST':
		post = Post.objects.create(
			post=request.POST['new_post_field'], 
			post_author=request.user
		)

		return redirect('home')

		# return HttpResponse('<b>Published</b>')
		# post_form = PostForm(request.POST)
		# if post_form.is_valid():
		# 	post_form.save()
			# f = post_form.save(commit=False)
			# f.post_author = request.user
			# f.post = request.POST['new_post_field']
			# f.save()
		# new_post = request.POST['new_post_field']
		# new_post_author = request.user

def delete_comment(request, pk):
	if request.method == 'DELETE':
		comment = Comment.objects.get(pk=pk)
		comment.delete()

		return HttpResponse('<p style="color: red;"> Comment deleted </p>')


def create_comment(request, pk):
	if request.method == 'POST':
		post = Post.objects.get(pk=pk)
		comment = Comment.objects.create(
			comment=request.POST['new_comment_field'],
			commented_post=post,
			comment_author=request.user
		)

		return redirect('home')


def my_posts(request):

	if request.method == 'GET':
		all_posts = Post.objects.all()
		
	context = {'all_posts': all_posts}
	return render(request, 'components/my_posts.html', context)