from .models import Companies
from .coSerializer import CoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# 기업 필터링 
@api_view(['GET'])
def companies(request):
    companies = Companies.objects.get(id=1)
    serializer = CoSerializer(companies)
    # info = json.loads(serializer.data['info'])
    # sgBrandNm =json.loads(serializer.data['sgBrandNm'])
    # print(companies.info)

    api_list ={}
    api_list['info']=companies.info
    api_list['sgBrandNm']=companies.sgBrandNm
    return Response(api_list)

