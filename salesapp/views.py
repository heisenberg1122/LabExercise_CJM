from django.shortcuts import render

# Create your views here.

def homepage_view(request):
    """View for the homepage."""
    # Use the name of your HTML file
    return render(request, 'HomePage.html') 

def login_view(request):
    """View for the login page."""
    # Use the name of your HTML file
    return render(request, 'LoginPage.html')

def about_view(request):
    """View for the About Us page."""
    # Use the name of your HTML file
    return render(request, 'AboutusPage.html')

def contact_view(request):
    """View for the Contact Us page."""
    # Use the name of your HTML file
    return render(request, 'ContactusPage.html')