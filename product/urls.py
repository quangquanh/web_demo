from django.urls import path
from . import views
app_name = "product" # set tên app để phân biệt đường dẫn đến các app khác
urlpatterns = [
    path('', views.Index.as_view(),name="home"),# đường dẫn đến trang chủ
    path("product/<int:product_id>",views.View_product.as_view(),name="view_product"),# đường dẫn đến sản phẩm
    # khi click vào đường dẫn này thì django sẽ truyền vào product_id id của sản phẩm đang chứa đường dẫn
    path("type/<int:type_id>",views.view_type,name="view_type"), # đường dẫn đến loại sản phẩm
    # khi click vào đường dẫn này thì django sẽ truyền vào type_id id của loại hàng đang chứa đường dẫn
    path("search/",views.Search.as_view(),name="search") # đường dẫn đến trang tìm kiếm
]