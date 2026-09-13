# SKU Generation
from pyscript import display, document

def skugeneration(e):
    document.getElementById('result2').innerHTML = " "

    # Variables
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_quantity = document.getElementById("stock_quantity").value

    category = category[:3].upper()
    product_name = product_name[:3].upper()

    sku = category + "-" + product_name + "-" + stock_quantity

    # Displaying the Output
    display(f'The sku is {sku}', target='result2')
