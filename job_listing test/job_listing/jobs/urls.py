
from django.urls import path
from .views import job_list, job_detail, create_job, edit_job, delete_job, application

urlpatterns = [
    path('', job_list, name='job_list'),
    path('jobs/', job_list, name='job_list'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('create/', create_job, name='create_job'),
    path('<int:job_id>/edit/', edit_job, name='edit_job'),
    path('<int:job_id>/delete/', delete_job, name='delete_job'),
    path('jobs/<int:job_id>/apply/', application, name='application'),
]
