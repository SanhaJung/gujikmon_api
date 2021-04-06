from .models import Companies
from .models import Certified
# 기업 필터링 
# -지역(lv1,lv2)(regionCd)
# -인증제도(lv1,lv2)(superIndTpCd)
def  coFiltering(select_data):
    regionCode =select_data['regionCd']
    businessCode=select_data['businessCd']
    certificationCd=select_data['certificationCd']
    recruitment = select_data['apply']
    # inner_qs = Certified.objects.
    companies=Companies.objects.filter(
        regionCd__in=regionCode,
        superIndTpCd__in=businessCode,
        recruitment=recruitment,
        # sgBrandNm_in=certificationCd
        )
  
   
    return companies

