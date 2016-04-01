from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from personal.forms import UserForm, UserProfileForm
from personal.tasks import add
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    add.delay(4,4)
    return render(request, 'personal/contact.html', {'contents':['please contact me','yangx59@mcmaster.ca']})

def handle_file(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open("/Users/Derrick/Documents/pythontest/django_tutorial/mysite/media/" + "file_" + str(count), "wb+") as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("uploaded!")

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'personal/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'personal/login.html')
# Create your views here.


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')