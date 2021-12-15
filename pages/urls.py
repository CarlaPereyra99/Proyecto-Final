from django.urls import path

from .views import *

urlpatterns = [
  path( 'new_task/', CreateView.as_view(), name='new_task' ),
  path( 'edit_task/<int:pk>', UpdateView.as_view(), name='edit_task' ),
  path( 'delete_task/<int:pk>', DeleteView.as_view(), name='delete_task' ),
  path( '', HomePageView.as_view(), name='home'),
]
