from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm



def home(request):
    return render(request, 'user_example/home.html')



# add authenticate and login 
from django.contrib.auth import authenticate, login

def home_view(request):    
    return render(request, "user_example/home.html")

def register(request):
    
    if request.method == 'POST':
        # pass in post data when instantiate the form.
        form = UserCreationForm(request.POST)
        # if the form is ok with the info filled:
        if form.is_valid():
            form.save()
            # that creates a new user
            # after creation of the user, want to authenticate it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # inspect the page and see the first password is password1, import authenticate
            user = authenticate(username=username, password=password)
            
            # want user to login right after registered, import login
            login(request, user)
            # want to redirect to home page, import redirect
            return redirect('home')
            
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/register.html", context)


def password_change(request):
    if request.method == 'POST':
        # We will use user change form this time
        # Import it
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/password_change.html", context)