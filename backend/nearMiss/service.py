from .models import SafetyIndicator, NearMiss

def update_safety_indicator(company_code):
    indicator, created = SafetyIndicator.objects.get_or_create(companyCode=company_code)
    total_near_miss_count = NearMiss.objects.filter(companyCode=company_code).count()
    indicator.totalOfNearMiss = total_near_miss_count
    indicator.save()
