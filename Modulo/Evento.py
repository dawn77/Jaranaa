class Evento:
    def __init__(self, id, cliente, fecha, servicios, impuestos, estado, total):
        self.id = id
        self.cliente = cliente
        self.fecha = fecha
        self.servicios = servicios
        self.impuestos = impuestos
        self.estado = estado
        self.total = total

#Impuestos Monto = IVA + Gastos administrativos
