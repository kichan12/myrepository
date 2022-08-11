from django.shortcuts import render
from rest_framework import viewsets

from accounts.models import User
from .models import Story, StoryComment
from .serializers import CommentSerializer, StorySerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from petpe import models


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_update(serializer)

### 댓글 기능 추가 ### 2022.08.10
class CommentViewSet(viewsets.ModelViewSet):
    queryset = StoryComment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


@csrf_exempt
def post_like(request,story_id):
    response_body = {"result": ""}

    if request.user.is_authenticated:
        if request.method == "POST":
            story = get_object_or_404(models.Story, pk=story_id)
            existed_user = Story.image_likes.filter(pk=request.user.id).exists()

            if existed_user:
            # 좋아요 누른 상태일 때는 "좋아요 취소"
                story.image_likes.remove(request.user)
                response_body["result"] = "dislike"

            else:
            # 좋아요가 아닐때 "좋아요"
                story.image_likes.add(status=200,data=request.user)
                response_body["result"] = "like"

            story.save()
    else:
        return JsonResponse(status=403, data=response_body)