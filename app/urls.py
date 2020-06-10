from django.urls import path ,include
from . import views
urlpatterns = [
     path('register/',views.home_page,name='homepage'),
     path('save_data/',views.save_data,name='saving'),
     path('',views.show_data,name='showdata'),
      path('delete/<int:id>',views.delete,name='deleting'),
       path('update/<int:id>',views.update,name='updating'),
]
