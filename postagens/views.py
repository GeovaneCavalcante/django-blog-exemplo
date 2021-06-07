from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import Post
from .serializers import PostSerializer


class ListPost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
