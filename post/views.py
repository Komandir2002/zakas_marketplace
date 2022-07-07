from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from django.views import generic
from django.views.generic import ListView
from datetime import datetime, timedelta
# Create your views here.

class VacancyListView(generic.ListView):
    paginate_by = 8
    template_name = 'posts.html'
    queryset = models.Post.objects.all()


class VacancyDetailView(generic.DetailView):
    template_name = "show_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Post, id=show_id)



class VacancyCreatedateView(generic.CreateView):
    template_name = "add_post.html"
    form_class = forms.Form_for_bookshow
    queryset = models.Post.objects.all()
    success_url = "/posts/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(VacancyCreatedateView, self).form_valid(form=form)

class VacancyUpdateView(generic.UpdateView):
    template_name = "vacancy_update.html"
    form_class = forms.Form_for_bookshow
    success_url = "/posts/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Post, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)

class VacancyDeleteView(generic.DeleteView):
    success_url = "/posts/"
    template_name = "delete_vacancy.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Post, id=show_id)
