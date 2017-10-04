from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.flatpages.models import FlatPage


class IndexView(generic.TemplateView):
	template_name = 'csweb/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context.update({
			'home': FlatPage.objects.get(url='/home/'),
			'academics': FlatPage.objects.get(url='/academics/'),
			'faculty': FlatPage.objects.get(url='/faculty/'),
			'gallery': FlatPage.objects.get(url='/gallery/'),
			'news': FlatPage.objects.get(url='/news/'),
			'contact': FlatPage.objects.get(url='/contact/'),
		})
		return context
