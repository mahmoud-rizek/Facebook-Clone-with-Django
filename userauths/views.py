from django.shortcuts import render ,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

from .models import Profile

# Create your views here.


def register_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered!')
        return redirect("core:home")
    
    form = UserRegisterForm(request.POST or None)
    if form.is_valid:
        
        

        
        full_name= form.cleaned_data.get('full_name')
        email= form.cleaned_data.get('email')
        phone= form.cleaned_data.get('phone')
        # gender= form.cleaned_data.get('gender')
        password = form.cleaned_data.get('password1')
        user = authenticate( email=email, password= password)
        login( request,user)
        # return redirect(f"/accounts/{username}/activate")

        profile = Profile.objects.get(user= request.user)
        profile.full_name=full_name
        profile.phone=phone
        # profile.gender=gender
        
        profile.save()
        messages.success(request,f"Wellcome, {full_name}, your account has been created successfuly!")
        return redirect("core:home")
    
    
    
    context={"registerForm":form}
    return render(request, 'register.html', context)
 
# def sign_up(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         print("Error is at here, after SignupForm !!!!!!!!!")
#         if form.is_valid():
#             print("Error is at here, after is_valid !!!!!!!!!")
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             myform = form.save()
#             profile = Profile.objects.get(user__username=username)  
#             profile.active = False
#             profile.save()
            

#             # send email
#             send_mail(
#                 subject= 'Greeny Activate Your Account',
#                 message=f"user this code {profile.code} to activate your acount", 
#                 from_email='mahmoudtino56@gmail.com', 
#                 recipient_list= [email],
#                 fail_silently=False
#             )
#             return redirect(f"/accounts/{username}/activate")

#     else:
#         form = SignupForm()
#         print("Error is at here, after else condition !!!!!!!!!")
#     return render(request, 'registration/signup.html', {"form":form} )

