import argparse
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas

class Invoice:
  def __init__(self, client_name, items, total_price):
    self.client_name = client_name
    self.items = items
    self.total_price = total_price

class Item:
  def __init__(self, name, quantity, price):
    self.name = name
    self.quantity = quantity
    self.price = price

def create_invoice(client_name, items, total_price):
  return Invoice(client_name, items, total_price)

def create_item(name, quantity, price):
  return Item(name, quantity, price)

def parse_items(items_str):
  items = []
  for item_str in items_str:
    name, quantity, price = item_str.split(',')
    quantity = int(quantity)
    price = float(price)
    items.append(create_item(name, quantity, price))
  return items

def save_invoice_to_pdf(invoice, filename):
  canvas = Canvas(filename, pagesize=A4)
  canvas.setFont("Helvetica", 12)

  # Add the invoice details to the PDF
  canvas.drawString(30, 750, "Invoice:")
  canvas.drawString(30, 735, f"Client: {invoice.client_name}")
  canvas.drawString(30, 720, "Items:")
  y = 705
  for item in invoice.items:
    canvas.drawString(30, y, f"  - {item.name} ({item.quantity} x ${item.price}) = ${item.quantity * item.price}")
    y -= 15
  canvas.drawString(30, y, f"Total: ${invoice.total_price}")

  # Save the PDF
  canvas.save()

def send_email(to, subject, filepath):
  # Get the login credentials
  print("Enter login credentials:")
    username = input("Username:")
        password = getpass.getpass()

  # Create the email message
  msg = MIMEMultipart()
msg['From'] = username
  msg['To'] = COMMASPACE.join([to])
  msg['Date'] = formatdate(localtime=True)
  msg['Subject'] = subject

  # Add the PDF attachment to the email
  with open(filepath, 'rb') as f:
    part = MIMEBase('application', 'octet-stream', Name=filepath)
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filepath)
    msg.attach(part)

  # Send the email
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(username, password)
  server.sendmail(username, to, msg.as_string())
  server.close()
  print("Receipt sent to email successfully!")


  

