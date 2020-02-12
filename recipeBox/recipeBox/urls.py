"""recipeBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from recipeBox import views
from recipeBox.models import Author, Recipe

#-- admin.site.register tells the specific stand-alone website
    # that we have some new things to hook into it.
    # This adds Author and NewsItem to the admin site.
    # Now, if you want a new author, click add and you have name attribute.
admin.site.register(Author)
admin.site.register(Recipe)
#--url patters is a path (item built in django), this is a path to send 'somewhere'
    # comes with an admin application mini site.
    # 1. tell django where to route by importing views (ie. news_view).
    # Remember to run: $python manage.py runserver to see the html render in localhost: 8000
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_list, name='home'),
    path('recipes/<int:id>', views.recipe_content, name='recipe_content'),
    path('authors/<int:id>', views.author_view, name='author_view'),
    path('add_recipe', views.add_recipe_view, name='add_recipe_view'),
    path('add_author', views.add_author_view, name='add_author_view'),
    path('sign_up', views.login_view)




   # path('<int:pk>/author', author_detail_view) #localhost/1/author

]

#-- when you go to /admin, this is everything 'backend' for django
# for models or hooking into the db
# migrations is the django term for anything that makes up a database.
# every piece of modle added, etc.  We run the migrations to get base template stuff
    # to get migrations ran, use $ python manage.py migrate.
    # it looks at models folder, then takes all the default stuff and makes raw sql and
    # commits it to db.
#!! MUST CREATE SUPER USER TO ACCESS /ADMIN SITE:
    # 1. $python manage.py createsuperuser
    # 2. input username, password, and email address

