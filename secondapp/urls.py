from django.urls import path
from . import views
urlpatterns=[
    path("",views.exam1,name='exam1'),
    path('exam2/', views.exam2),
    path('exam3/', views.exam3),
    path('exam4/', views.exam4),
    path('exam5/', views.exam5),
    path('exam6/', views.exam6),
]