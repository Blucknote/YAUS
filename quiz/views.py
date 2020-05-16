from django.contrib.auth import (
    authenticate, login as built_in_login, logout as built_in_logout,
    get_user_model)
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'index.html', {})


@require_POST
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        built_in_login(request, user)
        return redirect(reverse('index'))
    else:
        return JsonResponse(
            {'message': 'invalid username or password'}
        )


@require_POST
def register(request):
    username = request.POST.get('usernamereg')
    password = request.POST.get('passwordreg')
    password1 = request.POST.get('password1')

    if not any(
        [username, password, password1]
    ):
        return JsonResponse(
            {'message': 'Form incorrect'}
        )

    if not password or not password1:
        return JsonResponse(
            {'message': 'Empty password'}
        )

    if password != password1:
        return JsonResponse(
            {'message': 'passwords did not match'}
        )
    user_model = get_user_model()

    if user_model.objects.filter(username=username).first():
        return JsonResponse(
            {'message': 'User exists'}
        )

    user = user_model.objects.create(
        username=username,
        password=password
    )

    user.save()

    authenticate(request, username=username, password=password)
    built_in_login(request, user)
    return redirect(reverse('index'))


def logout(request):
    built_in_logout(request)
    return redirect(reverse('index'))
