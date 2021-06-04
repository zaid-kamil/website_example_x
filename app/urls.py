from django.urls import path
from .views import index, about,view_hr,detail_hr

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    # step 2
    path('hr/view',view_hr, name='view_hr'),
    # step x
    path('hr/detail/<int:pk>',detail_hr, name='detail_hr'),
]