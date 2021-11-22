"""
    Se define toda la estructura del almacen y del sistema junto con las funciones necesarias
    para simular el sistema de ventas, almacen y tiendas
"""

##############################################################################################

# Se llaman las estructuras dinamicas, cola y pila, con sus respectivos metodos
from Estructuras_Dinamicas import *

##############################################################################################

# Primero es necesario cargar toda la informacion de los archivos, sobre todo
# aquellos que se piden en el trabajo explicitamente: Tiendas.txt y Consolas.txt

Almacen = [Pila() for i in range(0, 1000)] # Simula el almacen con pilas de 10 elementos
Solicitudes = Cola() # Solicitudes de compras, tomadas en Tiendas.txt
TiendasInformacion = Cola() # Informacion de las tiendas se toma de Tiendas_Info.txt
NuevasTiendasInformacion = Cola() # Cola util para guardar la informacion de las nuevas tiendas
VentasHoy = Cola() # Cola para almacenar las ventas del dia
NoExistencias = Cola() # Aqui se guarda las consolas que ya no hay en existencia

# Cargamos la informacion de Tiendas.txt
lines = []
with open('Tiendas.txt') as f:
    lines = f.readlines()
for line in lines:
    lineS = line.rstrip("\n").split('|')
    Solicitudes.agregar(lineS)

# Cargamos la informacion de Tiendas_Info.txt donde guardamos toda la informacion de tiendas
lines = []
with open('Tiendas_Info.txt') as f:
    lines = f.readlines()
for line in lines:
    lineS = line.rstrip("\n").split('|')
    TiendasInformacion.agregar(lineS)

# Cargamos el almacen en Pilas de 10 elementos
lines = []
with open('Consolas.txt') as f:
    lines = f.readlines()
i = 0
for line in lines:
    lineS = line.rstrip("\n").split('|')
    if Almacen[i].llena():
        i += 1
    Almacen[i].incluir(lineS)

##############################################################################################

# A continuacion tenemos todas las funciones que son necesarias para simular el sistema.

" Almacena una nueva consola dados los datos, `ConsolaDates`."
def AgregarConsola(ConsolaDates):
    for PilaConsolas in Almacen: # Se busca en las pilas 
        if PilaConsolas.llena():
            continue
        else: # Si tiene espacio, se almacena en esta
            PilaConsolas.incluir(ConsolaDates)
            break
    # Aqui verificamos si es que podemos cumplir con
    # alguna de las solicitudes
    i = 0
    for solicitud in Solicitudes:
        logic = ProcessPedidoCheck(solicitud)
        if logic:
            Solicitudes.eliminar(i)
        else: 
            i += 1

"Busca la consola con `Codigo` y regresa sus existencias en el almacen."
def BuscarConsolaCodigo(Codigo):
    count = 0
    consola_date = []
    for PilaConsolas in Almacen:
        for Consola in PilaConsolas:
            if Consola[0] == Codigo:
                count += 1
                consola_date.append(Consola)
    if count == 0:
        print("No existe codigo buscado")
    else:
        print(f'Existencias | Code | Nombre | Empresa')
        print(f' {count} | {consola_date[0][0]} | {consola_date[0][1]} | {consola_date[0][2]} ')

"Busca la consola con `Nombre` y regresa sus existencias en el almacen."
def BuscarConsolaNombre(Nombre):
    count = 0
    consola_date = []
    for PilaConsolas in Almacen:
        for Consola in PilaConsolas:
            if Consola[1] == Nombre:
                count += 1
                consola_date.append(Consola)
    if count == 0:
        print("No existe nombre buscado")
    else:
        print(f'Existencias | Code | Nombre | Empresa')
        print(f' {count} | {consola_date[0][0]} | {consola_date[0][1]} | {consola_date[0][2]} ')

