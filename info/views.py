from django.shortcuts import render
from .models import Person, Contact
from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "",
        "Sitemap: https://www.emertatfarabar.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
def sitemap_xml(request):
    english_urls = [
        "/",
        "/about/",
        "/team/",
        "/why/",
        "/contact/",
        "/price-inquiry/",
        "/services/road-freight/",
        "/services/sea-freight/",
        "/services/rail-freight/",
        "/services/multimodal-transport/",
        "/services/customs-clearance/",
    ]

    persian_urls = [
        "/fa/",
        "/fa/about/",
        "/fa/team/",
        "/fa/why/",
        "/fa/contact/",
        "/fa/price-inquiry/",
        "/fa/services/road-freight/",
        "/fa/services/sea-freight/",
        "/fa/services/rail-freight/",
        "/fa/services/multimodal-transport/",
        "/fa/services/customs-clearance/",
    ]

    urls = english_urls + persian_urls

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append(
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    )

    for url in urls:
        xml.append(
            f"<url><loc>https://www.emertatfarabar.com{url}</loc></url>"
        )

    xml.append("</urlset>")

    return HttpResponse(
        "\n".join(xml),
        content_type="application/xml"
    )    
def home(request):
    return render(request, 'info/home.html')

def road_freight(request):
    return render(request, 'info/road_freight.html')

def sea_freight(request):
    return render(request, 'info/sea_freight.html')

def rail_freight(request):
    return render(request, 'info/rail_freight.html')
def multimodal_transport(request):
    return render(request, 'info/multimodal_transport.html') 
def customs_clearance(request):
    return render(request, 'info/customs_clearance.html')    

def about(request):
    return render(request, 'info/about.html')

def contact(request):
    return render(request, 'info/contact.html')

from django.db.utils import OperationalError

def team(request):
    return render(request, 'info/team.html')

def why(request):
    return render(request, 'info/why.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages  # Import Django's messages framework

def price_inquiry(request):
    if request.method == 'POST':
        # Collect form data
        fullname = request.POST.get('fullname')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact_method = request.POST.get('contactMethod')
        
        type_of_goods = request.POST.get('type_of_goods')
        goods_description = request.POST.get('goods_description')
        total_weight = request.POST.get('total_weight')
        dimensions = request.POST.get('dimensions')
        num_packages = request.POST.get('num_packages')
        cargo_value = request.POST.get('cargo_value')
        special_handling = request.POST.get('special_handling')
        
        pickup_location = request.POST.get('pickup_location')
        delivery_location = request.POST.get('delivery_location')
        shipping_method = request.POST.get('shipping_method')
        comments = request.POST.get('comments')
        
        # Optional server-side validation for required fields:
        is_fa = request.path.startswith('/fa/')

        if not (fullname and company and email and phone and contact_method):
            error_message = (
                "خطا: لطفاً همه فیلدهای الزامی اطلاعات تماس را تکمیل کنید."
                if is_fa
                else "Error: Please fill out all required contact fields."
            )
            return HttpResponse(error_message, status=400)
        
        # Build the email message
        message_body = f"""
        New Price Inquiry Submission:
        
        --- Contact Information ---
        Full Name: {fullname}
        Company: {company}
        Email: {email}
        Phone: {phone}
        Preferred Contact Method: {contact_method}
        
        --- Shipment Details ---
        Type of Goods: {type_of_goods}
        Description of Goods: {goods_description}
        Total Weight (kg): {total_weight}
        Dimensions: {dimensions}
        Number of Packages: {num_packages}
        Cargo Value: {cargo_value}
        Special Handling Requirements: {special_handling}
        
        --- Transportation Details ---
        Pickup Location: {pickup_location}
        Delivery Location: {delivery_location}
        Preferred Shipping Method: {shipping_method}
        Additional Comments: {comments}
        """
        
        # Send the email
        send_mail(
            subject="New Price Inquiry",
            message=message_body,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Make sure this is configured
            recipient_list=["social.emertatfarabar@gmail.com"],
        )
        
        # Use Django messages to show success once
        success_message = (
            "درخواست شما با موفقیت ارسال شد."
            if is_fa
            else "Your request has been sent successfully!"
        )
        messages.success(request, success_message)

        return redirect('/fa/price-inquiry/' if is_fa else '/price-inquiry/')
    
    # If GET, show the form
    return render(request, 'info/price_inquiry.html')
