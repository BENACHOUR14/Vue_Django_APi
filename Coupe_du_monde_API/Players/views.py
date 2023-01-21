from rest_framework import viewsets
from Players.serializers import PlayerSerializer
from Players.models import Players
from rest_framework.response import Response
from rest_framework import permissions

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Players.objects
    serializer_class = PlayerSerializer
    # permission_classes = [permissions.IsAuthenticated]
            
    def list(self, request):
        qs = self.get_queryset()
        if request.query_params.get('name'):
            qs = qs.filter(date=request.query_params.get('name'))          
        if request.query_params.get('goals'):
            qs = qs.filter(is_finished=request.query_params.get('goals'))
        return Response(self.get_serializer(qs, many=True).data)
        
    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
