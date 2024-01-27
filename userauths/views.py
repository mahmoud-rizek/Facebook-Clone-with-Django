from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.


def register_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered!')
        return render("core:home")
    
    form = UserRegisterForm(request.POST or None)
    if form.is_valid:
        form.save()
        
        full_name= form.cleaned_data.get('full_name')
        email= form.cleaned_data.get('email')
        phone= form.cleaned_data.get('full_name')
        gender= form.cleaned_data.get('full_name')
        password = form.cleaned_data.get('full_name')
        password = form.cleaned_data.get('full_name')
        
        user = ''