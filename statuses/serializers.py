from rest_framework import serializers

from statuses.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'uuid',
            'status_name')
        extra_kwargs = {
            'uuid': {'validators': []},
        }