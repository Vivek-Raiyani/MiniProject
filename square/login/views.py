from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(email=email, password=password)
        
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            # Redirect to the homepage or any other desired page
            return render(request, 'home/homepage.html')  # Change 'home' to the name of your homepage URL pattern
        else:
            # Authentication failed, display an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login/login.html', {'error_message': error_message})
    else:
        # Display the login form for GET requests
        return render(request, 'login/login.html')
    
def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect to the homepage or any other desired page
    return redirect('home/homepage')
