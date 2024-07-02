from rest_framework import serializers
from accounts.models import CompanyCode,Plant
from .models import (PlanOptimizationBenefit,ImprovementBenefit,RiskAvoidanceBenefit,VendorSelectionBenefit)



#PlanOptimizationBenefit
class POBSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )



    class Meta:
        model = PlanOptimizationBenefit
        fields =  ['companyCode','planOptJan','planOptFeb','planOptMar','planOptApr','planOptMay','planOptJun','planOptJul','planOptAug','planOptSep','planOptOct','planOptNov','planOptDec']


class CompanyCodePOBSerializer(serializers.ModelSerializer):
    pOBList = POBSerializer(many=True, read_only=True, source='planOptimizationBenefit_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'pOBList']




#ImprovementBenefit
class IBSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )



    class Meta:
        model = ImprovementBenefit
        fields =  ['companyCode','improvementJan','improvementFeb','improvementMar','improvementApr','improvementMay','improvementJun','improvementJul','improvementAug','improvementSep','improvementOct','improvementNov','improvementDec']


class CompanyCodeIBSerializer(serializers.ModelSerializer):
    iBList = IBSerializer(many=True, read_only=True, source='improvementBenefit_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'iBList']




#RiskAvoidanceBenefit
class RABSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )


    class Meta:
        model = RiskAvoidanceBenefit
        fields =  ['companyCode','riskAvoidJan','riskAvoidFeb','riskAvoidMar','riskAvoidApr','riskAvoidMay','riskAvoidJun','riskAvoidJul','riskAvoidAug','riskAvoidSep','riskAvoidOct','riskAvoidNov','riskAvoidDec']


class CompanyCodeRABSerializer(serializers.ModelSerializer):
    rABList = RABSerializer(many=True, read_only=True, source='riskAvoidanceBenefit_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'rABList']



#VendorSelectionBenefit
class VSBSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
    slug_field='companyCode', 
    queryset=CompanyCode.objects.all()
    )


    class Meta:
        model = VendorSelectionBenefit
        fields =  ['companyCode','vendorSelectJan','vendorSelectFeb','vendorSelectMar','vendorSelectApr','vendorSelectMay','vendorSelectJun','vendorSelectJul','vendorSelectAug','vendorSelectSep','vendorSelectOct','vendorSelectNov','vendorSelectDec']


class CompanyCodeVSBSerializer(serializers.ModelSerializer):
    vSBList = VSBSerializer(many=True, read_only=True, source='vendorSelectionBenefit_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'vSBList']


