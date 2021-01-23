from django import forms
from .models import BlogPost
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=SummernoteWidget())
	# content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'image' ,'slug','content', 'publish_date']
		widgets  = { 'content': SummernoteWidget(), }

	def clean_title(self,*args,**kwargs):
		instance = self.instance
		print(instance)
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexact = title)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError("This title has already been used. Please try Again!!!")
		return title