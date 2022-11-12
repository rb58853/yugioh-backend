# from rest_framework import generics, permissions, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache 
# from django.views.decorators.csrf import csrf_protect
# from django.views.generic.edit import FormView
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponseRedirect
# from rest_framework.authtoken.models import Token

# from .models import Player 
# from .permissions import IsPlayerOrReadOnly
# from .serializers import PlayerSerializer  

# class PlayerListView(generics.ListAPIView):
#     queryset = Player.objects.all() 
#     serializer_class = PlayerSerializer
    
# class DetailPlayer(generics.RetrieveUpdateDestroyAPIView): 
#     permission_classes =(IsPlayerOrReadOnly,)
#     queryset = Player.objects.all() 
#     serializer_class = PlayerSerializer
    
# class Logout(APIView):

#     def get(self, request, format = None):
#         request.user.auth_token.delete()
#         logout(request)
#         return Response(status = status.HTTP_200_OK)
    
# class Login(FormView):
#     template_name = "login.html"
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('api:person_list')

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super(Login,self).dispatch(request, *args, *kwargs)

#     def form_valid(self, form):
#         user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#         token, _ = Token.objects.get_or_create(user = user)
#         if token:
#             login(self.request, form.get_user())
#             return super(Login, self).form_valid(form)




