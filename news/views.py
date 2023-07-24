from django.shortcuts import render
from .models import New
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import NewFilter
from .forms import NewForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
class NewsList(ListView):
    model = New
    ordering = 'datepost'
    template_name = 'index.html'
    context_object_name = 'news'
    paginate_by = 10


def get_queryset(self):
    queryset = super().get_queryset()
    self.filterset = NewFilter(self.request.GET, queryset)
    return self.filterset.qs


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filterset'] = self.filterset
    return context


class NewDetail(DetailView):
    model = New
    template = 'index.html'
    context_object_name = 'news'


class NewCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news')
    form_class = NewForm
    model = New
    template_name = 'news_edit.html'


class NewUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_news')
    form_class = NewForm
    model = New
    template_name = 'news_edit.html'


class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news')
    model = New
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


def detail(request, slug):
    news = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'name': news})





# Create your views here.