"Busca las consolas de `Empresa` y regresa las existencias en el almacen."
def BuscarConsolaEmpresa(Empresa):
    count = []
    names_consola = []
    for PilaConsolas in Almacen:
        for Consola in PilaConsolas:
            if Consola[2] == Empresa:
                if Consola in names_consola:
                    for l in range(len(names_consola)):
                        if names_consola[l] == Consola:
                           count[l] += 1
                           break
                else:
                    count.append(1)
                    names_consola.append(Consola)
                
    if count == []:
        print("No existe empresa buscada")
    else:
        print(f'Existencias | Code | Nombre | Empresa')
        for l in range(len(names_consola)):
            print(f' {count[l]} | {names_consola[l][0]} | {names_consola[l][1]} | {names_consola[l][2]} ')

"Funcion principal para buscar consolas por Codigo, Nombre o Empresa."
def BuscarConsola(Num):
    if Num == 1:
        print("Ingrese codigo de consola: \n")
        codigo = input()
        BuscarConsolaCodigo(codigo)
    elif Num == 2:
        print("Ingrese nombre de consola: \n")
        Nombre = input()
        BuscarConsolaNombre(Nombre)
    elif Num == 3:
        print("Ingrese empresa de consola: \n")
        empresa = input()
        BuscarConsolaEmpresa(empresa)
    else: 
        print("Entrada erronea. Verifique menu.")

"""
    Dado el `RFC` busca la informacion de la tienda, en caso de no encontrarlo
    pide la informacion para agregarlo a la lista de tiendas.
    Posteriormente pide se ingresen los datos del pedido.
"""
def NuevoPedido(RFC):
    for Tienda in TiendasInformacion:
        if Tienda[-1] == RFC:
            print("Ingrese nombre de consola: \n")
            nombre = input()
            print("Ingrese empresa fabricante: \n")
            empresa = input()
            print("Ingrese empresa numero de piezas: \n")
            numero = input()
            ProcessPedido([Tienda[0], numero, nombre, empresa, Tienda[1], Tienda[2], RFC])
            return 0
    print("Informacion no encontrada, favor de ingresar datos")
    print("Ingrese nombre de tienda: \n")
    nombre_empresa = input()
    print("Ingrese telefono de tienda: \n")
    telefono_empresa = input()
    print("Ingrese correo de tienda: \n")
    correo_empresa = input()
    print("Ingrese pedido")
    print("Ingrese nombre de consola: \n")
    nombre = input()
    print("Ingrese empresa fabricante: \n")
    empresa = input()
    print("Ingrese numero de piezas: \n")
    numero = input()
    TiendasInformacion.agregar([nombre_empresa, telefono_empresa, correo_empresa, RFC])
    NuevasTiendasInformacion.agregar([nombre_empresa, telefono_empresa, correo_empresa, RFC])
    ProcessPedido([nombre_empresa, numero, nombre, empresa, telefono_empresa, correo_empresa, RFC])
    
"""
    Crea el recibo en ./recibos/recibo.txt de la compra realizada. Son necesarios los datos del 
    pedido `ArrayPedido` y el codigo de la consola `consola_codigo`.
"""
def create_recibo(ArrayPedido, consola_codigo):
    with open('recibos/recibo.txt', 'w') as f:
        f.write("Datos del comprador:")
        f.write('\n')
        f.write(f"Tienda: {ArrayPedido[0]} RFC: {ArrayPedido[-1]}")
        f.write('\n')
        f.write("Compra:")
        f.write('\n')
        f.write(f"Unidades | Codigo | Producto | Fabricante | Costo")
        f.write('\n')
        f.write(f"{ArrayPedido[1]} | {consola_codigo} | {ArrayPedido[2]} | {ArrayPedido[3]} | {ArrayPedido[1]}")

