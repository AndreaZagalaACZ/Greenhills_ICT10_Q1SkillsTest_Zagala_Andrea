# Receipt Calculation
from pyscript import display, document

def menuorder(e):
    document.getElementById('result').innerHTML = " "
    americano = document.getElementById("order1")
    spanish_latte = document.getElementById("order2")
    strawberry_frappe = document.getElementById("order3")
    affogato = document.getElementById("order4")
    caramel_macchiato = document.getElementById("order5")

    subtotal += float(americano.value) * americano.checked
    subtotal += float(spanish_latte.value) * spanish_latte.checked
    subtotal += float(strawberry_frappe.value) * strawberry_frappe.checked
    subtotal += float(affogato.value) * affogato.checked
    subtotal += float(caramel_macchiato.value) * caramel_macchiato.checked

    tax = subtotal * 0.12
    total = subtotal + tax
    
    display(f'The subtotal is {subtotal} PHP. The tax is {tax} PHP. The total is {total} PHP. ', target='result')
