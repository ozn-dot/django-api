from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Note
from .serializers import NoteSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class NoteList(APIView):
    'Lista todas las notas o crea un nuevo post'

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):    

    'Funciones para obtener o borrar notas individuales a traves de su pk (id)'

    def get_note(self, pk):
        try: 
            return Note.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        note = self.get_note(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    
    def delete(self, request, pk):
        post = self.get_note(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    