"""
    Dado los datos de un pedido `ArrayPedido`, verifica las existencais de la consola 
    y procede a realizar la compra o indica si no existen las suficientes existencias.
"""
def ProcessPedido(ArrayPedido):
    nombre_consola = ArrayPedido[2]
    count = 0
    # Busca las existencias en el Almacen
    for PilaConsolas in Almacen:
        for Consola in PilaConsolas:
            if Consola[1] == nombre_consola:
                count += 1
    # En caso de tener suficientes se procede a entregar pedido
    if count >= int(ArrayPedido[1]):
        count2 = 0
        for PilaConsolas in Almacen:
            i = -1
            for Consola in PilaConsolas:
                i += 1
                if count2 < int(ArrayPedido[1]):
                    # Se eliminan del almacen
                    if Consola[1] == nombre_consola:
                        PilaConsolas.extraer(i)
                        count2 += 1
                        consola_codigo = Consola[0]
                    else: 
                        continue
                else:
                    break
        # Crea recibo
        create_recibo(ArrayPedido, consola_codigo)
        print("Su recibo fue generado y guardado en ./recibos/")
        # Se guarda la venta
        VentasHoy.agregar([consola_codigo, ArrayPedido[1], nombre_consola, ArrayPedido[3]])
        # Verifica existencias restantes
        if (count == int(ArrayPedido[1])):
            NoExistencias.agregar([consola_codigo, nombre_consola])

    else:
        # En caso de no tener suficientes se notifica
        print(f"Su pedido no ha podido ser completado.")
        print(f"Hacen falta {int(ArrayPedido[1]) - count} unidades de {nombre_consola}.")
        print(f"Su solicitud sera colocada en espera, en cuanto lo tengamos sera despachada.")
        # Se guarda en solicitudes
        Solicitudes.agregar(ArrayPedido)

"""
    Dado los datos de un pedido `ArrayPedido`, verifica las existencais de la consola 
    y procede a realizar la compra o indica si no existen las suficientes existencias.
    Esta funcion es usada para checar el stock en todo momento y
    atender solicitudes.
"""
def ProcessPedidoCheck(ArrayPedido):
    nombre_consola = ArrayPedido[2]
    count = 0
    for PilaConsolas in Almacen:
        for Consola in PilaConsolas:
            if Consola[1] == nombre_consola:
                count += 1
    if count >= int(ArrayPedido[1]):
        count2 = 0
        for PilaConsolas in Almacen:
            i = -1
            for Consola in PilaConsolas:
                i += 1
                if count2 < int(ArrayPedido[1]):
                    if Consola[1] == nombre_consola:
                        PilaConsolas.extraer(i)
                        count2 += 1
                        consola_codigo = Consola[0]
                    else: 
                        continue
                else:
                    break
        create_recibo(ArrayPedido, consola_codigo)
        print("Una orden de Solicitudes.txt fue despachada, recibo en ./recibos/")
        VentasHoy.agregar([consola_codigo, ArrayPedido[1], nombre_consola, ArrayPedido[3]])
        if (count == int(ArrayPedido[1])):
            NoExistencias.agregar([consola_codigo, nombre_consola])
        return True

    else:
        return False

" Crea una nueva entrada para la informacion de una nueva tienda."
def Alta_nuevaTienda():
    print("Ingrese nombre de tienda: \n")
    nombre_empresa = input()
    print("Ingrese telefono de tienda: \n")
    telefono_empresa = input()
    print("Ingrese correo de tienda: \n")
    correo_empresa = input()
    print("Ingrese RFC: \n")
    RFC = input()
    TiendasInformacion.agregar([nombre_empresa, telefono_empresa, correo_empresa, RFC])
    NuevasTiendasInformacion.agregar([nombre_empresa, telefono_empresa, correo_empresa, RFC])

" Modifica informacion de una tienda ya registrada."
def ModificarTienda():
    print("Ingrese RFC de tienda: \n")
    RFC = input()
    i = 0
    check = False
    for Tienda in TiendasInformacion:
        if Tienda[-1] == RFC:
            TiendasInformacion.eliminar(i)
            check = True
            break
        i += 1
    if check:
        print("Ingrese nuevo nombre de tienda: \n")
        nombre_empresa = input()
        print("Ingrese nuevo telefono de tienda: \n")
        telefono_empresa = input()
        print("Ingrese nuevo correo de tienda: \n")
        correo_empresa = input()            
        TiendasInformacion.agregar([nombre_empresa, telefono_empresa, correo_empresa, RFC])
    else:
        print("RFC no se encontro")
 
