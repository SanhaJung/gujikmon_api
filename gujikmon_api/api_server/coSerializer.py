from .models import Companies
from rest_framework import serializers


class CoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields =[
            'coNm',
            'coAddr',
            'superRegionCd',
            'superRegionNm',
            'regionCd',
            'regionNm',
            'x',
            'y',
            'superIndTpCd',
            'superIndTpNm',
            'indTpCd',
            'indTpNm',
            'coContent',
            'coMainProd',
            'coGdpnt',
            'coHomePage',
            'alwaysWorkerCnt',
            'recruitment'
            ]


