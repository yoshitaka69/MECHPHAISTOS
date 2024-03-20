from rest_framework import viewsets

from .models import CeList
from accounts.models import CompanyCode
from .serializers import CeListSerializer, CompanyCodeCeListSerializer


#Critical equipment list
class CeListViewSet(viewsets.ModelViewSet):
    queryset = CeList.objects.all()
    serializer_class = CeListSerializer

class CeListByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeCeListSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('ceList_companyCode')
        return CompanyCode.objects.all()



