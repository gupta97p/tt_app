from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import user_reg, Tournament
from .serializers import RegisterSerializer, TournamentSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework import filters

#user classes

class RegisterViewSet(ViewSet):
    def create(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({ 'message': serializer.errors}, 422)
            serializer.save()
            return Response({'message': 'record Saved successfully', 'data': serializer.data}, 200)
        except Exception as e:
            return Response({ 'message': str(e)}, 500)

class LoginViewSet(ViewSet):
    def create(self, request):

        try:
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                token, created = Token.objects.get_or_create(user_id=user.id)
                return Response(
                    {'message': ['welcome', request.POST.get('username')], 'your login token is': token.key}, 200)

            return Response({'message': 'invalid credentials'}, 401)
        except Exception as e:
            return Response({'data': '', 'message': str(e)}, 500)

class ProfileViewSet(ViewSet):

    def partial_update(self, request, pk=None):

        try:
            user_detail = user_reg.objects.get(pk=pk)
            serializer = RegisterSerializer(user_detail,data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'data':'internal server error','message':'error aa gyi'},500)

            serializer.save()

        except Exception as e:

            return Response('some exception occured' + str(e))

        return Response('record Updated successfully')

    def retrieve(self, request,pk=None):

        queryset = user_reg.objects.get(pk=pk)
        serializer_class = RegisterSerializer(queryset)
        return Response(serializer_class.data)

class deleteViewSet(ViewSet):
    def destroy(self, request, pk=None):
        try:
            user_detail = UserValues.objects.get(pk=pk)
            user_detail.delete()

        except Exception as e:
            return Response('some exception occured' + str(e))
        return Response('record Deleted successfully')

#tournament classes
class HomeView(ViewSet):
    def list(self,request):

        queryset = user_reg.objects.all()
        serializer_class = RegisterSerializer(queryset, many=True)
        return Response(serializer_class.data)

class CreateTournament(ViewSet):
    def create(self,request):
        try:
            serializer = TournamentSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'data': '', 'message': serializer.errors}, 422)
            serializer.save()
            return Response({'message': 'record Saved successfully', 'data': serializer.data}, 200)
        except Exception as e:
            return Response({'data': '', 'message': str(e)}, 500)

class TournamentDetail(ViewSet):

    def retrieve(self, request, pk=None):
        print(request.data)
        queryset = Tournament.objects.get(pk=pk)
        serializer_class = TournamentSerializer(queryset)
        return Response(serializer_class.data)

