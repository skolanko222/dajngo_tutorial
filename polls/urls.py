from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index_page') # mapping a view to its URL
    # path arguments:
    # route - a string that contains a URL pattern
    # view - if it finds the specific URL it renders a given view
    # name - lets us refer to the URL from within templates
]