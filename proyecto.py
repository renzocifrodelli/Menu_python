comboSimple= 5
comboDoble= 6
comboTriple=7
mcFlurby=2





print("Bienvenido a Hamburguesas IT" )

nombre_de_encargado=input("Ingrese su nombre encargad@ :")

pedidos= input(f"Hamburguesas IT\n Encargad@ -> {nombre_de_encargado} \n Recuerda, siempre hay que recibir al\n cliente con una sonrisa :)\n 1 – Ingreso nuevo pedido\n 2 – Cambio de turno\n 3 – Apagar sistema\n")

if pedidos == "1":
    input("Ingrese nombre del cliente: ")
    comboS=int(input("Ingrese cantidad Combo S : "))*comboSimple
    comboD=int(input("Ingrese cantidad Combo D: "))*comboDoble
    comboT=int(input("Ingrese cantidad Combo T: "))*comboTriple
    flurby=int(input("Ingrese cantidad Flurby: "))*mcFlurby

total= comboS+comboD+comboT+flurby
print(f"total ${total}")
abona= int(input("abona con $"))
cuenta= abona - total
Vuelto= (print(f"su vuelto es ${cuenta}\n ¿confirma pedido? Y/N?"))

if Vuelto == "Y" or "y":
    pedidos