# Funcion para salir del sistema
def salir_sistema():
    # Crea todos los archivos cargados al inicio.
    with open('Tiendas_Info.txt', 'w') as f:
        for Tiendas in TiendasInformacion:
            f.write(f"{Tiendas[0]}|{Tiendas[1]}|{Tiendas[2]}|{Tiendas[3]}")
            f.write('\n')
    with open('Consolas.txt', 'w') as f:
        for PilaConsolas in Almacen:
            for consola in PilaConsolas:
                f.write(f"{consola[0]}|{consola[1]}|{consola[2]}|{consola[3]}")
                f.write('\n')
    with open('Tiendas.txt', 'w') as f:
        for solicitud in Solicitudes:
            f.write(f"{solicitud[0]}|{solicitud[1]}|{solicitud[2]}|{solicitud[3]}|{solicitud[4]}|{solicitud[5]}|{solicitud[6]}")
            f.write('\n')
    # Crea el reporte de ventas
    print("El reporte de ventas se encuentra en ./reportes/VentasHoy.txt")
    with open('./reportes/VentasHoy.txt', 'w') as f:
        for venta in VentasHoy:
            f.write(f"{venta[0]}|{venta[1]}|{venta[2]}|{venta[3]}")
            f.write('\n')
    # Crea reporte de faltantes
    print("Las consolas de las cuales no se tiene existencia se encuentra en ./reportes/no_existencias.txt")
    with open('./reportes/no_existencias.txt', 'w') as f:
        for consola in NoExistencias:
            f.write(f"{consola[0]}|{consola[1]}")
            f.write('\n')
    # Crea el reporte de nuevas tiendas
    print("El reporte de nuevas tiendas agregadas se encuentra en ./reportes/Nuevas_Tiendas_Info.txt")
    with open('./reportes/Nuevas_Tiendas_Info.txt', 'w') as f:
        for Tiendas in NuevasTiendasInformacion:
            f.write(f"{Tiendas[0]}|{Tiendas[1]}|{Tiendas[2]}|{Tiendas[3]}")
            f.write('\n')

# Menu para aplicaciones
menu_options = {
    1: 'Ingresar nueva solicitud de compra',
    2: 'Almacenar nueva consola',
    3: 'Consultar existencias en almacen',
    4: 'Dar de alta nueva tienda',
    5: 'Modificar datos de tienda',
    6: 'Salir del sistema',
}

# Submenu para buscar consola
menu_options2 = {
    1: 'Buscar por codigo',
    2: 'Buscar por nombre',
    3: 'Buscar por empresa fabricante',
}

"Apoyo para crear menu de aplicacion."
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

if __name__=='__main__':
    # Genera menu de aplicacion
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Seleccione actividad: '))
        except:
            print('Entrada incorrecta. Verifique menu')
        #Check what choice was entered and act accordingly
        if option == 1:
            print("Ingrese RFC: \n")
            RFC = input()
            NuevoPedido(RFC)
            
            print("Presione enter: \n")
            none = input()
            print("\n")
        elif option == 2:
            print("Ingrese codigo de consola \n")
            codigo_con = input()
            print("Ingrese nombre de consola \n")
            codigo_nom = input()
            print("Ingrese empresa fabricante de consola \n")
            empresa_nom = input()
            print("Ingrese descripcion de consola \n")
            descripcion_nom = input()      
            AgregarConsola([codigo_con, codigo_nom, empresa_nom, descripcion_nom])      
            print("Presione enter: \n")
            none = input()
            print("\n")
        elif option == 3:
            for key in menu_options2.keys():
                print (key, '--', menu_options2[key] )
            option = int(input('Seleccione actividad: '))
            BuscarConsola(option)
            print("Presione enter: \n")
            none = input()
            print("\n")
        elif option == 4:
            Alta_nuevaTienda()
            print("Presione enter: \n")
            none = input()
            print("\n")
        elif option == 5:
            ModificarTienda()
            print("Presione enter: \n")
            none = input()
            print("\n")
        elif option == 6:
            print("Hasta la proxima")
            salir_sistema()
            exit()
        else:
            print('Operacion invalida. Verifique menu.')
            print("Presione enter: \n")
            none = input()
            print("\n")
