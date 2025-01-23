from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.all_jobs, name='Jobs List'),
    path('<id>/', views.job_detail, name='detail'),
    # path("delete/<int:task_id>/", views.delete, name="delete"),
    # path("update/<int:task_id>/", views.update, name="update"),
]