from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import View
from .forms import PostForm


class PostView(View):
	def get(self,request):
		template="posts/todos.html"
		posts=Post.objects.all()
		form=PostForm()
		context={
		'posts':posts,
		'form':form
		}
		return render(request,template,context)
	def post(self, request):
		form=PostForm(request.POST)
		form.save(commit=False)
		return redirect('todos')

class PostDetailView(View):
	def get(self,request,matti):
		post=Post.objects.get(pk=matti)
		template="posts/detalle.html"
		context={
		'post':post
		}
		return render(request,template,context)




	# def post(self,request):
	# 	form=PostForm(request.POST)
	# 	form.save()
	# 	return redirect('todos')

		









# class PostView(View):
# 	def get(self,request):
# 		template="posts/todos.html"

# 		posts=Post.objects.all()
# 		context={
# 			'posts':posts
# 		}
# 		return render(request,template,context)

