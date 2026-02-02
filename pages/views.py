from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import ContactForm, OrderForm
from .models import Category, Product, Order, OrderItem
from .cart import Cart

def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def menu(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'pages/menu.html', {'categories': categories})

def news(request):
    return render(request, 'pages/news.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/contact.html', {'success': True})
    return render(request, 'pages/contact.html')

from django.http import JsonResponse

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1:
            quantity = 1
    except ValueError:
        quantity = 1
    cart.add(product=product, quantity=quantity)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'cart_length': len(cart)})
        
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

from .forms import ContactForm, OrderForm
from .models import Category, Product, Order, OrderItem
# ... existing imports ...

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'pages/cart.html', {'cart': cart})

from django.core.mail import send_mail
from django.conf import settings

def checkout(request):
    cart = Cart(request)
    if not cart:
        return redirect('menu')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = cart.get_total_price()
            order.save()
            
            # Create Order Items
            order_items_text = ""
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                # Format for email
                price_formatted = "{:,}".format(int(item['price']))
                order_items_text += f"- {item['product'].name} (x{item['quantity']}): {price_formatted}đ\n"
            
            # Send Confirmation Email
            total_formatted = "{:,}".format(int(order.total_price))
            subject = f'Xác nhận đơn hàng #{order.id} - TNK Coffee'
            message = f'''Xin chào {order.name},

Cảm ơn bạn đã đặt hàng tại TNK Coffee. Đơn hàng của bạn đã được tiếp nhận.

Mã đơn hàng: #{order.id}
Tổng cộng: {total_formatted}đ

Chi tiết đơn hàng:
{order_items_text}

Ghi chú: {order.note or "Không có"}
Địa chỉ giao hàng: {order.address}
Số điện thoại: {order.phone}

Chúng tôi sẽ sớm liên hệ với bạn để giao hàng.

Trân trọng,
TNK Coffee Team
'''
            email_from = settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@tnkcoffee.com'
            recipient_list = [order.email, ]
            
            # Fail silently to avoid crashing if email backend fails (though console backend shouldn't)
            try:
                send_mail( subject, message, email_from, recipient_list )
            except Exception as e:
                print(f"Error sending email: {e}")

            cart.clear()
            return redirect('checkout_success', order_id=order.id)
    else:
        form = OrderForm()
        
    return render(request, 'pages/checkout.html', {'cart': cart, 'form': form})

def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'pages/checkout_success.html', {'order': order})
