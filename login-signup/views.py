from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from users.serializers import RegisterSerializer ,UpdateSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class RegisterViewSet(ViewSet):
    def create(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'data': '', 'message': serializer.errors}, 422)

            serializer.save()
            return Response({'message': 'record Saved successfully', 'data': serializer.data}, 200)
        except Exception as e:
            return Response({'data': '', 'message': str(e)}, 500)


class LoginViewSet(ViewSet):
    def create(self, request):

        try:
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                token, created = Token.objects.get_or_create(user_id=user.id)

                return Response({'message':['welcome',request.POST.get('username')],'your login token is':token.key},200)

            return Response({'message':'invalid credentials'},401)
        except Exception as e:
            return Response({'data': '', 'message': str(e)}, 500)
        

class ProfileViewSet(ViewSet):

    def partial_update(self, request, pk=None):

        try:
            user_detail = user_reg.objects.get(pk=pk)
            print(pk)
            serializer = RegisterSerializer(user_detail,data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({'data':'internal server error','message':'error aa gyi'},500)

            serializer.save()

        except Exception as e:

            return Response('some exception occured' + str(e))

        return Response('record Updated successfully')

    def retrieve(self,request, pk=None):

        queryset = user_reg.objects.get(pk=pk)
        serializer_class = RegisterSerializer(queryset)
        return Response(serializer_class.data)
