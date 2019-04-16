from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница блога'
        return context


class DetailNewsView(DetailView):
    model = News
    template_name = 'blog/detail_news.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailNewsView, self).get_context_data(**kwargs)
        context['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return context


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/news_form.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/news_form.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete_news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


def contacts(request):
    return render(request, 'blog/contacts.html', {})
