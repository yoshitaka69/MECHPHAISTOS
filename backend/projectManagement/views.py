from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ProjectManagement
from .serializers import ProjectManagementSerializer
from accounts.models import CompanyCode


class ProjectManagementViewSet(viewsets.ModelViewSet):
    queryset = ProjectManagement.objects.all()
    serializer_class = ProjectManagementSerializer

    def create(self, request, *args, **kwargs):
        # リクエストデータのコピーを作成して、イミュータブル問題を回避
        data = request.data.copy()
        
        company_code_str = data.get('companyCode')
        
        try:
            # 会社コードを取得してプライマリキーに変換
            company_code = CompanyCode.objects.get(companyCode=company_code_str)
            data['companyCode'] = company_code.pk  # プライマリキーに変換してセット
        except CompanyCode.DoesNotExist:
            return Response({'error': 'Invalid company code'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # PATCHリクエストなら部分更新
        instance = self.get_object()
        data = request.data

        # companyCodeを処理
        company_code_str = data.get('companyCode')
        if company_code_str:
            try:
                # companyCodeをプライマリキーに変換
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                data['companyCode'] = company_code_obj.id
            except CompanyCode.DoesNotExist:
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # シリアライザでバリデーションと更新を実行
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_create(self, serializer):
        try:
            # データを保存 (新規作成)
            project = serializer.save()
            print(f"Successfully created project: {project}")
            return project
        except Exception as e:
            print(f"Error during serializer.save(): {e}")
            raise e

    def perform_update(self, serializer):
        try:
            # データを保存 (更新)
            project = serializer.save()
            print(f"Successfully updated project: {project}")
            return project
        except Exception as e:
            print(f"Error during serializer.save(): {e}")
            raise e


