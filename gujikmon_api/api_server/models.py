from djongo import models
from django import forms

# Create your models here.
class Info( models.Model):
    objects = models.DjongoManager()
    title = models.CharField(max_length=250)
    wantedInfoUrl = models.CharField(max_length=250)
    wantedMobileInfoUrl = models.CharField(max_length=250)
    class Meta:
        abstract = True

class InfoForm(forms.ModelForm):
    class Meta:
        model= Info
        fields = (
            'title','wantedInfoUrl','wantedMobileInfoUrl'
        )

class Certified(models.Model):
    objects=models.DjongoManager()
    ceNm=models.CharField(max_length=250)
    class Meta:
        abstract = True

class CertifiedForm(forms.ModelForm):
    class Meta:
        model = Certified
        fields = (
            'ceNm',
        )


class Companies(models.Model):
    objects=models.DjongoManager()
    coNm = models.CharField(max_length=250)
    coAddr = models.CharField(max_length=250)
    superRegionCd = models.IntegerField()  # 지역코드 상
    superRegionNm = models.CharField(max_length=250)
    regionCd =models.IntegerField() # 지역코드 중
    regionNm = models.CharField(max_length=250)
    x = models.CharField(max_length=250)
    y = models.CharField(max_length=250)
    superIndTpCd = models.CharField(max_length=250) # 업종코드 상
    superIndTpNm = models.CharField(max_length=250)
    indTpCd = models.CharField(max_length=250)# 업종코드 중
    indTpNm = models.CharField(max_length=250)
    coMainProd = models.CharField(max_length=250)
    coHomePage = models.CharField(max_length=250)
    alwaysWorkerCnt = models.CharField(max_length=250)
    sgBrandNm = models.ArrayField(model_container=Certified,model_form_class=CertifiedForm)
    recruitment = models.BooleanField(default=False)
    info = models.ArrayField(model_container=Info,model_form_class=InfoForm)




# {"coNm":"기업명(string)",    
#  "coAddr":"기업주소(string)",
# "regionCd":1234,
#  "regionNm":"지역명(string)",
#  "superIndTpCd":1234,
# "superIndTpNm":"업종 명(string)",
#  "coContent":"사업 내용(string)",
#   "coMainProd":"주요 생산품목(string)",
#       "coGdpnt":"기업 장점내용(string)",
#      "coHomePage":"회사 홈페이지(string)",
#     "alwaysWorkerCnt":"상시 근로자 수(string)",
#    "sgBrandNm":[{'ceNm':'인증제도1'}, {'ceNm':'인증제도2'}],     
#     "info":{
#           "title":"채용 공고 내용"
#          "wantedInfoUrl":"워크넷 채용정보 URL(string)",        
#        "wantedMobileInfoUrl":"워크넷 모바일 채용정보 URL(string)"
#        }}