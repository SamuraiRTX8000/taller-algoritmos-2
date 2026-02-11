notas = [1.6,3.5,2.5,4.0,5.0]
notas2 = []

def ver_notas(notas):
    print("Mostrando notas...")
    for i,nota in enumerate(notas):
        
        print(f"Estudiante: {i} {nota}")


def modificar_notas(notas):
    menu = int(input("""Menu
                
            1.) Modificar nota
                
            2.) Agregar nuevas notas """))
    match menu:
        case 1:
            for i, nota in enumerate(notas):
                print(f"Estudiante: {i} {nota}")
            indice = int(input("ingrese el numero del estudiante que quiere modificar"))
    #asi se asegura de que no ponga un indice que no existe y len me dice cuantos elementos hay(indice y numero de elementos son diferentes)
            if 0 <= indice and indice <len(notas):
                nueva_nota = float(input("Ingresa la nueva nota(emtre 1.0 y 5.0)"))
                if nueva_nota >=1.0 and nueva_nota<=5.0:#asegura que las notas ingresadas esten dentro del rango establecido para cambiarlas
                    #modifica las notas seleccionadas
                    notas[indice] = nueva_nota
                else:
                    print("Nota no valida")
            else:
                print("Indice no valido")
        
        case 2:
            vueltas = int(input("ingrese cuatas notas quiere agregar a la lista "))
            for i in range(vueltas):#repite el ciclo el numero de veces que se necesite agregar una nota

                nueva_nota = float(input("Ingrese la nota que quiere agregar a la lista(entre 1.0 y 5.0)"))
                if nueva_nota >=1.0 and nueva_nota<=5.0:#asegura que las notas que se guarden sean validas
                    notas.append(nueva_nota)
                    print("se ha modificado la lista con exito")
                else:
                    print("Nota no valida")
            print("Lista modificada:")        
            for i, nota in enumerate(notas):
                print(f"Estudiante: {i} {nota} ")#muestra la lista modificada


def resumen_notas(notas):
    aprobados = 0
    reprobados = 0
    if len(notas) == 0:
        print("No hay notas para analizar.")
    
    else:

        for nota in notas:
            if nota >= 3.0:
                aprobados = aprobados +1
            else:
                reprobados = reprobados +1
        
        promedio = sum(notas)/ len(notas)
        porcentaje_aprob = (aprobados/ len(notas))*100
        porcentaje_reprob = (reprobados / len(notas))*100

        print(f"""Resumen de notas
            
            Aprobados: {aprobados}
            
            Reprobados: {reprobados}
            
            Promedio de la clase: {promedio}

            Porcentaje de aprobados: {porcentaje_aprob}

            Porcentaje de reprobados: {porcentaje_reprob}  """)
    


def crear_lista():
        notas2 = []

        vueltas = int(input("ingrese cuatas notas quiere agregar a la lista "))
        for i in range(vueltas):#
                print("La nota de estar entre 1.0 y 5.0")
                nueva_nota = float(input(f"Ingrese la nota: {i})"))
                if nueva_nota >=1.0 and nueva_nota<=5.0:#asegura que las notas que se guarden sean validas
                    notas2.append(nueva_nota)
                else:
                    print("Nota no valida")

        return notas2








play = True
while play == True:

    menu = int(input("""Calificaciones de grupo 1
                 
        1.) Ver notas.
        
        2.) Modificar lista
                 
        3.) Ver resumen.
                 
        4.) Crear nueva lista.
                 
        5.) Salir.
                 
        """))
    match menu:

        case 1:
            ver_notas(notas)

        case 2:
            modificar_notas(notas)

        case 3:
            resumen_notas(notas)

        case 4:
            notas = crear_lista()

