from django.shortcuts import render

from .models import PlanOptimizationBenefit,ImprovementBenefit,RiskAvoidanceBenefit,VendorSelectionBenefit
from .serializers import POBSerializer,CompanyCodePOBSerializer,IBSerializer,CompanyCodeIBSerializer,RABSerializer,CompanyCodeRABSerializer,VSBSerializer,CompanyCodeVSBSerializer


#PlanOptimization
class POBViewSet(viewsets.ModelViewSet):
    queryset = PlanOptimizationBenefit.objects.all()
    serializer_class = POBSerializer

class CompanyCodePOBViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodePOBSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('planOptimizationBenefit_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



#ImprovementBenefit
class IBViewSet(viewsets.ModelViewSet):
    queryset = ImprovementBenefit.objects.all()
    serializer_class = IBSerializer

class CompanyCodeIBViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeIBSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('improvementBenefit_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




#riskAvoidanceBenefit
class RABViewSet(viewsets.ModelViewSet):
    queryset = RiskAvoidanceBenefit.objects.all()
    serializer_class = RABSerializer

class CompanyCodeRABViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeRABSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('riskAvoidanceBenefit_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



#vendorSelectionBenefit
class VSBViewSet(viewsets.ModelViewSet):
    queryset = VendorSelectionBenefit.objects.all()
    serializer_class = VSBSerializer

class CompanyCodeVSBViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeVSBSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('vendorSelectionBenefit_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset


