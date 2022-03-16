from django.db import models
from django.urls import reverse

class Post(models.Model):
    message = models.TextField()
    # photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    # auto_now_add=True 데이터가 생성될 때의 시각이 자동적으로 입력됨
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True 데이터가 수정될 때의 시각이 자동적으로 입력됨
    updated_at = models.DateTimeField(auto_now=True)
    
    # Java의 toString
    def __str__(self):
        return self.message
        # return f"Custom Post object({self.id})"
        # return "Custom Post object({})".format(self.id)
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_dsecription = '메세지 글자수'
    
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])