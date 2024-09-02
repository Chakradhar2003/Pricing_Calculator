"""option_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cal.views import two_step
from cal.views import n_step
from cal.views import black_scholes
from cal.views import home_view
from cal.views import about
from django.http import HttpResponseRedirect
from django.urls import path, re_path
from django.http import HttpResponseRedirect
from django.contrib import admin
from cal.views import two_step, n_step, black_scholes, home_view, about


def redirect_to_last_segment(request, segment):
    if segment == 'home':
        return home_view(request)
    elif segment == 'two-steps':
        return two_step(request)
    elif segment == 'n-steps':
        return n_step(request)
    elif segment == 'black-scholes':
        return black_scholes(request)
    elif segment == 'about':
        return about(request)
    else:
        return HttpResponseRedirect('/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('', home_view),
    path('two-steps/', two_step),
    path('n-steps/', n_step),
    path('black-scholes/', black_scholes),
    path('about/', about),
    re_path(r'.*/(?P<segment>[^/]+)/$', redirect_to_last_segment),  # Dynamic URL handler
]