from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# urlpatterns = [
#     path('housing', views.housing_list)
# ]

urlpatterns = [
    path('housing/<str:state>/<str:city>/', views.Housing.as_view())
]

# allowed request to hit localhost/todos and localhost/todos.json
urlpatterns = format_suffix_patterns(urlpatterns)
