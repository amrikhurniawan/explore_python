a = "UDDUUUDDU"
b = list(a)
c = b
print (c)

if (c[0] == "D" and c[-1] == "D"):
    print("1 Gunung D")

elif (c[0] == "U" and c[-1] == "U"):
    print("1 Gunung U")

else:
    print("2 Gunung")