from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from commune_app.all_models.chores import Chore


def main_page(request):
    return render(request, 'commune_app/index.html')


def commune(request):
    users = get_user_model().objects.all()
    context = {'users': users}
    return render(request, 'commune_app/commune.html', context)


def chore(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        assign_to = request.POST['assign_to']
        budget = request.POST['budget']
        commune_id = request.POST['commune_id']
        new_chore = Chore.create_chore(title=title, description=description, date=date, assign_to=assign_to,
                                       budget=budget, commune_id=commune_id)
        new_chore.save()
        return redirect('commune')
    return render(request, 'commune_app/chore.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(username=username, password=password, email=email)
        user_obj.set_password(password)
        user_obj.save()
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        return redirect('main_page')
    else:
        return render(request, 'commune_app/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'commune_app/commune.html')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'commune_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('main_page')
