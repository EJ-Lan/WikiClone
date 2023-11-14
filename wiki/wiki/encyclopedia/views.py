from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util

from django import forms

class SearchWikiForm(forms.Form):
    search = forms.CharField(label="Search")


def index(request):
    if "search" not in request.session:
            request.session["search"] = None

    if request.method == "POST":
        form = SearchWikiForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data["search"]
            request.session["search"] = search

            for entry in util.list_entries():
                if search.lower() == entry.lower():
                    return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={'title': entry}))
                
            return HttpResponseRedirect(reverse("encyclopedia:results"))
        else:
            return render(request, request, "encylopedia/index.html", {
                "form": form
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

def results(request):

    return render(request, "encyclopedia/results.html", {
        "entries": util.list_entries(),
        "form": SearchWikiForm(),
        "search": request.session["search"]
    })

def create(request):
    return render(request, "encyclopedia/create.html")
