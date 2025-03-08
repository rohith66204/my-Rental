from django.urls import path
from .views import *
from . import views
from .views import home,search_results, buyon
from .views import houses_by_type
from .views import house_details 
app_name = 'myapp'

urlpatterns = [
    path('',home, name='home'),
    path('search/<str:location>/', search_results, name='search_results'),
    path('buy/', buy, name='buy'),
    path('buy/<int:id>/', buyon, name='buyon'),
    path('rent/', rent, name='rent'),
    path('rental/<int:id>/', rental, name='rental'),
    path('sell/', sell_view, name='sell'),
    path('sigin/', sigin, name='sigin'),
    path('save_item/<int:id>/', save_item, name='save_item'),
    path('saved_items/', saved_items, name='saved_items'),
    path('login/', login_view, name='login'),
    path('logout/', logoutview, name='logout'),
    path('my_listings/', my_listings, name='my_listings'),
    path('houses/<str:house_type>/', houses_by_type, name='houses_by_type'),
    path('house/<int:house_id>/', house_details, name='house_details'),
    path('delete_house/<int:house_id>/', views.delete_house, name='delete_house'),
    # path('upload_images/<int:house_id>/', upload_images, name='upload_images'),
    path('view-inquiries/', views.view_inquiries, name='view_inquiries'),
    # admin
    
    

    
]

