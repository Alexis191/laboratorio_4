class LibroDiario:
    '''Agrega transacciones e imprime los resultados'''

    def __init__(self):
        '''Constructor de la clase'''
        self.transacciones = []

    def agregar_datos(self, fecha, descripcion, monto, tipo):
        '''Esta función agrega los datos de la transacción'''

        self.transacciones.append({
            "Fecha": fecha,
            "Descripción": descripcion,
            "Monto": monto,
            "Tipo": tipo
        })

    def resumen(self):
        '''Función para calcular el total de ingreso y egresos'''

        ingresos = 0
        egresos = 0
        for t in self.transacciones:
            if t["Tipo"] == "ingreso":
                ingresos += t["Monto"]
            else:
                egresos += t["Monto"]
        return "Total Ingresos: " + str(ingresos) + " Total Egresos: " + str(egresos)
