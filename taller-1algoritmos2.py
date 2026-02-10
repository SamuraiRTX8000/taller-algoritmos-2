notas = [1.6,3.5,2.5,4.0,5.0]

def ver_notas(notas):
    for i,nota in enumerate(notas):
        print("Mostrando notas...")
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
    #asi se asegura de que no ponga un indice que no existe y len medice cuantos elementos hay(indice y numero de elementos son diferentes)
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

                







menu = int(input("""Calificaciones de grupo 1
                 
        1.) Ver notas.
        
        2.) Modificar lista
                 
        3.) Ver resumen.
                 
        4.) Crear nueva lista.
                 
        5.) Salir.
                 
        """))

