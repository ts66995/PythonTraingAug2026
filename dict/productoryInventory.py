inventory={
    "Laptop":20,
    "Mouse":25,
    "Keyboard":15
}
productNameEntered=input("Enter product name: ")

for prName,quantity in inventory.items():
    if prName.lower()==productNameEntered.lower():
        print(f"{productNameEntered} is available")
        print(f"Quantity: {quantity}")
        quantityEntered=int(input("Enter product quantity to purchase: "))
        if quantity>=quantityEntered:
            print("Order can be processed")
        else:
            print("Insufficient stock")
        break;
else:
    print("Product not available")
