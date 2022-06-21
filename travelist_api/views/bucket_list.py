from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from travelist_api.models.bucket_list import BucketList


class BucketListView(ViewSet):
    """Travelist traveled list view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single traveled locations

        Returns:
            Response -- JSON serialized category
        """
        try: 
            bucketList = BucketList.objects.get(pk=pk)
            serializer = BucketListSerializer(bucketList)
            return Response(serializer.data)
        except BucketList.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all traveled list

        Returns:
            Response -- JSON serialized list of traveled locations
        """
        bucketLists = BucketList.objects.all()
        serializer = BucketListSerializer(bucketLists, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        serializer = CreateBucketListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BucketListSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = BucketList
        fields = ('id', 'location')

class CreateBucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = ['id', 'location']