from django import forms
from .models import Contact, Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Họ tên người nhận', 'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Email (để nhận thông báo)', 'style': 'height: 55px;'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Số điện thoại', 'style': 'height: 55px;'}),
            'address': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Địa chỉ giao hàng chi tiết', 'style': 'height: 55px;'}),
            'note': forms.Textarea(attrs={'class': 'form-control bg-light border-0 px-4 py-3', 'placeholder': 'Ghi chú thêm (ví dụ: Giao giờ hành chính...)', 'rows': 4}),
        }
