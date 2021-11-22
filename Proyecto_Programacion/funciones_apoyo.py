def AgregarConsola(ConsolaDates):
    for PilaConsolas in Almacen:
        if PilaConsolas.llena():
            continue
        else:
            PilaConsolas.incluir(ConsolaDates)
            break
    i = 0
    for solicitud in Solicitudes:
        logic = ProcessPedidoCheck(solicitud)
        if logic:
            Solicitudes.eliminar(i)
        else: 
            i += 1

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

def ProcessPedido(ArrayPedido):
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
        print("Su recibo fue generado y guardado en ./recibos/")
        VentasHoy.agregar([consola_codigo, ArrayPedido[1], nombre_consola, ArrayPedido[3]])
        if (count == int(ArrayPedido[1])):
            NoExistencias.agregar([consola_codigo, nombre_consola])

    else:
        print(f"Su pedido no ha podido ser completado.")
        print(f"Hacen falta {int(ArrayPedido[1]) - count} unidades de {nombre_consola}.")
        print(f"Su solicitud sera colocada en espera, en cuanto lo tengamos sera despachada.")
        Solicitudes.agregar(ArrayPedido)

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
        print("RFC no se encoentro")
 
def salir_sistema():
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
    print("El reporte de ventas se encuentra en ./reportes/VentasHoy.txt")
    with open('./reportes/VentasHoy.txt', 'w') as f:
        for venta in VentasHoy:
            f.write(f"{venta[0]}|{venta[1]}|{venta[2]}|{venta[3]}")
            f.write('\n')
    print("Las consolas de las cuales no se tiene existencia se encuentra en ./reportes/no_existencias.txt")
    with open('./reportes/no_existencias.txt', 'w') as f:
        for consola in NoExistencias:
            f.write(f"{consola[0]}|{consola[1]}")
            f.write('\n')
    print("El reporte de nuevas tiendas agregadas se encuentra en ./reportes/Nuevas_Tiendas_Info.txt")
    with open('./reportes/Nuevas_Tiendas_Info.txt', 'w') as f:
        for Tiendas in NuevasTiendasInformacion:
            f.write(f"{Tiendas[0]}|{Tiendas[1]}|{Tiendas[2]}|{Tiendas[3]}")
            f.write('\n')