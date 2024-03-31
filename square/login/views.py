
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account. models import User
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        
        # Authenticate the user
        user = authenticate(email=email, password=password)
        print(user)
        
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            # Redirect to the homepage or any other desired page
            return redirect(reverse('home:homepage'))  # Change 'home' to the name of your homepage URL pattern
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
    return redirect(reverse('home:homepage'))

def signup_view(request):
    # Handle user signup
    if request.method == 'POST':
        # Create a new user
        if request.POST.get('password') == request.POST.get('confirm_password'):
            user = User()
            user.email = request.POST.get('email')
            user.password = make_password(request.POST.get('password'))
            user.user_type = request.POST.get('user_type')
            user.phone_no = request.POST.get('phone')
            user.name = request.POST.get('name')
            user.gender = request.POST.get('gender')

            if request.FILES.get('profile_pic'):
                pic=request.FILES.get('profile_pic')
                print(pic)
                print(request.FILES.get('profile_pic'))
                user.profile_pic.delete()
                user.profile_pic = pic

                user.username = request.POST.get('username')
                user.save()
                return redirect(reverse('login:login'))
    return render(request, 'login/signup.html')