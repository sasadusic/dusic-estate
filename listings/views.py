from django.shortcuts import render, redirect,get_object_or_404
from .models import Listing
from .forms import ListingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

# User Manipulation
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Wellcome {username.title()}, you are logged in')
            return redirect('index')
        else:
            messages.success(request, f'Wrong username or password please try again')
            return redirect('index')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    messages.success(request, f'You are logged out, Login to continue')
    logout(request)
    
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Wellcome {username.title()}, you are registered')
            return redirect('index')

    else:
        form = SignUpForm()

        return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', {'form': form})

@login_required(login_url="login")
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url="login")
def  update_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = UpdateProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated successfully!")
            return redirect("profile")
        else:
            messages.error(request,"Please correct the error below.")
    else:
        form = UpdateProfileForm(instance=current_user)
    
    context={"form":form}
    return render(request,'update_profile.html',context)    

@login_required(login_url="login")
def change_password(request):
    current_user = request.user
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=current_user, data=request.POST)
        if form.is_valid():
            form.save()
            # Logout the user first to get rid of session cookie
            logout(request)
            messages.warning(request, "Password changed successfully! Please login again.")
            return redirect('logout')
        else:
            messages.error(request, "Error in password reset. Please try again.")
            
    else:
        form = CustomPasswordChangeForm(user=current_user)
        
    return render(request, 'change_password.html', {'form': form})

User = get_user_model()

@login_required(login_url="login")
def delete_profile(request):
    """
    View function for deleting a user's profile.
    Only accessible to authenticated users.
    """
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        user.delete()
        return redirect("index")
# User Manipulation

def list(request):
    listings = Listing.objects.all()
    return render(request, 'list.html', {'listings': listings})

def retrieve(request, id):
    listing = Listing.objects.get(pk=id)
    return render(request, 'retrieve.html', {'listing': listing})

def create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'create.html', {
                'form': form,
                'message': 'Listing created successfully!'
                })
        return render(request, 'create.html', {
            'form': form,
            'error': 'Error creating listing!'
            })
    form = ListingForm()
    return render(request, 'create.html', {'form': form})

def update_list(request, id):
    listing = Listing.objects.get(pk=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'update.html', {
                'form': form,
                'message': 'Listing updated successfully!'
                })
        return render(request, 'update.html', {
            'form': form,
            'error': 'Error creating listing!'
            })
    form = ListingForm(instance=listing)
    return render(request, 'update.html', {'form': form})

def delete_list(request, id):
    listing = Listing.objects.get(pk=id)
    listing.delete()
    return redirect('list')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login_user')
def korpa(request):
    return  render(request, 'korpa.html')