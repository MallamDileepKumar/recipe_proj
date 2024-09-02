from django.shortcuts import render, redirect
from django.views import View
from .models import Registration, Non_veg_curries
from .forms import RegistrationForm, LoginForm
from .models import Veg_recipes, Non_veg_recipes , Veg_curries,Non_veg_curries
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
# Create your views here.


@login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            password = form.cleaned_data.get('password')
            conform_password = form.cleaned_data.get('conform_password')

            # Check if the passwords match
            if password and password == conform_password:
                # Save the form data to the database
                form.save()
                return redirect('login')  # Redirect to the login page
            else:
                form.add_error('conform_password', 'Passwords do not match')

        # Re-render the form with errors if not valid
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'login': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Registration.objects.filter(username=form.cleaned_data['username'],
                                               password=form.cleaned_data['password']).first()
            if user:
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'login.html', {'login': form})

from django.shortcuts import render, get_object_or_404

# logout view
def logout_view(request):
    logout(request)
    return redirect('login')


def view_details(request, recipe_id, recipe_type):
    if recipe_type == 'veg':
        recipe = get_object_or_404(Veg_recipes, id=recipe_id)
    elif recipe_type == 'nonveg':
        recipe = get_object_or_404(Non_veg_recipes, id=recipe_id)
    elif recipe_type == 'veg_curries':
        recipe = get_object_or_404(Veg_curries, id=recipe_id)
    elif recipe_type == 'nonveg_curries':
        recipe = get_object_or_404(Non_veg_curries, id=recipe_id)
    else:
        # Handle the case where recipe_type is invalid
        return render(request, '404.html', status=404)

    return render(request, 'view_details.html', {'recipe': recipe})

def NonVegView(request):
    recipes = Non_veg_recipes.objects.all()
    return render(request, 'NonVeg.html', {'recipes': recipes})
def VegView(request):
    recipes = Veg_recipes.objects.all()
    return render(request, 'Veg.html', {'recipes': recipes})
def NonVegCurries(request):
    recipes = Non_veg_curries.objects.all()
    return render(request, 'nonveg_curries.html', {'recipes': recipes})
def VegCurries(request):
    recipes = Veg_curries.objects.all()
    return render(request, 'veg_curries.html', {'recipes': recipes})

def search_view(request):
    query = request.GET.get('search', '')
    veg_recipes = Veg_recipes.objects.filter(title__icontains=query)
    non_veg_recipes = Non_veg_recipes.objects.filter(title__icontains=query)
    veg_curries = Veg_curries.objects.filter(title__icontains=query)
    non_veg_curries = Non_veg_curries.objects.filter(title__icontains=query)
    context = {
        'query': query,
        'veg_recipes': veg_recipes,
        'non_veg_recipes': non_veg_recipes,
        'veg_curries': veg_curries,
        'non_veg_curries': non_veg_curries,
    }
    return render(request, 'search_results.html', context)

