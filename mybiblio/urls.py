""" mybiblio URL Configuration """

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from appmain import views
from django.contrib.auth.views import (
	password_reset,
	password_reset_done,
	password_reset_confirm,
	password_reset_complete
)
	
urlpatterns = [
	url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'), 
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^books/(?P<slug>[-\w]+)/$', views.book_detail, name='book_detail'),
    url(r'^books/(?P<slug>[-\w]+)/edit/$', views.edit_book, name='edit_book'),
    url(r'^accounts/password/reset/$', password_reset, {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name="password_reset_complete"),
    url(r'^accounts/', include('registration.backends.simple.urls')), 
    url(r'^admin/', include(admin.site.urls)), 
]


	
	