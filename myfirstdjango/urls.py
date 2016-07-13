from django.conf.urls import *
from myfirstdjango.views import hello
from myfirstdjango.views import current_time,hours_ahead
from myfirstdjango.views import current_time2
from django.contrib import admin
admin.autodiscover()
from books import  views


urlpatterns = [
    url(r'^hello/$',hello),
    url(r'^nowtime/$',current_time),
    url(r'^anothertime/$',current_time),
    url(r'^time/plus/(\d{1,3})/$',hours_ahead),
    url(r'^current_time2/$',current_time2),
    url(r'^admin/',include(admin.site.urls)),
#    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search)

]

