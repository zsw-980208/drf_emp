from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from api.models import User, Employee
from api.serializers import UserModelSerializer,EmployeeModelSerializer
from utils.response import APIResponse


class UserAPIView(APIView):

    def post(self,request,*args,**kwargs):
        request_data=request.data
        print(request_data)
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj=serializer.save()

        return APIResponse(200,True,results=UserModelSerializer(user_obj).data)


    def get(self,request,*args,**kwargs):
        username=request.query_params.get("username")
        password=request.query_params.get("password")
        print(username,password)
        user=User.objects.filter(username=username,password=password).first()
        print(user)
        if user:
            data=UserModelSerializer(user).data
            return APIResponse(200,True,results=data)
        return APIResponse(400,False)


class EmployeeView(ListModelMixin,
                   GenericAPIView,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        emp_id=kwargs.get("id")
        print(emp_id)
        user_list=[]
        if emp_id:
            user_list=self.retrieve(request,*args,**kwargs)
        else:
            user_list=self.list(request,*args,**kwargs)
        return APIResponse(200,True,results=user_list.data)

    def patch(self, request, *args, **kwargs):
        print(1111)
        print(request.data)
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def post(self,request,*args,**kwargs):
        user_obj=self.create(request,*args,**kwargs)
        return APIResponse(200,True,results=user_obj.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(http_status=status.HTTP_204_NO_CONTENT)


class RegisterView(ViewSet):

    def check_user(self,request,*args,**kwargs):
       return APIResponse("ok")
