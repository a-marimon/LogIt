from rest_framework import serializers
from job.models import Job, JobType


class JobTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobType
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=100)
    type = JobTypeSerializer()

    class Meta:
        model = Job
        fields = '__all__'
