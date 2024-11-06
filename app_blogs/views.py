from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_blogs.models import UsersModel
from app_blogs.serializers import UsersSerializer


@api_view(['GET', 'POST'])
def user_list_view(request):
    if request.method == 'GET':
        users = UsersModel.objects.all()
        serializer = UsersSerializer(users, many=True).data
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def user_detail_view(request, pk):
    user = UsersModel.objects.get(pk=pk)
    if request.method in ['PATCH', 'PUT']:
        serializer = UsersSerializer(user, data=request.data, partial=(request.method == 'PATCH'))
        serializer.is_valid()
        serializer.save()
        response = {
            "status": True,
            "message": "User updated successfully." if request.method == 'PUT' else "User created successfully.",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        response = {
            "status": True,
            "message": "User deleted successfully."
        }
        return Response(response, status=status.HTTP_200_OK)
