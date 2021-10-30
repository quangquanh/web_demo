from django.db import models
from django.db.models.aggregates import Count
# Create your models here.


class Product_type(models.Model):
    """lớp biểu diễn loại sản phẩm"""
    name = models.CharField(default="", max_length=256)  # tên loại sản phẩm
    description = models.TextField(default="")  # mô tả loại sản phẩm
    def __str__(self):
        return self.name # khi hiển thị class sẽ hiển thị ra tên 


class Product(models.Model):
    """lớp biểu diễn sản phẩm"""
    name = models.CharField( default="", max_length=1000)  # tên sản phẩm để mặc định là rỗng
    # mô tả sản phẩm dùng trường Text để biểu diễn
    description = models.TextField(default="")
    # chi tiết về sản phẩm
    detail = models.TextField(default="",max_length=10000)
    # biểu diễn sản phẩm có được đưa lên trình chiếu hay không
    active = models.BooleanField(default=False)
    value = models.IntegerField(default=0)  # giá tiền của sản phẩm
    # kết nối đến bảng loại sản phẩm và set sự kiện xóa
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE) # liên kết đến bảng loại sản phẩm
    img_avata = models.ImageField(null=True)
    def __str__(self):
        return self.name # khi hiển thị class sẽ hiển thị ra tên
#     lưu ý phải khai báo loại sản phẩm trước sản phẩm
class Picture(models.Model):
    """ lớp biểu diễn ảnh của sản phẩm"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # liên kết đến bảng sản phẩm
    picture = models.ImageField(null=True) # ảnh của sản phẩm được biểu diễn dưới trường ảnh
    def __str__(self):
        return self.picture.url # khi hiển thị class sẽ hiển thị ra đường dẫn
class Order(models.Model):
    """ lớp biểu diễn sự đặt hàng, đơn hàng """
    name_user = models.CharField(max_length=256,default="") # tên người đặt
    value = models.IntegerField(default=1) # tổng số tiền cần thanh toán
    count = models.IntegerField(default=1) # số lượng sản phẩm
    address = models.CharField(max_length=256) # địa chỉ người đặt
    phone_number = models.CharField(max_length=11) # số điện thoại người đặt hàng
    name_product = models.CharField(default="",max_length=1000) # tên sản phẩm 
    shipped = models.BooleanField(default=False) # trạng thái đã ship hay chưa
    def __str__(self):
        return  self.name_user + " / " + self.name_product +" / " + self.phone_number 