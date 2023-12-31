from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from doeja.forms.DonationForm import DonationForm
from doeja.models import Donation, Profile
from django.core.paginator import Paginator

def list_donation_view(request):
    name_of_object = request.GET.get("name_of_object")
    description = request.GET.get('description')
    date_of_donation = request.GET.get('date_of_donation')
    status = request.GET.get('status')
    picture = request.GET.get('picture')
    category = request.GET.get('category')
    
    donations_list = Donation.objects.all().order_by('-created_at')
    
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
        

    paginator = Paginator(donations_list , 8 )
    page = request.GET.get("page")
    donations = paginator.get_page(page)
        
    context={
        'donations' : donations
    }
    
    return render(
        request, template_name='home/home.html', context=context
    )
    

def see_and_contact(request, id):
    donations = Donation.objects.filter(id=id)
    context = {
        'donations': donations
    }
    return render(
        request,
        template_name='home/contact.html',
        context=context
            
    )
    
    
@login_required
def own_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user.profile
            donation.save()
            return redirect('own_donation')
    else:
        form = DonationForm()

    user = Profile.objects.get(user=request.user)
    donations = Donation.objects.filter(user=user).order_by('-created_at')

    context = {
        'donations': donations,
        'form': form,
    }
    
    return render(request, template_name='home/own_donation.html', context=context)

@login_required
def delete_donation(request, id):
    donation = get_object_or_404(Donation, pk=id)
    donation.delete()
    return redirect('own_donation')

@login_required
def edit_donation(request, id):
    donation = get_object_or_404(Donation, pk=id)

    if request.method == "POST":
        form = DonationForm(request.POST, request.FILES, instance=donation)
        if form.is_valid():
            updated_donation = form.save(commit=False)
            updated_donation.user = request.user.profile
            updated_donation.save()
            return redirect('own_donation')
    else:
        form = DonationForm(instance=donation)

    context = {'form': form, 'donation': donation}
    return render(
        request,
        template_name='home/edit-donation.html',
        context=context
    )
        
# view to like donation
def like_donation(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    
    if request.user in donation.likes.all():
        donation.likes.remove(request.user)
    else:
        donation.likes.add(request.user)
        
        
    return redirect(
        'home'
    )