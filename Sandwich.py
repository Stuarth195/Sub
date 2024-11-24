import uuid

class Sandwich:
    def __init__(self, tipo, tamaño):
        """
        Inicializa el sándwich con el tipo y tamaño especificado.
        """
        self.tipo = tipo
        self.tamaño = tamaño  # Tamaño en cm: 15 o 30
        self.precio_base = 0.0

    def getDescripcion(self):
        """
        Devuelve la descripción del sándwich.
        """
        return f"{self.tipo} ({self.tamaño} cm)"

    def getPrecio(self):
        """
        Devuelve el precio base del sándwich.
        """
        return self.precio_base

    def getTamaño(self):
        """
        Devuelve el tamaño del sándwich (15 o 30).
        """
        return self.tamaño


class Pavo(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Pavo", tamaño)
        self.precio_base = 12.0 if tamaño == 15 else 16.0


class Pollo(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Pollo", tamaño)
        self.precio_base = 12.0 if tamaño == 15 else 16.0


class Beef(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Beef", tamaño)
        self.precio_base = 14.0 if tamaño == 15 else 18.0


class Italiano(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Italiano", tamaño)
        self.precio_base = 13.0 if tamaño == 15 else 17.0


class Veggie(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Veggie", tamaño)
        self.precio_base = 10.0 if tamaño == 15 else 14.0


class Atun(Sandwich):
    def __init__(self, tamaño):
        super().__init__("Atún", tamaño)
        self.precio_base = 12.0 if tamaño == 15 else 16.0


class Combo(Sandwich):
    def __init__(self, tipo1, tipo2, tamaño):
        """
        Un "Combo" es una combinación de dos tipos de sándwiches con el mismo tamaño.
        """
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.tamaño = tamaño
        self.precio_base = self.calcularPrecioCombo(tipo1, tipo2, tamaño)

    def calcularPrecioCombo(self, tipo1, tipo2, tamaño):
        """
        Calcula el precio del combo sumando los precios de los sándwiches individuales.
        """
        # Creamos instancias de los sándwiches para obtener sus precios
        sandwich1 = self.crearSandwich(tipo1, tamaño)
        sandwich2 = self.crearSandwich(tipo2, tamaño)

        # Sumamos los precios de los dos sándwiches
        return sandwich1.getPrecio() + sandwich2.getPrecio()

    def crearSandwich(self, tipo, tamaño):
        self.descuento = 10
        """
        Crea una instancia de sándwich según el tipo y tamaño especificados.
        """
        if tipo == "Pavo":
            return Pavo(tamaño)
        elif tipo == "Pollo":
            return Pollo(tamaño)
        elif tipo == "Beef":
            return Beef(tamaño)
        elif tipo == "Italiano":
            return Italiano(tamaño)
        elif tipo == "Veggie":
            return Veggie(tamaño)
        elif tipo == "Atún":
            return Atun(tamaño)
        else:
            raise ValueError(f"Tipo de sándwich no reconocido: {tipo}")

    def getDescripcion(self):
        return f"Combo: {self.tipo1} + {self.tipo2} ({self.tamaño} cm)"

    def getPrecio(self):
        return self.precio_base - (self.precio_base * (self.descuento/100))
