from .models import Companies
from .coSerializer import CoSerializer
from .services import coFiltering
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# 기업 필터링 
@api_view(['POST'])
def companies(request):
    select_param = json.loads(request.body)
    coFiltering(select_param)

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

