from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

# admin 페이지에서 앱을 보고 싶다면 등록하는 과정이 필요

# 등록법1 / 기본 ModelsAdmin으로 동작
# admin.site.register(Post)

# # 등록법2 / 지정한 ModelAdmin으로 동작
# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

# 등록법3 / Wrapping
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message', 'is_public','message_length', 'created_at', 'updated_at']
    list_display_links = ['message'] # message에 링크가 걸림
    search_fields = ['message']
    list_filter = ['created_at', 'is_public']
    
    def message_length(self, post):
        return f"{len(post.message)} 글자"
        # return len(post.message)
    