from django.contrib import admin

# Register your models here.
from support.models import Faq, Inquiry, Category, Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    # 리스트 화면에서 보일 필드
    list_display = ('id', 'question', 'created_at', 'writer',)
    # 자동으로 갱신되어 수정할 수 없는 필드들 볼 수 있게
    readonly_fields = ('created_at', 'updated_at',)

# Inquiry 한 객체에 answer list가 들어갈 수 있도록 class 생성
class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변'
    readonly_fields = ('created_at', 'updated_at',)

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    # 리스트 화면에서 보일 필드
    list_display = ('id', 'content', 'created_at', 'writer',)
    # 자동으로 갱신되어 수정할 수 없는 필드들 볼 수 있게
    readonly_fields = ('created_at', 'updated_at',)

    inlines = [AnswerInline]

# 카테고리 class admin site에 등록
admin.site.register(Category)
