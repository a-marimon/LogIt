import datetime
from pyexpat.errors import messages

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from job.models import Job
from job.serializers import JobSerializer





@api_view()
def all_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view()
def job_detail(request, id):
    task = get_object_or_404(Job, pk=id)
    serializer = JobSerializer(task)
    print(task.id)
    return Response(serializer.data)
