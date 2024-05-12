from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import User
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

class UserList(generics.ListAPIView):
    serializer = serializers.UserSerializer

    def get_queryset(self):
        name = self.request.GET.get('name')
        limit = self.request.GET.get('limit')
        if limit is not None:
            limit = int(limit)
        sort_by_param = self.request.GET.get('sort')
        page = self.request.GET.get('page')
        # if params, limit and sort_by_param is not provided, return all user list
        if name is None and limit is None and sort_by_param is None and page is None:
            return User.objects.all()
        else:
            if name is None:
                name = ""
            if sort_by_param is None:
                sort_by_param = "id"
            if page is None:
                page = 1
            queryset = User.objects.filter(Q(first_name_contains = name) | Q(last_name_contains = name)).order_by(str(sort_by_param))[:limit]
            paginator = Paginator(queryset,5)
            users = paginator.page(page)
            return users
    def perform_create(self,serializer):
        return serializer.save()
        

class UserDetail(APIView):
    def get(self,request,id = None):
       
        if id:
            item = User.objects.get(id = id)  # get one particular user data by id
            serializer = serializers.UserSerializer(item)
            return Response({"status" : "success","data" : serializer.data},status=status.HTTP_200_OK)
        
        items = User.objects.all() # get all the user data
        serializer = serializers.UserSerializer(items,many = True)
        return Response({"status" : "success","data" : serializer.data},status=status.HTTP_200_OK)
    
    # create new User
    def post(self,request):
        serializer = serializers.UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success","data" : serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status" : "error","data" : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    # modifty/update the user
    def patch(self,request,id = None):
        item = User.objects.get(id = id)
        serializer = serializers.UserSerializer(item,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success","data" : serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status" : "error","data" : serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # delete the user
    def delete(self,request,id = None):
        item = User.objects.filter(id = id)
        print(item)
        item.delete()
        return Response({"status" : "success"},status=status.HTTP_200_OK)
        