from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from favorites.entity.favorites import Favorites
from favorites.service.favorites_service_impl import FavoritesServiceImpl
from kakao_oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class FavoritesView(viewsets.ViewSet):
    queryset = Favorites.objects.all()

    redisService = RedisServiceImpl.getInstance()
    favoritesService = FavoritesServiceImpl.getInstance()

    def favoritesRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.favoritesService.favoritesRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            return Response({ 'error': str(e) }, status=status.HTTP_400_BAD_REQUEST)
