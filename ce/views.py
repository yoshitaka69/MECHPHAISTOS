from django.views.generic import ListView
from . import models

class CeList(ListView):
    # Companyテーブル連携
    model = models.Ce
    # レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "Ce_list"
    # テンプレートファイル連携
    template_name = "Ce_list.html"