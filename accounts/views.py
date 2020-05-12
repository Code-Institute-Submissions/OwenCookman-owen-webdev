from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from comms.models import order, question
from payments.models import invoice

# Create your views here.


def index(request):
    """ Returns the index.html page """

    return render(request, 'index.html')


@login_required
def logout(request):
    """ Logs the user out if they are logged in """

    auth.logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect(reverse('index'))


def login(request):
    """ Returns the login.html page and allows a user to log in """

    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """ Returns the registration.html page and registers new users """

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(
                    request, "Unable to register your account at this time")

    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})


@login_required
def user_profile(request):
    """ The user's profile page where the user's orders, invoices and questions are displayed """

    user = User.objects.get(email=request.user.email)
    orders = order.objects.filter(client=request.user.id)
    invoices = invoice.objects.filter(client=request.user.id)
    questions = question.objects.filter(client=request.user.id)

    context = {'profile': user, 'orders': orders,
               'questions': questions, 'invoices': invoices}
               
    return render(request, 'profile.html', context)
