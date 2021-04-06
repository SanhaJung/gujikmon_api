from .models import Companies
from rest_framework import serializers


class CoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields =[
            'coNm',
            'coAddr',
            'regionCd',
            'regionNm',
            'superIndTpCd',
            'superIndTpNm',
            'coContent',
            'coMainProd',
            'coGdpnt',
            'coHomePage',
            'alwaysWorkerCnt',
            'sgBrandNm',
            'info',
            ]




