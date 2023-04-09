from django.urls import path

from . import views

app_name = 'randing'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    # path('statics/', views.statics, name='statics'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]