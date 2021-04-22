from .models import Companies
from .jsondata.region import allregioncode
from .jsondata.businessCode import allindTpCd

# 기업 필터링 
# -지역(lv1,lv2)(regionCd)
# -인증제도(lv1,lv2)(superIndTpCd)
def  coFiltering(select_data):
    superRegionCd = [11000,26000,27000,28000,29000,30000,31000,
    41000,42000,43000,44000,45000,46000,47000,48000,50000]

    regionCode =select_data['regionCd'] 
    #업종 코드 
    superBusinessCd=["A",'B','C','D','E','F','G',
    'H','I','J','K','L','M','N','O','P','Q','R','S','T','U']
    businessCode=select_data['businessCd']
  
    # 인증 제도
    certificationCd=select_data['certificationCd']
  
    ce_list=[]
    if  "all" not in certificationCd:
        for ce in certificationCd:
            dic = {}
            dic['ceNm']=ce
            ce_list.append(dic)


    # 지역코드가 선택하지 않았을 경우
    if "all" in regionCode :
        # 업종코드를 선택하지 않았을 경우
        if "all" in businessCode:
            # 인증기업을 선택하지 않았을 경우
            if not ce_list:
                # 채용 여부를 선택하지 않았을 경우
                
                companies=Companies.objects.all() #모든값
                return companies
           
            # 인증 기업을 선택했을 경우
            else:
               
                companies = Companies.objects.filter(
                sgBrandNm__in=ce_list,               
                )                                 #인증
                                            # 인증,채용여부
                
                return companies
        # 업종코드를 선택했을 경우
        else:
            # 대분류
            superBusiness = [i for i in superBusinessCd if i in businessCode ]
            
            # 중분류
            business = list(set(businessCode)-set(superBusinessCd))
           
            #대분류가 있으면
            if superBusiness:
                for bu in superBusiness:
                    businessplus=allindTpCd[bu]
                    business+=businessplus

            if not ce_list:

                companies = Companies.objects.filter(
                indTpCd__in=business
                )                                  #업종
                return companies
               
            else:
            
                companies = Companies.objects.filter(
                indTpCd__in=business,
                sgBrandNm__in=ce_list
                )                                   #업종,인증
                return companies
               
    # 지역코드를 선택했을 경우 
    else:
        # 대분류
        largeregion = [i for i in superRegionCd if i in regionCode ]
        # 중분류
        midelregion = list(set(regionCode)-set(superRegionCd))
        # 대분류가 있으면
        if largeregion:
            # 대분류 속 중분류 추가 
            for la  in largeregion:
                str_la = str(la)
                midelregionplus=allregioncode[str_la]
                midelregion+=midelregionplus

        # 업종을 선택하지 않았을 경우
        if "all" in businessCode:
            # 인증제도를 선택하지 않았을 경우
            if not ce_list:
                # 채용 여부를 선택하지 않았을 경우
                companies = Companies.objects.filter(
                regionCd__in=midelregion,
                )                                       #지역
                return companies
            else:
                companies = Companies.objects.filter(
                regionCd__in=midelregion,
                sgBrandNm__in=ce_list
                )                                       #지역,인증
                return companies
              
        # 업종을 선택했을 경우
        else:
            # 대분류
            superBusiness = [i for i in superBusinessCd if i in businessCode ]
            # 중분류
            business = list(set(businessCode)-set(superBusinessCd))
            if superBusiness:
                for bu in superBusiness:
                    businessplus=allindTpCd[bu]
                    business+=businessplus

            if not ce_list:
                companies = Companies.objects.filter(
                regionCd__in=midelregion,
                indTpCd__in=business
                )                               #지역,업종
                return companies
          
            else:
                companies = Companies.objects.filter(
                regionCd__in=midelregion,
                indTpCd__in=business,
                sgBrandNm__in=ce_list
                )                               #지역,업종,인증
                return companies
              
            


      
