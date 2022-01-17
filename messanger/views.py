import requests
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.db.models import Q
from .models import Profile, User, GlobalMessage, Chat


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    context = {}
    if request.method == 'post' or request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('global_chet')
        else:
            context['error_messages'] = form.errors
            return render(request, 'messanger/register.html', context)
    else:
        return render(request, 'messanger/register.html', context)


def user_login(request):
    context = {}
    if request.method == 'post' or request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('global_chet')
            else:
                context['error_message'] = 'Upps.., please try letter'
                return render(request, 'messanger/login.html', context)
        else:
            context['error_message'] = 'Username or password is invalid'
            return render(request, 'messanger/login.html', context)

    else:
        return render(request, 'messanger/login.html', context)


def index(request):
    context = {}
    profile = Profile.objects.get(user=request.user)
    if request.method == 'post' or request.method == 'POST':
        text = request.POST['text']
        GlobalMessage.objects.create(text=text,
                                     from_user_id=profile.pk)

    context['chat'] = GlobalMessage.objects.all()
    context['profile'] = profile
    context['header_chat'] = 'Global Chat'
    return render(request, 'messanger/index.html', context)


def chat_list(request):
    context = {}

    return render(request, 'messanger/chat_list.html', context)


def friend_list(request):
    context = {}
    context['profile_id'] = Profile.objects.get(user__username=request.user.username).pk
    return render(request, 'messanger/friend_list.html', context)


def settings(request):
    context = {}

    return render(request, 'messanger/settings.html', context)


def chat(request, user_id):
    context = {}
    profile = Profile.objects.get(user=request.user)
    user = Profile.objects.get(user_id=user_id)

    if request.method == 'post' or request.method == 'POST':
        text = request.POST['text']
        GlobalMessage.objects.create(text=text,
                                     from_user_id=profile.pk)

    chats = Chat.objects.all()
    if not chats:
        new_chat = Chat()
        new_chat.members.add(profile)
        new_chat.members.add(user)
        new_chat.save()
        context['chat'] = new_chat

    for chat in chats:
        if profile.pk in chat.members and user_id in chat.members:
            context['chat'] = chat
        else:
            new_chat = Chat()
            new_chat.members.add(profile)
            new_chat.members.add(user)
            new_chat.save()
            context['chat'] = new_chat

    context['profile'] = profile
    context['header_chat'] = user.get_full_name()
    return render(request, 'messanger/index.html', context)
