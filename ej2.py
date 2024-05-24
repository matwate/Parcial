# Numero de asientos disponibles en el sistema de boletos
NUM_SEATS = 500

# La clase TicketSystem representa un sistema de boletos.
class TicketSystem:

    # El método __init__ inicializa una nueva instancia de la clase.
    # num_seats es el número de asientos disponibles en el sistema.
    def __init__(self, num_seats: int):
        self.num_seats = num_seats  # Número de asientos disponibles.
        self.tickets = []  # Lista de boletos vendidos.
        self.returned_tickets = []  # Lista de boletos devueltos.

    # El método has_tickets verifica si hay boletos disponibles.
    # Devuelve True si el número de boletos vendidos es menor que el número de asientos disponibles, False en caso contrario.
    def has_tickets(self) -> bool:
        return len(self.tickets) < self.num_seats
    
    # El método next_ticket devuelve el próximo boleto disponible.
    # Si hay boletos devueltos, devuelve el primero de ellos.
    # Si no hay boletos devueltos pero hay boletos vendidos, devuelve el primero de ellos.
    # Si no hay boletos disponibles, devuelve -1.
    def next_ticket(self) -> int:
        if self.returned_tickets:
            return self.returned_tickets.pop(0)
        if self.tickets:
            return self.tickets.pop(0)
        return -1

    # El método return_ticket permite devolver un boleto al sistema.
    # Si el boleto ya está en la lista de boletos vendidos, no hace nada.
    # Si el boleto no está en la lista de boletos vendidos, lo añade a la lista de boletos devueltos y ordena la lista.
    def return_ticket(self, ticket: int) -> None:
        if ticket in self.tickets:
            return
        self.returned_tickets.insert(0, ticket)
        self.returned_tickets.sort()
        return