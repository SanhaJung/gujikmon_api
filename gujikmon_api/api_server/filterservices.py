from .models import Companies
from .models import Certified
from .jsondata.region import allregioncode
from .jsondata.businessCode import allindTpCd

# 기업 필터링 
# -지역(lv1,lv2)(regionCd)
# -인증제도(lv1,lv2)(superIndTpCd)
def  coFiltering(select_data):
    # 지역 코드
    # -지역 무관 all
    # -서울 11000 (11000~20000)
    # -부산 26000 (26000~26710)
    # -대구 27000 (27000~27710)
    # -인천 28000 (28000~28720)
    # -광주 29000 (29000~29200)
    # -대전 30000 (30000~30230)
    # -울산 31000 (31000~31710)
    # -세종 36110
    # -경기 41000 (41000~41830)
    # -강원 42000 (42000~42830)
    # -충북 43000 (43000~43800)
    # -충남 44000 (44000~44825)
    # -전북 45000 (45000~45800)
    # -전남 46000 (46000~46910)
    # -경북 47000 (47000~47940)
    # -경남 48000 (48000~48890)
    # -제주 50000 (50000~50130)
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
    if not "all" in certificationCd:
        for ce in certificationCd:
            dic = {}
            dic['ceNm']=ce
            ce_list.append(dic)
    # 채용 여부
    apply = select_data['apply']


    # 지역코드가 선택하지 않았을 경우
    if "all" in regionCode :
        # 업종코드를 선택하지 않았을 경우
        if "all" in businessCode:
            # 인증기업을 선택하지 않았을 경우
            if not ce_list:
                # 채용 여부를 선택하지 않았을 경우
                if "all" == apply:
                    companies=Companies.objects.all()
                    return companies
                #채용 여부를 선택했을 경우
                else: 
                    companies = Companies.objects.filter(
                    recruitment=apply
                    )
                    return companies
            # 인증 기업을 선택했을 경우
            else:
                if "all" == apply:
                    companies = Companies.objects.filter(
                    sgBrandNm__in=ce_list
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    recruitment=apply,
                    sgBrandNm__in=ce_list
                    )
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
                if "all"==apply:
                    companies = Companies.objects.filter(
                    indTpCd__in=business
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    indTpCd__in=business,
                    recruitment=apply
                    )
                    return companies
            else:
                if "all" == apply:
                    companies = Companies.objects.filter(
                    indTpCd__in=business,
                    sgBrandNm__in=ce_list
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    recruitment=apply,
                    indTpCd__in=business,
                    sgBrandNm__in=ce_list
                    )
                    return companies
    # 지역코드를 선택했을 경우 
    else:
        # 
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
        
        print(midelregion)
        # 업종을 선택하지 않았을 경우
        if "all" in businessCode:
            # 인증제도를 선택하지 않았을 경우
            if not ce_list:
                # 채용 여부를 선택하지 않았을 경우
                if "all" == apply:
                    companies = Companies.objects.filter(
                    regionCd__in=midelregion,
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    regionCd__in=midelregion,
                    recruitment=apply
                    )
                    return companies
            else:
                if "all" == apply:
                    companies = Companies.objects.filter(
                    regionCd__in=midelregion,
                    sgBrandNm__in=ce_list
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    recruitment=apply,
                    regionCd__in=midelregion,
                    sgBrandNm__in=ce_list
                    )
                    return companies
        # 업종코드가 모두가 아닌경우
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
                if "all" == apply:
                    companies = Companies.objects.filter(
                    regionCd__in=midelregion,
                    indTpCd__in=business,
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    regionCd__in=midelregion,
                    indTpCd__in=business,
                    recruitment=apply
                    )
                    return companies
            else:
                if "all" == apply:
                    companies = Companies.objects.filter(
                    regionCd__in=midelregion,
                    indTpCd__in=business,
                    sgBrandNm__in=ce_list
                    )
                    return companies
                else:
                    companies = Companies.objects.filter(
                    recruitment=apply,
                    regionCd__in=midelregion,
                    indTpCd__in=business,
                    sgBrandNm__in=ce_list
                    )
                    return companies
            


      
