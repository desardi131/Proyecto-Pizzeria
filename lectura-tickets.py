import numpy as np
import pandas as pd

class Ticket():

    def __init__(self) -> None:
        self.nombre = nombre
        self.hora = hora
        self.precio = precio
        self.contenido = contenido
         
        
class TicketInvita(Ticket):

    def __init__(self) -> None:
        super().__init__()
        self.precio:float = 0.00

class TicketReparto(Ticket):

    def __init__(self) -> None:
        super().__init__()
        self.ruta = ruta
        self.telefono = telefono

class TicketRecoger(Ticket):

    def __init__(self) -> None:
        super().__init__()
        self.telefono = telefono