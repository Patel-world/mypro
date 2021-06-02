"""Defines url pattern for learning_logs"""

from django.urls import path

from . import views

urlpatterns = [
    path('Privacy_Policy', views.prv, name='prv'),
    path('assign/', views.upload_file, name='assign'),
    path('microprocessor', views.micro1, name='micro1'),
    path('microprocessor-unit-1', views.micro1, name='micro1'),
    path('microprocessor-unit-2', views.micro2, name='micro2'),
    path('microprocessor-unit-3', views.micro3, name='micro3'),
    path('microprocessor-unit-4', views.micro4, name='micro4'),
    path('microprocessor-unit-5', views.micro5, name='micro5'),
    path('math4/unit3', views.math40, name='math40'),
    path('class/<slug:slug>/', views.detail, name="adhyapna"),
    path('join', views.join, name='join'),

    path('relax_mode', views.relax, name='relax'),
    #Home Page

    path('', views.index, name='index'),
    path('course_feed', views.course_feed, name='index343'),
    path('profile', views.profile, name='profile'),

    # Show all Topics
    path('topics', views.topics, name='topics'),

    #Detail page for single topic
    path('topics/<topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing a entry
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]