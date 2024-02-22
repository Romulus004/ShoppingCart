run = True
count = 1
listForAll = []

atot = 0
name = input("Enter the product name: ")
item = int(input("Enter the item: "))
price = int(input("Enter the price: "))
x = input("To keep shopping enter '1', to stop shopping enter '0' : ")
subTot = item*price
ToT = subTot
listForAll.append(f"       {name:<7}             {item:<5}             {price:<6}            {subTot:<8}      ")


while run:
    if x == '1':
        name = input("\nEnter the product name: ")
        item = int(input("Enter the item: "))
        price = int(input("Enter the price: "))
        subTot = item*price
        x = input("To keep shopping enter '1', to stop shopping enter '0' : ")
        count += 1
        ToT += subTot
        listForAll.append(f"       {name:<7}             {item:<5}             {price:<6}            {subTot:<8}      ")

    elif x == '0':
        sen = f"\n{'='*25}Thank you for shopping with us <3{'='*25}\n"
        print(f"{sen}\n       PRODUCT             ITEMS            PRICES             SUBTOTAL        ")

        for i in listForAll:
                print(i)

        print(f"\n{'='*len(sen)} \nTotal amount is {ToT}.")
        run = False