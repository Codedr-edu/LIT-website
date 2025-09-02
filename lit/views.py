from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Story, News, Event, Member, ContactMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
import os


def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("check")
        else:
            return redirect("index")


def home(request):
    news = News.objects.last()  # Get the latest 3 news items
    events = Event.objects.last()  # Get the
    return render(request, 'home.html', {'news': news, 'event': events, 'user': request.user})


def story(request):
    stories = Story.objects.all().order_by('-timestamp')
    return render(request, 'story.html', {'stories': stories})


def news(request):
    news_list = News.objects.all().order_by('-created')
    if request.method == 'GET':
        search_query = request.POST.get('search', '')
        if search_query:
            news_list = news_list.filter(title__icontains=search_query)
    else:
        news_list = News.objects.all().order_by('-created')
    return render(request, 'news.html', {'news_list': news_list, 'user': request.user})


def event(request):
    events = Event.objects.all().order_by('date')
    if request.method == 'GET':
        search_query = request.POST.get('search', '')
        if search_query:
            events = events.filter(title__icontains=search_query)
    else:
        events = Event.objects.all().order_by('date')
    return render(request, 'event.html', {'events': events, 'user': request.user})


def members(request):
    members = Member.objects.all().order_by('role_order')
    if request.method == 'GET':
        search_query = request.POST.get('search', '')
        if search_query:
            members = members.filter(name__icontains=search_query)
    else:
        members = Member.objects.all().order_by('role_order')
    return render(request, 'members.html', {'members': members, 'user': request.user})


def create_news(request):
    # news_list = News.objects.all().order_by('-created')
    if request.method == 'POST' and request.user.is_authenticated:
        # Handle form submission for creating news
        title = request.POST.get('title')
        image = request.FILES.get('image')
        content = request.POST.get('content')
        if title and content:
            news = News(title=title, image=image, content=content)
            news.save()
            return redirect('news')
    # return render(request, 'news.html')


def create_event(request):
    # events = Event.objects.all().order_by('date')
    if request.method == 'POST' and request.user.is_authenticated:
        # Handle form submission for creating event
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        date = request.POST.get('date')
        if title and description and date:
            event = Event(title=title, description=description,
                          image=image, date=date)
            event.save()
            return redirect('event')
    # return render(request, 'event.html')


def create_members(request):
    # members = Member.objects.all().order_by('role_order')
    if request.method == 'POST' and request.user.is_authenticated:
        # Handle form submission for creating member
        name = request.POST.get('name')
        role = request.POST.get('role')
        bio = request.POST.get('bio')
        achievements = request.POST.get('achievements')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')
        if name and role:
            member = Member(name=name, role=role, bio=bio,
                            achievements=achievements, contact=contact, image=image)
            member.save()
            return redirect('members')
    # return render(request, 'members.html', {'members': members})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, message=message)
            return render(request, 'contact.html', {'message': 'Message sent successfully'})
    return render(request, 'contact.html')


def news_view(request, id):
    news_list = News.objects.filter(id=id).first()
    if not news_list:
        return render(request, 'news.html', {'error': 'News not found'})
    return render(request, 'news_view.html', {'news_list': news_list})


def event_view(request, id):
    events = Event.objects.filter(id=id).first()
    if not events:
        return render(request, 'event.html', {'error': 'Event not found'})
    return render(request, 'event_view.html', {'events': events})


def members_view(request, id):
    members = Member.objects.filter(id=id).first()
    if not members:
        return render(request, 'members.html', {'error': 'Member not found'})
    return render(request, 'members_view.html', {'member': members})


@csrf_exempt
def froala_image_upload(request):
    if request.method == 'POST' and 'file' in request.FILES:
        image = request.FILES['file']
        save_path = os.path.join('froala_uploads', image.name)
        file_path = default_storage.save(save_path, image)
        file_url = settings.MEDIA_URL + file_path
        return JsonResponse({'link': file_url})
    return JsonResponse({'error': 'Upload failed'}, status=400)


@csrf_exempt  # Nếu cấu hình CSRF token, nên xử lý bảo mật tốt hơn khi dùng thực tế
def tinymce_image_upload(request):
    if request.method == 'POST' and request.FILES:
        image = request.FILES['file']
        filename = default_storage.get_available_name(image.name)
        file_path = default_storage.save('tinymce_uploads/' + filename, image)
        file_url = settings.MEDIA_URL + file_path
        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Upload failed'}, status=400)
