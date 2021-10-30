from django import views
from django.db import models
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from .forms import OrderForm
from .models import Order, Product,Product_type
# Create your views here.
class Index(View):
    """ class hiển thị trang chủ """
    def get(self,request):
        """hàm hiển thị""" 
        pros = Product.objects.all() # tạo danh sách chứa toàn bộ sản phẩm
        sliders = [] # tạo 1 danh sách để chiếu trên slider
        prosduct_types = Product_type.objects.all() # tạo danh sách loại sản phẩm
        for i in pros: 
            if i.active: sliders.append(i) # lặp trong toàn bộ sản phẩm nếu được chiếu trên slider thì thêm vào
        first = sliders.pop() # lấy sản phẩm được chiếu trên slider đầu tiên
        # trả về trang template thị sản phẩm và truyền vào đó dic chứa sản phẩm,sliders,loại sản phẩm
        return render(request,"product/index.html",{"pros":pros,"sliders": sliders,"first":first,"product_types":prosduct_types})
class View_product(View):
    """class chứa trang hiển thị sản phẩm"""
    def get(self,request,product_id):
        p = Product.objects.get(pk=product_id)  # lấy sản phẩm theo key truyền vào từ đường dẫn
        f = OrderForm() # tạo 1 form đặt hàng để cho khách hàng có thể đặt hàng
        return render(request,"product/view_product.html",{"pro":p,"f":f})
        # trả về template hiển thị sản phầm và truyền vào đó dic chứa sản phẩm
        #  key của đối tượng sẽ biểu diễn cho đối tượng đó trong template 
    def post(self,request,product_id):
        """ hàm bắt sự kiện và xử lý khi khách hàng điền form đặt hàng và gửi"""
        product = Product.objects.get(pk = product_id) # lấy đối tượng sản phẩm được đặt
        orderform = OrderForm(request.POST) # lấy đối tượng form theo phản hồi từ người dùng trả về
        order = Order() # tạo đối tượng đơn đặt hàng để lưu về database
        if orderform.is_valid(): # nếu form trả về đúng định dạng
            order.name_product = product.name # lấy tên sản phẩm được đặt
            order.name_user = request.POST["name_user"] # lấy tên người đặt
            order.address = request.POST["address"] # lấy địa chỉ người đặt
            order.phone_number = request.POST["phone_number"] # lấy số điện thoại người đặt
            order.count = request.POST["count"] # lấy số lượng sản phẩm được đặt
            if(int(order.count) <= 0): return HttpResponse("vui lòng nhập số lượng lớn hơn 0") 
            # xử lý khi người đặt nhập số hàng nhỏ hơn 0
            order.value = int(request.POST["count"])*product.value # tính số tiền mà người đặt cần trả
            order.save() # lưu đơn hàng vào database
            return render(request,"product/view_pay.html",{"order":order}) 
            # trả về trang hiển thị đặt hàng thành công
        else: 
            return HttpResponse("bạn nhập sai định dạng") 
            # nếu không đúng định dạng thì truyền thông báo đến người dùng 
class Search(View):
    """ class xử lý tìm kiếm """
    def get(self,request): 
        """ hàm hiển thị trang tìm kiếm"""
        return render(request,"product/search.html")
    def post(self,request): 
        """hàm xử lý tìm kiếm"""
        search = request.POST['search'] # lấy phản hồi của người dùng từ search bar
        pros = Product.objects.filter(name__contains=search) # lấy danh sách sản phẩm được lọc ra từ database
        return render(request,"product/search.html",{"search":search,"pros":pros})
        # trả lại danh sách sản phẩm tìm được
def view_type(request,type_id):
    pro_type = Product_type.objects.get(pk= type_id) # lấy loại sản phẩm theo id của sản phẩm được chọn
    pros = pro_type.product_set.all() # lấy danh sách sản phầm thuộc loại sản phẩm đó
    return render(request,"product/view_type.html",{"pro_type":pro_type,"pros":pros})
    # trả về trang hiển thị danh sách sản phẩm thuộc loại sản phẩm đó 

