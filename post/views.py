from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from django.views import generic
from django.views.generic import ListView
from datetime import datetime, timedelta
# Create your views here.

class MarketplaceListView(generic.ListView):
    paginate_by = 8
    template_name = 'posts.html'
    queryset = models.Marketplace.objects.all()


class MarketplaceDetailView(generic.DetailView):
    template_name = "show_detail.html"
    success_url = '/mp/'
    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Marketplace, id=show_id)



class MarketplaceCreatedateView(generic.CreateView):
    template_name = "add_post.html"
    form_class = forms.Form_for_marketplase
    queryset = models.Marketplace.objects.all()
    success_url = '/mp/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MarketplaceCreatedateView, self).form_valid(form=form)

class MarketplaceUpdateView(generic.UpdateView):
    template_name = "vacancy_update.html"
    form_class = forms.Form_for_marketplase
    success_url = '/mp/'
    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Marketplace, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)

        return super().form_valid(form)

class MarketplaceDeleteView(generic.DeleteView):
    template_name = "delete_vacancy.html"
    success_url = '/mp/'
    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Marketplace, id=show_id)
