from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html', {})


def contacts(request):
    return render(request, 'blog/contacts.html', {})
