import argparse
import openpyxl

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
    
#def generate_invoice(invoice):
 #   print("Invoice:")
  ## print("Items:")
   # for item in invoice.items:
    #    print(f" - {item.name} ({item.quantity} x R{item.price}) = R{item.quantity * item.price}")
    #print(f"Total: R{invoice.total_price}")
            
#def generate_receipt(invoice):
 #   print("Receipt:")
  #  print(f"Client: {invoice.client_name}")
   # print("items:")
    #for item in invoice.items:
     #   print(f" - {item.name} ({item.quantity} x R{item.price}) = R{item.quantity * item.price}")
    #print(f"Total: R{invoice.total_price}")
        
        
def parse_items(items_str):
    items = []
    for item_str in items_str:
        name, quantity, price = item_str.split(',')
        quantity = int(quantity)
        price = float(price)
        items.append(create_item(name, quantity, price))
        return items
    
def inv_excel(invoice,filename):
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    #add the invoice details to the sheet
    sheet['A1'] = "Invoice"
    sheet['A2'] = f"Client: {invoice.client_name}"
    sheet['A3'] = "Items:"
    row = 4
    for item in invoice.items:
        sheet[f'A{row}'] = f" - {item.name} ({item.quantity} x R{item.price}) = R{item.quantity * item.price}"
        row += 1
    sheet[f'A{row}'] = f"Total: R{invoice.total_price}"
    
    #save the workbook
    wb.save(filename)

parser = argparse.ArgumentParser()
parser.add_argument("client_name", type=str, help="the name of the client")
parser.add_argument("items", nargs='+', type = str, help ="the items on the invoice,in the format 'name,quantity,price'")
parser.add_argument("total_price", type= float, help = "the total price of the invoice")
parser.add_argument("filename", type=str, help="the name of the excel file to save the invoice to")

args = parser.parse_args()
items = parse_items(args.items)
invoice = create_invoice(args.client_name, items, args.total_price)
#generate_invoice(invoice)
#generate_receipt(invoice)
    #save the invoice to the excel sfile
inv_excel(invoice,args.filename)
