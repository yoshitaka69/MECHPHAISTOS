from .models import SafetyIndicators, NearMiss,ActionItems


def calculate_and_update_rate_of_level_a(company_code):
    # 特定の companyCode に関連する NearMiss インスタンスの総数
    total_near_miss = NearMiss.objects.filter(companyCode=company_code).count()
    
    if total_near_miss > 0:
        # 'A' の値を含む NearMiss インスタンスの数
        level_a_count = NearMiss.objects.filter(companyCode=company_code, measures__contains='A').count()
        
        # リスクレベルAの割合を計算
        rate_of_level_a = (level_a_count / total_near_miss) * 100
    else:
        rate_of_level_a = 0
    
    # SafetyIndicator インスタンスの取得・更新
    indicator, created = SafetyIndicator.objects.get_or_create(companyCode=company_code)
    indicator.rateOflevelA = rate_of_level_a
    indicator.save()


def update_safety_indicator(company_code):
    indicator, created = SafetyIndicators.objects.get_or_create(companyCode=company_code)
    total_near_miss_count = NearMiss.objects.filter(companyCode=company_code).count()
    indicator.totalOfNearMiss = total_near_miss_count
    indicator.save()


def calculate_and_update_rate_of_action_items(company_code):
    # 対策アクションアイテムの合計数と解決済み数を取得
    total_action_items = ActionItems.objects.filter(companyCode=company_code).count()
    solved_action_items = ActionItems.objects.filter(companyCode=company_code, is_solved=True).count()
    
    if total_action_items > 0:
        rate_of_action_items = (solved_action_items / total_action_items) * 100
    else:
        rate_of_action_items = 0
    
    # SafetyIndicator インスタンスの取得・更新
    indicator, created = SafetyIndicator.objects.get_or_create(companyCode=company_code)
    indicator.rateOfActionItems = rate_of_action_items
    indicator.save()
