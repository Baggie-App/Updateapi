from django.shortcuts import render
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.db.models import Q

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from poll.models import *
from poll.serializers import *
from headers import *

# Create your views here.
#
#
# class QuestionViewSet(ListCreateAPIView):
#     serializer_class = QuestionSerializer
#     queryset = Question.objects.all()
#     lookup_field = 'id'
#
#
#     @action(detail=True, methods=["GET"])
#     def choices(self, request, id=None):
#         question = self.get_object()
#         choices = Choice.objects.filter(question=question)
#         serializer = ChoiceSerializer(choices, many=True)
#         return Response(serializer.data, status=200)
#
#     @action(detail=True, methods=["POST"])
#     def choice(self, request, id=None):
#         question = self.get_object()
#         data = request.data
#         data["question"] = question.id
#         serializer = ChoiceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.erros, status=400)

from rest_framework import viewsets, mixins, status
from rest_framework.settings import api_settings
from poll.models import *
from poll.serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

class PollAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


# Create your views here.

# class PostViewSet(ListCreateAPIView):
#     """
#     Post ModelViewSet.
#     """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     # permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def create(self, request, *args, **kwargs):
#         print(request.data)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def get_success_headers(self, data):
#         try:
#             return {'Location': str(data[api_settings.URL_FIELD_NAME])}
#         except (TypeError, KeyError):
#             return {}


# class PollAPIView(APIView):
#     def get(self, request):
#         questions = Question.objects.all()
#         serailizer = QuestionSerializer(questions, many=True)
#         return Response(serailizer.data, status=200)
#
#     def post(self, request):
#         data = request.data
#         serializer = QuestionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.erros, status=400)
