from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from job.models import Job
from job.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Job.objects.all()
        return self.queryset.filter(user=self.request.user)
