import random

nombre = input("¿CUÁL ES SU NOMBRE USUARIO?\n")
nombre_upper = nombre.upper()
vida = 100
ataque = 12
objeto = False
esc_conf = True
solo_menu = True


print ("MUY BIEN, " + nombre_upper + " EMPECEMOS")

vida_enemigo = 70
daño = 10
botella_de_agua = 100

suerte1 = [1,1,1,2,1,1,1,2,2,2]
suerte2 = [1,1,1,2,1,1,1,2,1,1]
suerte3 = [1,1,1,2,1,2,1,2,1,1] 

def atacar(objetoA, vidaA, ataqueA):
    if objetoA == False:
        if vidaA >= ataqueA:
            vidaA -= ataqueA
            print("¡¡¡TOMA!!!")
            return vidaA
        if vidaA < ataqueA:
            print("EL PERRO ESTÁ MUY HERIDO")
            vidaA -= vidaA
            return vidaA
    if objetoA == True:
        if vidaA >= ataqueA:
            vidaA -= ataqueA + 6
            print("¡¡¡TOMA!!!")
            return vidaA
        if vidaA < ataqueA:
            vidaA -= vidaA
            print("EL PERRO ESTÁ MUY HERIDO")
            return vidaA

def movimientos_de_judo(vidaC):
    precision = random.choice(suerte1)
    while precision == 1:
        print("¿HUH? EL ATAQUE FALLÓ")
        vidaC = vidaC
        return vidaC
    else:
        if vidaC < 25:
            vidaC -= vidaC
            print("EL PERRO ESTÁ MUY HERIDO")
            print("AL ENEMIGO LE QUEDAN --------------------")
            print(0)
            print("-------------------- PUNTOS DE VIDA")
            return vidaC
        elif vidaC >= 25:
            vidaC -= 25
            print("AL ENEMIGO LE QUEDAN --------------------")
            print(vidaC)
            print("-------------------- PUNTOS DE VIDA")
            return vidaC

def piedra_invisible(esc_confirm):
    precision1 = random.choice(suerte3)
    if precision1 == 1:
        print("¿HUH? EL ATAQUE FALLÓ")
        esc_confirm = esc_conf
        return esc_confirm
    else:
        print("EL PERRO ESCAPÓ AULLANDO\n¡¡¡GANASTE!!!")
        esc_confirm = False
        return esc_confirm

def bate (objetoM):
    if objetoM == False:
            print("TE EQUIPASTE EL BATE")
            objetoM = True
            return objetoM
    if objetoM == True:
        print("YA TIENES EQUIPADO EL BATE, ¡ATACA!")
        return objetoM

def botella(vidaM):
    if vidaM <= 75:
        print("¡¡¡REFRESCANTE!!!\n¡RECUPERAS 25 DE VIDA!")
        vidaM += 25
        return vidaM
    elif vidaM == 100:
        print("VAYA DESPERDICIO...")
        vidaM = 100
        return vidaM
    else:
        vida_llena = 100 - vidaM
        print("BUENO...")
        print("---------- RECUPERAS ----------")
        print(vida_llena)
        print("---------- PUNTOS DE VIDA ----------")
        vidaM += vida_llena
        return vidaM
    

def escapar(esc_confirm):
    esc = random.choice(suerte2)
    if esc == 1:
        print("EL PERRO IMPIDIÓ TU ESCAPE")
        esc_confirm = True
        return esc_confirm
    if esc == 2:
        print("ESCAPASTE")
        esc_confirm = False
        return esc_confirm

print("-----------UN PERRO SALVAJE TE ATACÓ-----------\n")

while vida > 0 and vida_enemigo > 0 and esc_conf == True:
    print((str(nombre_upper)) + " --- PV " + str(vida))
    try:
        accion = int(input("¿QUÉ DESEAS HACER?\n1. ATACAR\n2. ATAQUE COMPUESTO\n3. MOCHILA\n4. ESCAPAR\n"))
        if accion > 0 and accion < 5:
            while accion == 1:
                solo_menu = True
                vida_enemigo = atacar(objeto, vida_enemigo, ataque)
                print("AL ENEMIGO LE QUEDAN --------------------")
                if vida_enemigo > 0:
                    print(vida_enemigo)
                    print("-------------------- PV")
                    break
                else:
                    print(0)
                    print("-------------------- PV")
                    break
            while accion == 2:
                eleccionA = int(input("LISTA DE ATAQUES COMPUESTOS:\n 1. MOVIMIENTO DE JUDO\n 2. PIEDRA INVISIBLE\n 3. SALIR\n"))
                solo_menu = True
                while eleccionA == 1:
                    vida_enemigo = movimientos_de_judo(vida_enemigo)
                    break
                while eleccionA == 2:
                    esc_conf = piedra_invisible(esc_conf)
                    eleccionA = 4
                while eleccionA == 3:
                    solo_menu = False
                    break
                else:
                    break
            while accion == 3:
                solo_menu = True
                eleccionB = int(input("ESTO HAY EN TU MOCHILA\n1. BATE\n2. BOTELLA DE AGUA\n3. SALIR\n"))
                if eleccionB == 1: 
                    objeto = bate(objeto)
                    break
                elif eleccionB == 2:
                    botella_de_agua -= 25
                    if botella_de_agua == 75:
                        vida = botella(vida)
                        print("LA BOTELLA ESTÁ MEDIO LLENA")
                        break
                    elif botella_de_agua == 50:
                        vida = botella(vida)
                        print("LA BOTELLA ESTÁ MEDIO VACÍA")
                        break
                    elif botella_de_agua == 25:
                        vida = botella(vida)
                        print("LA BOTELLA SE ESTÁ QUEDANDO VACÍA")
                        break
                    else:
                        print("LA BOTELLA SE QUEDÓ SIN AGUA")
                        print(":c")
                elif eleccionB == 3:
                    solo_menu = False
                    break
                else:
                    print("ESO NO ESTÁ EN TU MOCHILA")
            while accion == 4:
                solo_menu = True
                esc_conf = escapar(esc_conf)
                break
        else:
            print("ESE NÚMERO NO ESTÁ ENTRE LAS OPCIONES >:[")
            continue
        if vida <= 0:
            continue
        if esc_conf == False:
            continue
        if solo_menu == False:
            continue
        else:
            if vida_enemigo <= 0:
                continue
            else:
                print("EL PERRO ATACÓ\nHIZO 10 DE DAÑO")
                vida -= daño
    except (ValueError, TypeError):
        print("ESA OPCIÓN NO ESTÁ >:[")
else:
    if vida_enemigo <= 0:
        print("¡¡¡GANASTE!!!")
    elif vida <= 0:
        print("")
    else:
        print("")