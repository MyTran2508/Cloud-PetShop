from email.headerregistry import Address
from django import forms
import re
from django.contrib.auth.models import User
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from requests import request
from petshop.utils import *

class ContactForm(forms.Form):
    nametext = forms.CharField(label='Name', max_length=30)
    Subject = forms.CharField(label='Suject')
    Message = forms.CharField(label='Message')

    def contact(self,email):
        namet = self.cleaned_data['nametext']
        subt=self.cleaned_data['Subject']
        mst=self.cleaned_data['Message']
        
        gmail_user = 'baolocace111@gmail.com'
        gmail_password = 'godofstar123'
        sent_from  = to = gmail_user
        
        message = MIMEMultipart("alternative") 
        text="""<h3>&emsp;&emsp;&emsp;&emsp;&emsp;RESPOND FROM A CUSTOMER</h3>
                <p> <b>Name:</b> """+namet+'</p>'
        text+="""
                <p> <b>Email:</b> """+email+'</p>'
        text+="""
                <p> <b>Subject:</b> """+subt+'</p'
        text+="""
                <p> <b>Content:</b> """+mst+'</p>'
        part=MIMEText(text,"html")
        message.attach(part)
        if(True):
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)           
            server.sendmail(sent_from, to, message.as_string())
            server.close()

            print ('Email sent!')
        else:
            print("error")


class CheckoutForm(forms.Form):  
     FullName = forms.CharField(label='Full Name', max_length=30)
     Telephone = forms.CharField(label='Telephone', max_length=30)
     Address = forms.CharField(label='Delivery Address', max_length=100)
     
     
     def CheckOut(self, email,request):
        data = cartData(request)
        cartItems=data['cartItems']
        order=data['order']
        items=data['items']
        
        fname = self.cleaned_data['FullName']
        phone=self.cleaned_data['Telephone']
        address=self.cleaned_data['Address']
        
        gmail_user = 'zzs2harypoters2zz@gmail.com'
        gmail_password = 'ntagpcyafggdsuey'
        sent_from = gmail_user
        to = email
        
        message = MIMEMultipart("alternative")    
        html = """<h3>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ORDER DETAILS</h3> 
        <html>
                <body>
                <div class="table-content table-responsive">
                                <table>
                                <thead>
                                        <tr>
                                        <th>Product Name</th>
                                        <th>Unit Price</th>
                                        <th>Quantity</th>
                                        <th>Subtotal</th>
                                        </tr>
                                </thead>   
                                <tbody>"""                                                                    
                        
        for item in items:
                html+= '<tr>'+  '<td class="product-name"><a href="#">'+item.product.name+'</a></td>'
                html+= '<td class="product-price-cart"><span class="amount">&emsp;$'+ str(item.product.price) +'</span></td>'
                html+='<td class="product-quantity">'
                html+='&emsp;&emsp;<a href="#">'+str(item.quantity) +'</a></td>'
                html+='<td class="product-subtotal" id="subtotal">&emsp;$'+ str(item.get_total) +'</td>'
        html+='</tr> </tbody> <tfoot> <tr> <td colspan="0">Grand Total:</td> <td id="total" colspan="1">'
        html+='$'+ str(order.get_cart_total) + '</td> </tr>'                                                                                                               
        html+="""</tfoot>                        
                                </table>
                        </div>                                                   
                        </body>
                </html>"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        html+="""--------------------------------------------------------------------------------------------------            
                <p>    <b>Customer Name:</b> """+ fname +'      </p>'
        html+="""
                <p>    <b>Telephone:</b> """+ phone + '       </p>'
        html+="""
                <p>    <b>Delivery Address:</b> """ + address +'      </p>'
        html+="<h4>Đơn đặt hàng của quý khách đã được duyệt thành công. Chúng tôi sẽ giao đến từ 1-3 ngày. Xin cảm ơn quý khách!!!<h4>"
        part = MIMEText(html, "html")
        message.attach(part)
        
        if(True):
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)           
            server.sendmail(sent_from, to, message.as_string())
            server.close()

            print ('Email sent!')
        else:
            print("error")
        
        
        