from django import forms
from django.forms import widgets
from .models import Order
# đây là file chứa các form
class OrderForm(forms.ModelForm):
    """ class biểu diễn form đặt hàng"""
    class Meta:
        model = Order # gán đối tượng cho form
        fields = ("name_user","address","phone_number","count") # tupple các trường được biểu diễn ra
        # chỉnh dao diện cho các forms
        widgets = {"name_user": forms.TextInput(attrs={"class":"form-control form-control-sm"}),
                    "address": forms.TextInput(attrs={"class":"form-control form-control-sm"}),
                    "phone_number": forms.TextInput(attrs={"class":"form-control form-control-sm"}),
                    "count": forms.NumberInput(attrs={"class":"form-control form-control-sm"})
                    }