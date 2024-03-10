from django.contrib import admin

from .models import Question

# Questionモデルを管理サイトに登録
admin.site.register(Question)

# Register your models here.
