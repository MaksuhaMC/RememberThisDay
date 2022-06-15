
from django.urls import path
# from web.views import index, about
#from django.conf.urls import url
from django.contrib import admin
from web.views import RTD, home
from web.views import category
from web.views import redirect_view
# urlpatterns = [
#     path('home/', index, name='home'),
#     path('about/', about, name='about'),
#     path('admin/', admin.site.urls)
#     ]
# urlpatterns = [
# 	url(r'$^', redirect_view ),
# 	url(r'^admin/', admin.site.urls),
# 	url(r'^todo/', RTDay, name="RTDayList"),
# 	url(r'^category/', category, name="Category"),
urlpatterns = [
	path(' ', redirect_view),
	path('home/', home, name='Home'),
	path('admin/', admin.site.urls),
	path('RTDay/', RTD, name="RTDayList"),
	path('category/', category, name="Category"),
]