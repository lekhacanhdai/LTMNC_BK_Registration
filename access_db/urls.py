from django.urls import path, include
from .views import (
    TermView, HocPhanView, ClearCache, LoadData, MultiConnect
)

urlpatterns = [
    path('api', TermView.as_view()),
    path('terms', HocPhanView.as_view()),
    path('clean-cache', ClearCache.as_view({"delete": "cleanCache"})),
    path("load-data", LoadData.as_view({"get": "loadData"})),
    path('get-term', LoadData.as_view({'get': 'getTerm'})),
    path('student-connect', MultiConnect.as_view({'put': 'connectDB'})),
    path('connect-redis', MultiConnect.as_view({'put': 'connectRedis'}))
]


