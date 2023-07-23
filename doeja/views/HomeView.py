from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from doeja.models import Donation, Profile

def list_donation_view(request):
    name_of_object = request.GET.get("name_of_object")
    description = request.GET.get('description')
    date_of_donation = request.GET.get('date_of_donation')
    status = request.GET.get('status')
    picture = request.GET.get('picture')
    category = request.GET.get('category')
    
    donations = Donation.objects.all().order_by('-created_at')
    
    if name_of_object is not None:
        donations = donations.filter(name_of_object__icontains=name_of_object)
    if description is not None:
        donations = donations.filter(description__id=description)
    if date_of_donation is not None:
        donations = donations.filter(date_of_donation__id=date_of_donation)
    if status is not None:
        donations = donations.filter(status__id=status)
    if picture is not None:
        donations = donations.filter(picture__id=picture)
    if category is not None:
        donations = donations.filter(category__id=category)
        
        
    context={
        'donations' : donations
    }
    
    return render(
        request, template_name='home/home.html', context=context
    )
    

def own_donation(request):
    user = Profile.objects.get(user=request.user)
    donations = Donation.objects.filter(user=user).order_by('-created_at')
    context = {
        'donations' : donations
    }
    
    return render(
        request, template_name='home/home.html', context=context
    )
    