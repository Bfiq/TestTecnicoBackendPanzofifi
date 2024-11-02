from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

# Create your views here.
class CommentView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
      
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'message': 'Comentario creado exitosamente'
                }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = self.get_object()
        data_serializer = CommentSerializer(data, data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({
                'message': 'Comentario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': data_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):#?
        try:
            comment = self.get_object()
            comment.active = False
            comment.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comments.DoestasNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        try:
            comment = self.get_object()
            serializer = self.get_serializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        comment = self.get_object()
        serializer = self.get_serializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Comentario actualizado parcialmente con éxito',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Errores en la actualización parcial',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True) 
    def responsesToAComment(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        responses = comment.response.all()
        serializer = CommentSerializer(responses, many=True)
        return Response(serializer.data)
