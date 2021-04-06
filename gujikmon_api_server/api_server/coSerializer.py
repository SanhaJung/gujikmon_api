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
            'x',
            'y',
            'superIndTpCd',
            'superIndTpNm',
            'coContent',
            'coMainProd',
            'coGdpnt',
            'coHomePage',
            'alwaysWorkerCnt',
            'recruitment'
            ]




