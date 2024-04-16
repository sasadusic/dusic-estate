from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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