from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util

from django import forms

class SearchWikiForm(forms.Form):
    search = forms.CharField(label="New Search")


def index(request):

    if request.method == "POST":
        form = SearchWikiForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data["search"]

            for entry in util.list_entries():
                if search == entry:
                    return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={'title': entry}))
        else:
            return render(request, request, "encylopedia/index.html", {
                "entries": util.list_entries(),
                "form": SearchWikiForm()
            })
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchWikiForm()
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "entry": util.get_entry(title),
        "form": SearchWikiForm()
    })

def results(request, title):
    return render(request, "encyclopedia/results.html", {
        "entries": util.list_entries(),
        "form": SearchWikiForm()
    })

