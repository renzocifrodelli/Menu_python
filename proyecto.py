import datetime


combos = {"comboSimple": 5,"comboDoble": 6 ,"comboTriple": 7 ,"mcFlurby":2}



while True:  
    print("Bienvenido a Hamburguesas IT" )
    turnoActivo=True
    ventasDelEncagardo=0
    
    nombre_de_encargado=input("Ingrese su nombre encargad@ :")
    
    archi2=open("registros.txt","a") 
    archi2.write(f"In,{datetime.datetime.now()} Encargade {nombre_de_encargado}\n")
    archi2.close()
    
    while turnoActivo:
        pedidos= input(f"""
                       Hamburguesas IT
                       Encargad@ -> {nombre_de_encargado} 
                       Recuerda, siempre hay que recibir al
                       cliente con una sonrisa :)
                       1 – Ingreso nuevo pedido
                       2 – Cambio de turno
                       3 – Apagar sistema
                       """)

        if pedidos == "1":
            nombre_cliente=input("Ingrese nombre del cliente: ")
            comboS=int(input("Ingrese cantidad Combo S : "))
            comboD=int(input("Ingrese cantidad Combo D: "))
            comboT=int(input("Ingrese cantidad Combo T: "))
            flurby=int(input("Ingrese cantidad Flurby: "))
            
            totalDelPedido= comboS*combos["comboSimple"]+comboD*combos["comboDoble"]+comboT*combos["comboTriple"]+flurby*combos["mcFlurby"]
            ventasDelEncagardo=totalDelPedido+ventasDelEncagardo
            print(f"total ${totalDelPedido}")
            
            abona= int(input("abona con $"))
            cuenta= abona - totalDelPedido
            print(f"su vuelto es ${cuenta}")
            confirma_pedido=input( "¿confirma pedido? Y/N?")

            if confirma_pedido == "Y" or confirma_pedido =="y":
                archi1=open("ventas.txt","a")                 
                archi1.write(f"{nombre_cliente},{datetime.datetime.now()},{comboS},{comboD},{comboT},{flurby},{totalDelPedido}\n ") 
                archi1.close() 

        if pedidos == "2":
            archi2=open("registros.txt","a") 
            archi2.write(f"Out,{datetime.datetime.now()} Encargade {nombre_de_encargado} ${ventasDelEncagardo}\n")
            archi2.write(f"############################################################################\n")
            archi2.close()
            turnoActivo=False
            
        