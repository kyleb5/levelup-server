"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event


class EventView(ViewSet):
    """Level up event view"""

    def retrieve(self, request, pk):
        """Handle GET requests for event type
        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of game types
            """
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')
