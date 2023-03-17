import json
from rest_framework import viewsets
from .serializer import OverviewSerializer, AlbumSerializer, SongSerializer, RecommendSerializer, SanctuarySerializer, UserSerializer
from yorushika.models import Overview, Album, Song, Recommend, Sanctuary
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class SampleClass(APIView):
    def get(self, request):
        contents = {"test": "OK"}
        return Response(contents)


sample = SampleClass.as_view()


class OverviewViewSet(viewsets.ModelViewSet):
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.filter(album=5)
    serializer_class = SongSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


song_list = SongList.as_view()


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


song_detail = SongDetail.as_view()


class RecommendViewSet(viewsets.ModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer


class SanctuaryViewSet(viewsets.ModelViewSet):
    queryset = Sanctuary.objects.all()
    serializer_class = SanctuarySerializer


class SanctuaryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Sanctuary.objects.all()
    serializer_class = SanctuarySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


sanctuary_list = SanctuaryList.as_view()


class SanctuaryDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Sanctuary.objects.all()
    serializer_class = SanctuarySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


sanctuary_detail = SanctuaryDetail.as_view()


# クラスビューを使うことでPOST、GETの分岐を
# if文を使うことなく表現することができる
class RecommendList(APIView):
    def get(self, request):
        recommends = Recommend.objects.all()
        serializer = RecommendSerializer(recommends, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


recommend_list = RecommendList.as_view()


class RecommendDetail(APIView):
    def get_object(self, pk):
        try:
            return Recommend.objects.get(pk=pk)
        except Recommend.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recommend = self.get_object(pk)
        serializer = RecommendSerializer(recommend)
        return Response(serializer.data)

    def put(self, request, pk):
        recommend = self.get_object(pk)
        serializer = RecommendSerializer(recommend, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recommend = self.get_object(pk)
        recommend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


recommend_detail = RecommendDetail.as_view()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_list = UserList.as_view()


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_detail = UserDetail.as_view()
