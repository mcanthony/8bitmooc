# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from mooc import views

# This kicks off the admin panel.
admin.autodiscover()

# Point URLs to their respective apps, and be smart about it.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mooc.views.home', name='home'),
    # url(r'^mooc/', include('mooc.foo.urls')),
    
    # Use a basic TemplateView to get the index page.
    # We might make it into a fancy blog feed one day (maybe import the
    # tumblr RSS as a planet-like thing).
    url(r'^$', views.view_index, name='index'),
    url(r'^privacy$', views.view_privacy, name='privacy'),
    url(r'^terms$', views.view_terms, name='terms'),

    # Apps!
    url(r'^', include('students.urls')),            # /~<user>/     # /profile/
    url(r'^', include('assembler.urls')),           # /playground/
    url(r'^chat/', include('chatroom.urls')),       # /world/
    url(r'^world/', include('world.urls')),       # /world/
    url(r'^textbook/', include('wiki.urls')),   # /textbook/
    url(r'^badges/', include('badger.urls')),       # /badges/

    # Django-admin panel
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

