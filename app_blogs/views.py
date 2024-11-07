from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_blogs.models import UsersModel, BlogsModel
from app_blogs.serializers import UsersSerializer, BlogSerializer


@api_view(['GET', 'POST'])
def user_list_view(request):
    if request.method == 'GET':
        users = UsersModel.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def user_detail_view(request, pk):
    user = get_object_or_404(UsersModel, pk=pk)
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method in ['PATCH', 'PUT']:
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
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def blog_list_create(request):
    if request.method == 'GET':
        blogs = BlogsModel.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def blog_detail_update_delete(request, pk):
    blog = get_object_or_404(BlogsModel, pk=pk)
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method in ['PATCH', 'PUT']:
        serializer = BlogSerializer(blog, data=request.data, partial=(request.method == 'PATCH'))
        serializer.is_valid()
        serializer.save()
        response = {
            "status": True,
            "message": "Blog updated successfully." if request.method == 'PUT' else "Blog created successfully.",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        blog.delete()
        response = {
            "status": True,
            "message": "Blog deleted successfully."
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
