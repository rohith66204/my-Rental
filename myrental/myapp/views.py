from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import loginForm
from django.shortcuts import render, redirect
from .models import sell
from .forms import SearchForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import sell, Saved 

def home(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data['location']
            return redirect('myapp:search_results', location=location)
    else:
        form = SearchForm()

    # Map house types to their images
    house_type_images = {
        'single_family': 'single_family.jpg',
        'villa': 'villa.jpg',
        'farmhouse': 'farmhouse.jpg',
        'land': 'land.jpg',
        'apartment': 'apartment.jpg',
        'condo': 'condo.jpg',
        'townhouse': 'townhouse.jpg',
        'bungalow': 'bungalow.jpg',
        'duplex': 'duplex.jpg',
        'penthouse': 'penthouse.jpg',
        'studio': 'studio.jpg',
        'cottage': 'cottage.jpg',
        'mansion': 'mansion.jpg',
    }

    # Get counts for each house type
    house_type_counts = []
    for house_type, display_name in HOUSE_TYPE_CHOICES:
        count = sell.objects.filter(house_type=house_type).count()
        house_type_counts.append({
            'type': house_type,
            'display_name': display_name,
            'count': count,
            'image': house_type_images.get(house_type, 'default.jpg')  # Fallback image
        })

    # Sort by count in descending order and take the top 8
    house_type_counts_sorted = sorted(house_type_counts, key=lambda x: x['count'], reverse=True)[:8]

    return render(request, 'home.html', {
        'form': form,
        'house_type_counts': house_type_counts_sorted,
    })
@login_required(login_url='myapp:login')
def house_details(request, house_id):
    # Fetch the house object or return a 404 error if not found
    house = get_object_or_404(sell, id=house_id)
    return render(request, 'house_details.html', {'house': house})


def search_results(request, location):
    houses = sell.objects.filter(location__icontains=location)
    return render(request, 'search_results.html', {'houses': houses, 'location': location})


@login_required(login_url='myapp:login')  
def buy(request):
    user = request.user
    items = Saved.objects.filter(user=user)
    obj = sell.objects.all()
    return render(request, 'buy.html', {'obj': obj,'items': items})

from .forms import AgentInquiryForm
# views.py (update buyon view)

@login_required(login_url='myapp:login')
def buyon(request, id):
    obj = get_object_or_404(sell, id=id)
    usage_history = obj.usage_history.all()
    submitted = False
    
    if request.method == 'POST':
        form = AgentInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.house = obj
            inquiry.seller = obj.user  # Set the seller as the house owner
            inquiry.save()
            submitted = True
    else:
        form = AgentInquiryForm()
    
    return render(request, 'buyon.html', {
        'obj': obj,
        'usage_history': usage_history,
        'form': form,
        'submitted': submitted
    })
    # return render(request, 'buyon.html', {'obj': obj, 'form': form})

@login_required(login_url='myapp:login')
def rent(request):
    obj = sell.objects.all()
    return render(request, 'rent.html', {'obj': obj})

@login_required(login_url='myapp:login')
def rental(request, id):
    obj = sell.objects.get(id=id)
    form = RentForm()
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rent')
    return render(request, 'rental.html', {'obj': obj, 'form': form})
    
@login_required(login_url='myapp:login')
def sell_view(request):
    if request.method == 'POST':
        form = sellForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.user = request.user
            house.save()

            # Handle usage history
            users = request.POST.getlist('user')
            starting_years = request.POST.getlist('starting_year')
            ending_years = request.POST.getlist('ending_year')
            prices = request.POST.getlist('price')

            for user, starting_year, ending_year, price in zip(users, starting_years, ending_years, prices):
                if user and starting_year and ending_year and price:  # Ensure fields are not empty
                    PropertyUsage.objects.create(
                        house=house,
                        user=user,
                        starting_year=starting_year,
                        ending_year=ending_year,
                        price=price
                    )

            return redirect('myapp:buy')
    else:
        form = sellForm()

    return render(request, 'sell.html', {'form': form})


def sigin(request):
    form = SiginForm()
    if request.method == 'POST':
        form = SiginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:login')  
        else:
            print("Form Errors:", form.errors) 

    return render(request, 'sigin.html', {'form': form})

@login_required(login_url='myapp:login')
def save_item(request, id):
    user = request.user  # Current logged-in user
    house = get_object_or_404(sell, id=id)  # Get house or 404 if not found

    # Check if the house is already saved
    saved_item = Saved.objects.filter(user=user, house=house).first()

    if saved_item:
        saved_item.delete()
        messages.info(request, "House removed from saved items.")
    else:
        Saved.objects.create(user=user, house=house)
        messages.success(request, "House added to saved items.")

    return redirect('myapp:saved_items')

@login_required(login_url='myapp:login')
def saved_items(request):
    user = request.user  # Use Django's authentication system
    items = Saved.objects.filter(user=user)
    return render(request, 'saved.html', {'items': items})

def login_view(request):
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('myapp:buy')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def logoutview(request):
    logout(request)  # Properly log out user
    return redirect('myapp:login')

def debug_view(request):
    print("User authenticated:", request.user.is_authenticated)
    print("Current user:", request.user)

@login_required(login_url='myapp:login')
def my_listings(request):
    user = request.user
    houses = sell.objects.filter(user=user)  # Get houses listed by the logged-in user
    return render(request, 'my_listings.html', {'houses': houses})

@login_required(login_url='myapp:login')
def houses_by_type(request, house_type):
    houses = sell.objects.filter(house_type=house_type)
    count = houses.count()
    return render(request, 'houses_by_type.html', {'houses': houses, 'house_type': house_type, 'count': count})


@login_required(login_url='myapp:login')
def delete_house(request, house_id):
    house = get_object_or_404(sell, id=house_id)
    # Ensure the user owns the house before deletion
    if request.user == house.user:
        house.delete()
    return redirect('myapp:my_listings')



# views.py
@login_required(login_url='myapp:login')
def view_inquiries(request):
    # Get all inquiries for houses owned by the current user
    inquiries = AgentInquiry.objects.filter(seller=request.user).select_related('house')
    
    # Group by house
    inquiries_by_house = {}
    for inquiry in inquiries:
        if inquiry.house not in inquiries_by_house:
            inquiries_by_house[inquiry.house] = []
        inquiries_by_house[inquiry.house].append(inquiry)
    
    return render(request, 'agent_inquiries.html', {
        'inquiries_by_house': inquiries_by_house
    })


# @login_required(login_url='myapp:login')
# def upload_images(request, house_id):
#     house = get_object_or_404(sell, id=house_id, user=request.user)
#     images = HouseImage.objects.filter(house=house)
#     history_records = PropertyHistory.objects.filter(house=house)

#     if request.method == "POST":
#         if "upload_image" in request.POST:  # Handle image upload
#             image = request.FILES.get("image")
#             room_type = request.POST.get("room_type")

#             if image and room_type:
#                 HouseImage.objects.create(house=house, image=image, room_type=room_type)

#         elif "upload_history" in request.POST:  # Handle property history upload
#             event = request.POST.get("event")
#             date = request.POST.get("date")

#             if event and date:
#                 PropertyHistory.objects.create(house=house, event=event, date=date)

#     return render(request, "upload_images.html", {
#         "house": house,
#         "images": images,
#         "history_records": history_records
#     })


# admin
