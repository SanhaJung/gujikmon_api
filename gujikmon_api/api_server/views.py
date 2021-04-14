from .models import Companies,Certified
from .coSerializer import CoSerializer
from .filterservices import coFiltering
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
# from django.http import JsonResponse

# 기업 필터링 
@api_view(['POST'])
def companies(request):
    print(request.body)
    select_param = json.loads(request.body)
    # 필터링 서비스로 필터링된 companies를 받아온다
    companies=coFiltering(select_param)
    serializer = CoSerializer(companies,many=True)
    count=len(companies)
    json_list =[]
    json_list.append({'count':count})
    for idx,co in enumerate(companies):
        company={}
        company['company']=serializer.data[idx]
        company['sgBrandNm']=co.sgBrandNm
        company['info']=co.info
        json_list.append(company)
    return Response(json_list)


# 기업이름 검색 
# -키워드로 검색
@api_view(['GET'])
def searchCompany(request,keyword):
    coNm=keyword
    companies = Companies.objects.filter(coNm__contains=coNm)
    serializer=CoSerializer(companies,many=True)
    json_list =[]
    for idx,co in enumerate(companies):
        company={}
        company['company']=serializer.data[idx]
        company['sgBrandNm']=co.sgBrandNm
        company['info']=co.info
        json_list.append(company)
    return Response(json_list)


# 관심기업 필터링
@api_view(['GET'])
def favoriteCompanies(request):
    # userdb와 연동/userapp에서 생성
    pass


