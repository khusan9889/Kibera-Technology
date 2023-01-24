# from django.shortcuts import render
from rest_framework import generics
# from .models import News
# from .serializers import NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import News
from django.forms import model_to_dict
from .serializers import NewsSerializer
from django.http import Http404
# Create your views here.

#Более детальное описание
# class NewsAPIView(APIView):
#     def get(self, request):
#         n = News.objects.all()
#         return Response({'post': NewsSerializer(n, many=True).data})

#     def post(self, request):
#         serializer = NewsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Put method is not allowed"})

#         try:
#             instance = News.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})

#         serializer = NewsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, pk):
#         instance = News.objects.get(pk=pk)
#         if not pk:
#             return Response({"error": "Delete method is not allowed"})

#         instance.delete()
#         return Response({"post":"delete post" + str(pk)})


#Get all APIs
class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

#POST method  
class NewsCreateAPIView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

#GET,PUT,DELETE methods
class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
