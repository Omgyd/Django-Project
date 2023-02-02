from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from first_app.forms import UserForm, UserProfileInfoForm


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def new_index(request):
    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict ={
    #     'access_records': webpages_list
    # }
    # my_dict = {'insert_me': "Hello uWu"}
    return render(request, 'first_app/new_index.html')


# def help(request):
#     my_context = {'my_context': "This is the context"}
#     return render(request, 'first_app/help.html', context=my_context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('new_index')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm
    return render(request, 'first_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('new_index')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password {password}")
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'first_app/login.html')


