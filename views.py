from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm


def home_page(request):
    my_title = 'Home Page'
    context = {'title': 'my_title'}
    if request.user.is_authenticated:
        context = {'title': my_title, 'my_list': [1, 2, 3, 4, 5, ]}
    return render(request, 'home.html', context)


def about_page(request):
    my_title = 'About Page'
    return render(request, 'about.html', {'title': my_title})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        'title': "Contact Us",
        "form": form
    }
    return render(request, 'form.html', context)


def example_page(request):
    context = {"title": "example"}
    template_name = 'about.html'
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
