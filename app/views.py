from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from app.models import Recipe
from .forms import RecipeForm
from django.shortcuts import redirect
# Create your views here.


def recipe_list(request):
    recipes = Recipe.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'app/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'app/recipe_detail.html', {'recipe': recipe})


def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'app/recipe_edit.html', {'form': form})
