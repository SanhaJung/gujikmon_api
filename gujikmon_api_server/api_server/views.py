from .models import Companies
from .coSerializer import CoSerializer
# from .services import coFiltering
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# 기업 필터링 
@api_view(['GET'])
def companies(request):
    regionCd=request.GET['region_code']
    superIndTpCd=request.GET['business_code']
    # coFiltering(regionCd,superIndTpCd)

    companies = Companies.objects.get(id=1)
    serializer = CoSerializer(companies)
    return Response(serializer.data)


# 기업이름 검색 
# -키워드로 검색
@api_view(['GET'])
def searchCompany(request,keyword):
    coNm=keyword
    companies = Companies.objects.filter(coNm__contains=coNm)
    serializer=CoSerializer(companies,many=True)
    return Response(serializer.data)


# 관심기업 필터링
@api_view(['GET'])
def favoriteCompanies(request):
    # userdb와 연동/userapp에서 생성
    pass

