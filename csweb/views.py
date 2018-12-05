from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils.html import strip_tags


class IndexView(generic.TemplateView):
    template_name = 'csweb/index.html'


class SearchView(generic.TemplateView):
    template_name = 'csweb/results.html'

    # def post(self, request, *args, **kwargs):
    #     results = []
    #     search = request.POST.get('search')
    #     for flatpage in FlatPage.objects.all():
    #         counter = 0
    #         for word in flatpage.title.split():
    #             if word.lower() == search.lower():
    #                 counter += 1
    #         for word in strip_tags(flatpage.content).split():
    #             if word.lower() == search.lower():
    #                 counter += 1
    #         if counter > 0:
    #             results.append({'counter': counter, 'title': flatpage.title, 'url': flatpage.url})
    #     sort_on = "counter"
    #     decorated = [(dict_[sort_on], dict_) for dict_ in results]
    #     decorated.sort(reverse=True)
    #     results = [dict_ for (key, dict_) in decorated]
    #     context = self.get_context_data(**kwargs)
    #     context['results'] = results
    #     context['home'] = FlatPage.objects.get(url='/home/')
    #     return self.render_to_response(context=context)


class ComputerScienceDepartmentView(generic.TemplateView):
    template_name = 'computer_science/computer_science.html'


class MathDepartmentView(generic.TemplateView):
    template_name = 'math/math.html'


class EngineeringDepartmentView(generic.TemplateView):
    template_name = 'engineering/engineering.html'


class PhysicsDepartmentView(generic.TemplateView):
    template_name = 'physics/physics.html'
