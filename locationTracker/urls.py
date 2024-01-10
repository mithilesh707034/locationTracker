
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-member/',views.add_member),
    path('get-member/',views.get_member),
    path('update-member/',views.update_member),
    path('get-all-member/',views.get_all_member),
]
