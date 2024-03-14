
#RepairingCostの1月12月までの合計
def calculate_total_cost(instance):
    return sum(getattr(instance, month, 0) or 0 for month in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment'])

