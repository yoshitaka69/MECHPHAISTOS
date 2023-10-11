from django.shortcuts import render
from .forms import FileUploadForm
from django.views.generic import FormView
import pandas as pd
from django.urls import reverse_lazy
from django.http import HttpResponse
import io

class FileUploadView(FormView):
   template_name = 'app/fileupload.html'
   form_class = FileUploadForm
   success_url = reverse_lazy('file-upload')

   def form_valid(self, form):
       # フォームから受け取ったデータをデータフレームへ変換
       # ファイル形式に応じた読み込み
       filetype = form.cleaned_data['FileType']
       file = io.TextIOWrapper(form.cleaned_data['file'])
       if filetype == 'csv':
           df = pd.read_csv(file, dtype=str)
       elif filetype == 'xlsx':
           df = pd.read_excel(file, dtype=str, index_col=0)

       # データフレームへの処理を記載
       # （今回は、postalCodeの先頭3桁を取り出した'pc_3dig'という列を追加）
       df['pc_3dig'] = df['postalCode'].str[:3]

       # ファイルの保存とダウンロード処理
       f_name = 'your_favourite_filename' # 日本語は使えない
       # ファイル形式に応じた保存とダウンロード処理
       if filetype == 'csv':
           response = HttpResponse(content_type='text/csv')
           response['Content-Disposition'] = 'attachment; filename ="' + f_name + '.csv"'
           df.to_csv(path_or_buf=response, sep=",", index=False, encoding="utf-8")
       elif filetype == 'xlsx':
           response = HttpResponse(content_type='application/vnd.ms-excel')
           response['Content-Disposition'] = 'attachment; filename ="' + f_name + '.xlsx"'
           df.to_excel(excel_writer=response, sheet_name="result", index=False)

       return response