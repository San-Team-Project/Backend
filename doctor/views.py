
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from doctor.choices import statee,state_choices
from .models import Doctor,DoctorType
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import DoctorForm,Doctor
from django.http import HttpResponseRedirect
from django.contrib import messages, auth


def index(request):
    listings = Doctor.objects.order_by('-regadate')[:3]  #.filter(is_published=True)

    context = {
        'listings': listings,
        'statee': statee ,
        'state_choices': state_choices,
        'values': request.GET
        
    }
    return render(request, 'pages/index.html', context)

def about(request):
    about = DoctorType.objects.all()
    listen = Doctor.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            about = about.filter( name__icontains=keywords)

     # State
    if 'special' in request.GET:
        state = request.GET['special']
        if state:
            listen =listen.filter(specialization__iexact=state)

    context = {
        'about': about,
        'listen':listen,
        'statee': statee ,
        'values': request.GET
       
    }

    return render(request, 'pages/about.html', context)



def doctor(request):
    listings = Doctor.objects.order_by('-regadate') #[:3]  #.filter(is_published=True)
    
    lol = Doctor.objects.distinct().all()


    # Q(first_name__startswith='R') | Q(last_name__startswith='D')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(
                Q(name__icontains=keywords) |
                Q(specialization__icontains=keywords) | 
                Q(city__icontains=keywords)|
                Q(state__icontains=keywords)|
                Q(country__icontains=keywords)|
                Q(address__icontains=keywords)|
                Q(hospital__icontains=keywords))


    # City 
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            listings =listings.filter(city__iexact=city)

    # State
    if 'special' in request.GET:
        state = request.GET['special']
        if state:
            listings =listings.filter(specialization__iexact=state)

    # State
    if 'state' in request.GET:
        bedrooms = request.GET['state']
        if bedrooms:
            listings = listings.filter(state__iexact=bedrooms)

    # Country
    if 'country' in request.GET:
        bedrooms = request.GET['country']
        if bedrooms:
            listings = listings.filter(country__iexact=bedrooms)
    

    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    context = {
        'users': users,
        'statee': statee ,
        'state_choices': state_choices,
        'lol': lol,
        'values': request.GET
        
    }

    return render(request, 'doctor/doctorlist.html', context)

def doctor_detail(request, listing_id):
  listing = get_object_or_404(Doctor, slug=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'doctor/details.htm', context)


def geo(request):
  return render(request, 'doctor/GeoMap.html')

# def adddoctor(request):
#     if request.method == 'POST':
#         form = DoctorForm(request.POST)
#         if form.is_valid():
#             return render(request, 'doctor/adddoctor.html')
#     else:
#         form = DoctorForm()
#     return render(request, 'doctor/adddoctor.html', {'form': form})


def adddoctor(request):
    # if request.method == 'POST':
    form = DoctorForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():

            return render(request, 'doctor/doctorlist.html')

    else:
        form = DoctorForm()

    return render(request, 'doctor/adddoctor.html', {'form': form})