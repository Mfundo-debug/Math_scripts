import argparse
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
    
def inv_pdf(invoice,filename):
    canvas = Canvas(filename,pagesize=A4)
    canvas.setFont("Helvetica", 12)
    
    
    #add the invoice details to the pdf
    
    canvas.drawString(30,750,"Invoice:")
    canvas.drawString(30, 735, f"Client: {invoice.client_name}")
    canvas.drawString(30, 720, "Items:")
    y = 705
    for item in invoice.items:
        canvas.drawString(30,y, f" - {item.name} ({item.quantity} x R{item.price}) = R{item.quantity * item.price}")
        y -= 15
        canvas.drawString(30,y, f"Total: R{invoice.total_price}")
        
        #save the pdf
        
        canvas.save()

parser = argparse.ArgumentParser()
parser.add_argument("client_name", type=str, help="the name of the client")
parser.add_argument("items", nargs='+', type = str, help ="the items on the invoice,in the format 'name,quantity,price'")
parser.add_argument("total_price", type= float, help = "the total price of the invoice")
parser.add_argument("filename", type=str, help="the name of the pdf file to save the invoice to")

args = parser.parse_args()
items = parse_items(args.items)
invoice = create_invoice(args.client_name, items, args.total_price)
inv_pdf(invoice, args.filename)