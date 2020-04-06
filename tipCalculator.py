billAmount = float(input("What is the bill amount? "))
tipRate = float(input("What is the tip rate? "))

tip = billAmount * float(tipRate) / 100
total = billAmount + tip

print("Tip: $ {:.{}f}".format(tip, 2))
print("Total: $ {:.{}f}".format(total, 2))
