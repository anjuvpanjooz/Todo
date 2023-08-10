from . import views
from django.urls import path
app_name='todoapp'
urlpatterns =  [
    path('',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('cvhome/',views.TaskListview.as_view(),name='cvhome'),
    path('cvdetail/<int:pk>/',views.TaskDetailView.as_view(), name='cvdetail'),
    path('cvupdate/<int:pk>/',views.TaskUpdateView.as_view(), name='cvupdate'),
    path('cvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvdelete'),

]