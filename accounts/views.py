from django.shortcuts import render, redirect
from django.conf import settings
from .forms import MyRegistrationForm, AddedSignupForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        base_form = MyRegistrationForm(request.POST)
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        added_form = AddedSignupForm(request.POST, instance=profile, )

        if all((base_form.is_valid(), added_form.is_valid())):
            base = base_form.save()
            added = added_form.save()

            return redirect(settings.LOGIN_URL)

    else:
        base_form = MyRegistrationForm()
        added_form = AddedSignupForm()

    return render(request, 'accounts/signup_form.html', {
        'base_form' : base_form,
        'added_form' : added_form,
    })