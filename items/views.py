from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Item, Comment
from .serializers import CommentSerializer, ItemSerializer, PopulatedItemSerializer

class ItemListView(APIView):
    #GET ALL ITEMS

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        items = Item.objects.all()
        serialized_items = PopulatedItemSerializer(items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)


class ItemCreateView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.data['sold_by'] = request.user.id
        created_item = ItemSerializer(data=request.data)
        if created_item.is_valid():
            print('working round 3')
            created_item.save()
            return Response(created_item.data, status=status.HTTP_201_CREATED)
        return Response(created_item.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)    

class ItemDetailView(RetrieveUpdateDestroyAPIView):
    '''Detail View for /items/id SHOW UPDATE DELETE'''
    queryset = Item.objects.all()
    serializer_class = PopulatedItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentListView(APIView):
    ''' List View for /items/:itemId/comments CREATE comments'''
    
    permission_classes = (IsAuthenticated, )

    def post(self, request, item_pk):
        request.data['item'] = item_pk
        request.data['owner'] = request.user.id
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CommentDetailView(APIView):
    ''' DELETE COMMENT VIEW '''

    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):
        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            # item_comment_to_delete = Item.objects.get(pk=)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail='Comment Not Found')

class ItemLikeView(APIView):
    ''' Adds likes to items or removes if already liked '''

    permission_classes = (IsAuthenticated, )

    def post(self, request, item_pk):
        try:
            item_to_like = Item.objects.get(pk=item_pk)
        except Item.DoesNotExist:
            raise NotFound()

        if request.user in item_to_like.liked_by.all():
            item_to_like.liked_by.remove(request.user.id)
        else:
            item_to_like.liked_by.add(request.user.id)

        serialized_item = ItemSerializer(item_to_like)

        return Response(serialized_item.data, status=status.HTTP_202_ACCEPTED)    
