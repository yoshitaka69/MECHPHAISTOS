from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Max

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        sent_test_nos = [item.get('testNo') for item in data if item.get('testNo') is not None]

        # 現在のデータベースに存在するtestNoを取得
        existing_test_nos = list(Product.objects.values_list('testNo', flat=True))

        # 削除する必要があるtestNoを特定
        test_nos_to_delete = set(existing_test_nos) - set(sent_test_nos)

        # 削除処理
        if test_nos_to_delete:
            Product.objects.filter(testNo__in=test_nos_to_delete).delete()

        # 新規作成または更新の処理
        created_items = []
        for item in data:
            test_no = item.get('testNo')

            if test_no is not None:
                # testNoが存在する場合、既存のレコードを更新する
                existing_item = Product.objects.filter(testNo=test_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # testNoがnullまたは新規作成の場合
            if test_no is None:
                # 最大のtestNoを取得し、そこから次の番号を割り当てる
                max_test_no = Product.objects.aggregate(Max('testNo'))['testNo__max'] or 0
                item['testNo'] = max_test_no + 1

            serializer = self.get_serializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_items.append(serializer.data)

        return Response(created_items, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        test_no = request.data.get('testNo')
        if test_no:
            try:
                # testNoに基づいて既存の製品を取得し、削除を試みる
                product = Product.objects.get(testNo=test_no)
                self.perform_destroy(product)
                print("Delete request received with testNo:", test_no)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Product.DoesNotExist:
                return Response({"error": "Product with testNo not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "testNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # 新規作成時の追加処理が必要な場合はここで行う
        serializer.save()

    def perform_update(self, serializer):
        # 更新時の追加処理が必要な場合はここで行う
        serializer.save()

    def perform_destroy(self, instance):
        # 削除時の追加処理が必要な場合はここで行う
        instance.delete()
