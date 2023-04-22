from django.urls import include, path
from .views import index, signs, your_sign, type_index, type_list

urlpatterns = [
    path('', index, name="index"),
    path('types', type_index, name="type_index"),
    path('type/<str:type>', type_list, name="type_list"),

    path('your_sign', your_sign, name="your_sign"),
    path('<str:sign>', signs, name="signs"),
    # path('<int:month>/<int:day>', your_sign, name="your_sign"),

]
