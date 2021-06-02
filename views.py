import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm

from .forms import TopicForm, EntryForm, ClassForm
from .models import Topic, Entry, Blog
from .utils import handle_uploaded_file

from django.contrib.auth.decorators import login_required




def prv(request):
    return render(request, 'learning_logs/priv.html')


def micro1(request):
    return render(request, 'notes/m1.html')

def micro2(request):
    return render(request, 'notes/m2.html')

def micro3(request):
    return render(request, 'notes/m3.html')

def micro4(request):
    return render(request, 'notes/m4.html')

def micro5(request):
    return render(request, 'notes/m5.html')

def math40(request):
    return render(request, 'notes/math4/m01.html')


@login_required
def detail(request, slug):
    return render(request, 'webrtc/rtcweb.html', {'slug':slug})

@login_required
def web(request):

    if request.method != 'POST':
        """No data submitted; create a blank form"""
        form = ClassForm()
    else:
        """Post data submitted; process data"""
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.owner = request.user
            new_class.save()
            return HttpResponseRedirect(reverse('adhyapna', args=[new_class]))
    context = {'form': form}
    return render(request, 'webrtc/pop.html', context)

@login_required
def join(request):
    letters = string.ascii_lowercase
    result_str1 = ''.join(random.choice(letters) for i in range(3))
    result_str2 = ''.join(random.choice(letters) for i in range(4))
    result_str3 = ''.join(random.choice(letters) for i in range(3))
    result_str = result_str1 + '-' + result_str2 + '-' + result_str3
    return render(request, 'webrtc/room.html')

def index(request):
    """The Home Page For Learning log"""
    projects = Blog.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def relax(request):
    return render(request, 'inde.html')

def course_feed(request):
    if not request.user.is_authenticated:
        messages.success(request, 'login required')
        return redirect('/users/login/')
    else:
        projects = Blog.objects.all()
        context = {
            'projects': projects
        }
        return render(request, 'learning_logs/index343.html', context)

@login_required
def profile(request):
    return render(request, 'learning_logs/profile.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    """Make sure the topic belongs to the current user"""
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new Topic"""
    if request.method != 'POST':
        """No data submitted; create a blank form"""
        form = TopicForm()
    else:
        """Post data submitted; process data"""
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'learning_logs/upload.html', {'form': form})

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        """No data submiited, create a blank form"""
        form = EntryForm()
    else:
        """Post data submitted, process data"""
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id],))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        """Initial request; pre-fill form with the current entry. """
        form = EntryForm(instance=entry)
    else:
        """ POST data submitted; process data. """
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)