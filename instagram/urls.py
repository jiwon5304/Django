from django.urls import path, re_path, register_converter
from .converters import YearConverter, MonthConverter, DayConverter
from . import views

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'  # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),
    
    # path('archives/<int:year>/', views.archives_year),
    
    # r은 ROW의 약자로 \을 자동
    # re_path('archives/(?P<year>\\d+)/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
]