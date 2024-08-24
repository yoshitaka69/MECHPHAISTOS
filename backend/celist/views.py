from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CeList, RiskMatrixPossibility, CompanyCode, RiskMatrixImpact
from .serializers import CeListSerializer, CompanyCodeCeListSerializer, RiskMatrixPossibilitySerializer, RiskMatrixImpactSerializer

# Critical equipment list
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




@api_view(['POST'])
def post_risk_matrix_possibility(request):
    print("Request data:", request.data)
    
    company_code_str = request.data.get('companyCode')
    if not company_code_str:
        return Response({"error": "companyCode is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    all_company_codes = CompanyCode.objects.all()
    print("All CompanyCodes in the database:")
    for code in all_company_codes:
        print(f"id: {code.id}, companyCode: {code.companyCode}")
    
    company_codes = CompanyCode.objects.filter(companyCode=company_code_str)
    print("Matching CompanyCodes:", company_codes)
    
    if not company_codes.exists():
        return Response({"error": "No matching companyCode found"}, status=status.HTTP_400_BAD_REQUEST)
    if company_codes.count() > 1:
        return Response({"error": "Multiple matching companyCodes found"}, status=status.HTTP_400_BAD_REQUEST)
    
    company_code = company_codes.first()
    
    risk_matrix_possibility = RiskMatrixPossibility(
        companyCode=company_code,
        x=request.data.get('x'),
        y=request.data.get('y')
    )
    risk_matrix_possibility.save()

    coordinates = RiskMatrixPossibility.objects.filter(companyCode=company_code).order_by('-timestamp')[10:]
    for coordinate in coordinates:
        coordinate.delete()

    serializer = RiskMatrixPossibilitySerializer(risk_matrix_possibility)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_latest_risk_matrix_possibilities(request, company_code):
    try:
        company_code_instance = CompanyCode.objects.get(companyCode=company_code)
    except CompanyCode.DoesNotExist:
        return Response({"error": "Invalid companyCode"}, status=status.HTTP_400_BAD_REQUEST)

    latest_possibilities = RiskMatrixPossibility.objects.filter(companyCode=company_code_instance).order_by('-timestamp')[:10]
    serializer = RiskMatrixPossibilitySerializer(latest_possibilities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_risk_matrix_impact(request):
    company_code_str = request.data.get('companyCode')
    level_set_value = request.data.get('levelSetValue')
    x_value = request.data.get('x')
    y_value = request.data.get('y')
    
    # ログを出力
    print(f"Received POST request with data: companyCode={company_code_str}, levelSetValue={level_set_value}, x={x_value}, y={y_value}")

    if not company_code_str:
        return Response({"error": "companyCode is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        company_code = CompanyCode.objects.get(companyCode=company_code_str)
    except CompanyCode.DoesNotExist:
        return Response({"error": "Invalid companyCode"}, status=status.HTTP_400_BAD_REQUEST)
    
    risk_matrix_impact = RiskMatrixImpact(
        companyCode=company_code,
        levelSetValue=level_set_value,
        x=x_value,
        y=y_value
    )
    risk_matrix_impact.save()

    # 最新10件のみ保持し、それ以上は削除
    impacts = RiskMatrixImpact.objects.filter(companyCode=company_code, levelSetValue=level_set_value).order_by('-timestamp')
    if impacts.count() > 10:
        for impact in impacts[10:]:
            impact.delete()

    serializer = RiskMatrixImpactSerializer(risk_matrix_impact)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_latest_risk_matrix_impacts(request, company_code, level_set_value):
    try:
        company_code_instance = CompanyCode.objects.get(companyCode=company_code)
    except CompanyCode.DoesNotExist:
        return Response({"error": "Invalid companyCode"}, status=status.HTTP_400_BAD_REQUEST)

    latest_impacts = RiskMatrixImpact.objects.filter(companyCode=company_code_instance, levelSetValue=level_set_value).order_by('-timestamp')[:10]
    serializer = RiskMatrixImpactSerializer(latest_impacts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
