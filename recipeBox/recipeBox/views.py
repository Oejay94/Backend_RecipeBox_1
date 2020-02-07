from django.shortcuts import render, reverse
#response sends whatever text you give it as a regular http response w/ 200
#redirect sends a 302 w/ link to diff page
from django.http import HttpResponse, HttpResponseRedirect
from recipeBox.models import Recipe, Author

from recipeBox.forms import Add_Recipe, Add_Author
# --can write function based view or classed based view.  But class based lets us do more w/ request.
# -- Pass it around alot, etc.  Using a function based view here bc its easier

# -- all functions inside django take a request object(implicit by default).
# -- takes in method, etc. So first: make it return 'something'
def recipe_list(request):
    # 1. !!run this code to get somethign to render to the page
        # html = """oh I guess this actually worked """
        # return HttpResponse(html)
    # 2. Now get it to render a newly created .html file in
        # folder 'HTML' in the basedir.  Use:
        # return render(request, 'news_view.html')
    # 3.  Once both work, use below to pass data from DB into news_view to render to page.
    results = Recipe.objects.all()
    # results1 = NewsItem.objects.filter(author__id=2)
    return render(request, 'recipe_list.html', {'data': results})

def recipe_content(request, id):
    recipe = Recipe.objects.get(pk=id)
    return render(request, 'recipe_content.html', {'recipe': recipe})

def author_view(request, id):
    author = Author.objects.get(pk=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {'author': author, 'recipes': recipes})

# forms view
def add_recipe_view(request):
    if request.method == 'POST':
        form = Add_Recipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                time = data['time'],
                description = data['description'],
                instructions = data['instructions']
            )
            return HttpResponseRedirect(reverse('home'))
    form = Add_Recipe()
    return render(request, 'add_recipe.html', {'form': form})


def add_author_view(request):
    if request.method == 'POST':
        form = Add_Author(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name = data['name'],
                bio = data['bio']
            )
            return HttpResponseRedirect(reverse('home'))
    form = Add_Author()
    return render(request, 'add_author.html', {'form': form})
