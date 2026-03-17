from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required
def update_profile(request):
    # Get or create the profile for the user
    # _ can be used to tell the program to discard a returned value
    # if I don't care if the Profile was created or retrieved then I can use a discard _
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # the files are not request.POST they are in request.FILES
        # if you exclude this your form submission will still succeed
        # but the image (profile_photo) will never be updated
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form, 'profile': profile})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

    