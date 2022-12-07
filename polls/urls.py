from django.urls import path
from . import views

app_name = 'polls' # namespace of URLconf

urlpatterns = [
    path('',views.index, name = 'index_page'), # mapping a view to its URL
    # path arguments:
    # route - a string that contains a URL pattern
    # view - if it finds the specific URL it renders a given view
    # name - lets us refer to the URL from within templates

    # mathing the striped 'number/'
    path('<int:question_id>/', views.detail, name='detail'), # sending incomming questioon_id as a keyword
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]