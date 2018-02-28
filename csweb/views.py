from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.flatpages.models import FlatPage
from django.utils.html import strip_tags


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


class SearchView(generic.TemplateView):
    template_name = 'csweb/results.html'

    def post(self, request, *args, **kwargs):
        results = []
        search = request.POST.get('search')
        for flatpage in FlatPage.objects.all():
            counter = 0
            for word in flatpage.title.split():
                if word.lower() == search.lower():
                    counter += 1
            for word in strip_tags(flatpage.content).split():
                if word.lower() == search.lower():
                    counter += 1
            results.append({flatpage.title: counter})
        context = self.get_context_data(**kwargs)
        context['results'] = results
        context['home'] = FlatPage.objects.get(url='/home/')
        return self.render_to_response(context=context)
