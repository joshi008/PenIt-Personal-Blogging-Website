from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# Create your views here.
from .forms import *
from .models import *


# GET => 1 object
# filter => list of objects

# def blog_post_detail_page(request,slug):
# 	# queryset = BlogPost.objects.filter(slug=slug)
# 	# if queryset.count() ==0:
# 	# 	raise Http404
# 	# obj = queryset.first()
# 	obj = get_object_or_404(BlogPost, slug=slug)
# 	template_name = 'blog_post_detail.html'
# 	context = {"object" : obj,"title": "BLOG"}
# 	return render(request, template_name, context)





	# try:
	# 	obj = BlogPost.objects.get(id=post_id)
	# except BlogPost.DoesNotExist:
	# 	raise Http404
	# except ValueError:
	# 	raise Http404



# CRUD

# GET -> Retrieve / List

# POST -> Create / Update / DELETE

# Create Retrieve Update and Delete (CRUD)


def blog_post_list_view(request):
	# list out objects
	# could bee searched => objects.filter(title_icontains='hello')
	# now = timezone.now()
	qs = BlogPost.objects.all().published()   # queryset -> list of python objects
	# qs = BlogPost.objects.filter(publish_date__lte=now)
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct()
	template_name = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template_name,context)



# @login_required
@staff_member_required
def blog_post_create_view(request):
	# create objects
	# use a form
	# request.user => return something
	# if not request.user.is_authenticated:
	# 	return render(request,"not-a-user.html",{})
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		# print(form.cleaned_data)
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		# obj = BlogPost.objects.create(**form.cleaned_data)
		form = BlogPostModelForm()
	template_name = 'form.html'
	context = {'form': form, 'title':"Create Blog"}
	return render(request, template_name, context)

def blog_post_detail_view(request, slug):
	# 1 object => detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/detail.html'
	context = {"object" : obj,"title": "BLOG"}
	return render(request, template_name,context)


@staff_member_required
def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=obj)
	template_name = 'form.html'
	context = {"form": form, "title": f"Update {obj.title}" }
	if form.is_valid():
		obj.save()
	return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	context = {"object" : obj,"title": "BLOG"}
	return render(request, template_name,context)