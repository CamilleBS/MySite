from django.shortcuts import render,get_object_or_404
from .models import Recette
from .forms import RecetteForm
from django.utils import timezone
from django.shortcuts import redirect

def sommaire(request):
    return render(request,'diy/sommaire.html')

def recettes(request):
    recettes = Recette.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'diy/recettes.html',{'recettes':recettes})

def recette_detail(request, pk):
    recette = get_object_or_404(Recette, pk=pk) 
    return render(request,'diy/recette_detail.html', {'recette':recette})

def recette_edit(request):
    if request.method == "POST":
        form = RecetteForm(request.POST)
        if form.is_valid():
            recette = form.save(commit=False)
            recette.author = request.user
            recette.published_date = timezone.now()
            recette.save()
            return redirect('diy:recette_detail', pk=recette.pk)
    else:
        form = RecetteForm()
    return render(request, 'diy/recette_edit.html', {'form': form})