from django.conf.urls import include, url
from django.contrib import admin
from views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^accounts/login', login, name='login'),
    url(r'^validate/', validate),
    url(r'^accounts/logout', logout , name='logout'),
    url(r'get_status/(?P<status>\w+)/$', status),
    url(r'load_get/(?P<load>\d+)/$', get_load),
    url(r'add_load/',add_load),
    url(r'add_driver/',add_driver),
    url(r'add_contacts/',add_contacts),
    url(r'all/',all_records),
    url(r'update_status/(?P<id>\d+)/$', update_status),
    url(r'accounts/invalid',invalid),
    url(r'reports/', reports),
    url(r'edit_contact/(?P<cid>\d+)/$', edit_contact),
    url(r'contacts/(?P<cid>\d+)/$', contacts),
    url(r'add_trailer/(?P<cid>\d+)/$', add_trailer),
    url(r'add_truck/(?P<cid>\d+)/$', add_truck),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()