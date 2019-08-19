from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import course, rating
from django.contrib.auth.models import User
from .serializers import courseSerializer,ratingSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    print (serializer_class)


class courseViewSet(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = courseSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['POST'])
    def rate_course(self, request, pk=None):
        if 'stars' in request.data:

            Course = course.objects.get(id=pk)
            print('Course Title',Course.title)
            stars = request.data['stars']
            user = request.user
            try:
                Rating = rating.objects.get(user=user.id,Course=Course.id)
                Rating.stars = stars
                Rating.save()
                serializer = ratingSerializer(Rating, many=False)
                response = {'message': 'ratings updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                Rating = rating.objects.create(user=user, Course=Course, stars=stars)
                serializer = ratingSerializer(Rating, many=False)
                response = {'message': 'ratings created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else :
           response = {'message': 'provide stars'}
           return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ratingViewSet(viewsets.ModelViewSet):
    queryset = rating.objects.all()
    serializer_class = ratingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


def update(self, request, *args, **kwargs):
    response = {'message': 'You cant update ratings like this'}
    return Response(response, status=status.HTTP_400_BAD_REQUEST)


def create(self, request, *args, **kwargs):
    response = {'message': 'You cant create ratings like this'}
    return Response(response, status=status.HTTP_400_BAD_REQUEST)