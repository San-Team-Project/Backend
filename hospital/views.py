from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from doctor.choices import statee,state_choices
from .models import Hospital
from doctor.choices import state_choices,statee
from django.db.models import Q
from .forms import HospitalForm
# Create your views here.


def hospital(request):
    listings = Hospital.objects.order_by('-regadate') #[:3]  #.filter(is_published=True)
    lol = Hospital.objects.distinct().all()
    

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(
                Q(name__icontains=keywords) |
                Q(city__icontains=keywords)|
                Q(state__icontains=keywords)|
                Q(country__icontains=keywords)|
                Q(about__icontains=keywords)|
                Q(address__icontains=keywords))


    # City 
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            listings =listings.filter(city__iexact=city)

    # City
    if 'type' in request.GET:
        state = request.GET['type']
        if state:
            listings =listings.filter(type__iexact=state)

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

    return render(request, 'hospital/hospitallist.htm', context)

def hospital_details(request, listing_id):
  listing = get_object_or_404(Hospital, slug=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'hospital/hospital.htm', context)


def addhospital(request):
    # if request.method == 'POST':
    form = HospitalForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():

            return render(request, 'hospital/addhospital.html')

    else:
        form = HospitalForm()
    return render(request, 'hospital/addhospital.html', {'form': form})