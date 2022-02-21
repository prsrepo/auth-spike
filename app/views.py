import json
import traceback
from uuid import uuid4

import requests
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from app.handlers.oauth2handler import Oauth2Handler
from app.models import KRMap, Connection
from app.serializers import KRMapSerializer, ConnectionSerializer


def index(request):
    return HttpResponse({"data": "sample"})


@api_view(['GET', 'POST', 'DELETE'])
def krmap_list(request):
    if request.method == 'GET':
        krmaps = KRMap.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            krmaps = krmaps.filter(title__icontains=title)

        krmaps_serializer = KRMapSerializer(krmaps, many=True)
        return JsonResponse(krmaps_serializer.data, safe=False)
    elif request.method == 'POST':
        krmap_data = JSONParser().parse(request)
        krmap_serializer = KRMapSerializer(data=krmap_data)
        if krmap_serializer.is_valid():
            krmap_serializer.save()
            return JsonResponse(krmap_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(krmap_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def krmap_detail(request, pk):
    # find krmap by pk (id)
    try:
        krmap = KRMap.objects.get(pk=pk)
    except krmap.DoesNotExist:
        return JsonResponse({'message': 'The krmap does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        krmap_serializer = KRMapSerializer(krmap)
        return JsonResponse(krmap_serializer.data)
    elif request.method == 'PUT':
        krmap_data = JSONParser().parse(request)
        krmap_serializer = KRMapSerializer(krmap, data=krmap_data)
        if krmap_serializer.is_valid():
            krmap_serializer.save()
            return JsonResponse(krmap_serializer.data)
        return JsonResponse(krmap_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        krmap.delete()
        return JsonResponse({'message': 'krmap was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def get_autheticate_url(request):
    try:
        connection_data = JSONParser().parse(request)
        if request.method == 'POST':
            conn = ConnectionSerializer(
                data={
                    "name": connection_data.get('name'),
                    "email": connection_data.get('email'),
                    "meta_data": {
                        "state": json.dumps({
                            "email": connection_data.get('email'),
                            "session": str(uuid4())
                        }),
                        "is_autheticated": False,
                        "access_token": None,
                        "refresh_token": None,
                        "expires_at": None,
                        "expires_in": None
                    }
                }
            )
            if conn.is_valid():
                conn.save()
            else:
                return JsonResponse(conn.errors, status=status.HTTP_400_BAD_REQUEST)
            conn_data = conn.data
            return JsonResponse(
                {
                    "url": Oauth2Handler().get_authorization_url(conn_data.get('meta_data').get('state'))
                },
                status=status.HTTP_200_OK
            )
    except Exception as e:
        return JsonResponse({
            "message": f"Exception occured in get auth url with {str(e)}"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handle_callback(request):
    try:
        authorization_code = request.GET.get('code')
        state = request.GET.get('state')
        Oauth2Handler().handle_callback(authorization_code, state)
        return HttpResponse('''
            <!DOCTYPE html>
            <html><body><script type="text/javascript">
                open(location, '_self').close();
            </script></body></html>
        ''')
    except Exception as e:
        return JsonResponse({
            "message": f"Exception occured in get auth url with {str(e)}"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recent_files(request):
    try:
        res = Oauth2Handler().send_request(
            url='https://graph.microsoft.com/v1.0/me/drive/recent?$top=1',
            method='GET'
        )
        return JsonResponse(
            res.json(),
            safe=False,
            status=status.HTTP_200_OK
        )
    except Exception as e:
        print(traceback.format_exc().splitlines())
        return JsonResponse({
            "message": f"Exception occured in get auth url with {str(e)}"
        }, status=status.HTTP_400_BAD_REQUEST)

