from djongo import models
from django import forms

# Create your models here.
class Info (models.Model):
    objects=models.DjongoManager()
    exit = models.BooleanField(default=False)
    wantedInfoUrl=models.CharField(db_column='wantedInfoUrl',max_length=250)
    wantedMobileInfoUrl = models.CharField(db_column='wantedMobileInfoUrl',max_length=250)
    class Meta:
        abstract = True

class Certified(models.Model):
    ceNm=models.CharField(max_length=250)
    def __str__(self):
        return self.ceNm
    class Meta:
        abstract = True
        
class CertifiedForm(forms.ModelForm):
    class Meta:
        model=Certified
        fields =['ceNm',]


class Companies(models.Model):
    objects=models.DjongoManager()
    coNm =models.CharField(max_length=250)
    coAddr = models.CharField(max_length=250)
    regionCd = models.IntegerField()
    regionNm = models.CharField(max_length=250)
    superIndTpCd = models.IntegerField()
    superIndTpNm = models.CharField(max_length=250)
    coContent =  models.TextField()
    coMainProd = models.CharField(max_length=250)
    coGdpnt = models.CharField(max_length=250)
    coHomePage = models.CharField(max_length=250)
    alwaysWorkerCnt = models.CharField(max_length=250)
    sgBrandNm = models.ArrayField(model_container=Certified,model_form_class=CertifiedForm)
    info = models.EmbeddedField(model_container=Info,null=True)





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
#           "exit":true,
#          "wantedInfoUrl":"워크넷 채용정보 URL(string)",        
#        "wantedMobileInfoUrl":"워크넷 모바일 채용정보 URL(string)"
#        }}
