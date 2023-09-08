from django.shortcuts import render, redirect
from .models import Snippet
from .forms import AddSnippetForm

# Create your views here.
def home(request):
    #return render(request, 'index.html',{'nombre': 'Isaias'})
    snippets = Snippet.objects.all()
    return render(request, 'index.html',{'snippets':snippets})


# def add_snippet2(request):
#     if request.method == 'POST':
#         form = AddSnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('snippets')
#     else:
#         form = AddSnippetForm()
#     return render(request, 'add_snippet.html', {'form': form})


def add_snippet(request):
    form = AddSnippetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            add_snippet = form.save()
            return redirect('home')
    return render(request, 'add_snippet.html', {'form': form})