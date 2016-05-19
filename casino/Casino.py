import redis

class Casino:

    def __init__(self, connector=None):
        if connector is None:
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
            self.r = redis.Redis(connection_pool=pool)
        else:
            self.r = connector


    def ayadir_jugador(self, nombre, creditos):
        contador_numero = int(self.r.get("contador"))
        numero_contador = contador_numero + 1
        if creditos is None and creditos < 0 and nombre is None:
            raise Exception
        if creditos > 0:
            self.r.set(nombre, creditos)
            self.r.set("contador", numero_contador)
            self.r.zadd("jugadores", nombre, creditos)
            return True


    def escoger_juego(self, numero_juego):
        if numero_juego < 1 and numero_juego > 2 and numero_juego is bool:
            raise Exception
        else:
            return True

    def abandonar_juego(self, nombre, creditos):
        contador_numero=int(self.r.get("contador"))
        if contador_numero <= 0 and nombre is bool and creditos is bool:
            raise Exception
        else:
            numeroContador = contador_numero - 1
            self.r.set("contador", numeroContador)
            return True

    def obtener_creditos(self, nombre):
        creditos_jugador= int(self.r.get(nombre))
        if (creditos_jugador is None) or (nombre is None):
            raise Exception
        else:
            print creditos_jugador
            return True

    def obtener_creditos_varios_jugadores(self, nombre1, nombre2):
        creditos_jugador1 = int(self.r.get(nombre1))
        creditos_jugador2 = int(self.r.get(nombre2))
        if creditos_jugador1 is None or creditos_jugador1 is bool:
            raise Exception
        if creditos_jugador2 is None or creditos_jugador2 is bool:
            raise Exception
        else:
            #print ("Creditos jugador 1 "+creditos_jugador1+" Creditos jugador 2"+creditos_jugador2)
            return True

    def ingresar_creditos(self, nombre, creditos_ingresar):
        creditos_jugador = int(self.r.get(nombre))
        if nombre is None or nombre is bool or nombre is int:
            raise Exception
        if creditos_ingresar < 0 and creditos_ingresar is bool and creditos_ingresar is str:
            raise Exception
        else:
            credito_total = creditos_jugador + int(creditos_ingresar)
            self.r.set(nombre, credito_total)
            return True


    def sacar_creditos(self, nombre, creditos_sacar):
        creditos_jugador = int(self.r.get(nombre))
        credito_total = creditos_jugador - int(creditos_sacar)
        if nombre is None or nombre is bool or creditos_sacar is bool:
            raise Exception
        if credito_total < 0 or credito_total is None:
            raise Exception
        else:
            self.r.set(nombre, credito_total)
            return True

if __name__ == "__main__":
    casino = Casino()

    casino.r.flushall()

    casino.r.set("contador", 0)

    casino.ayadir_jugador("pepe", 30)

    casino.escoger_juego(1)

    casino.ingresar_creditos("pepe", 1)

    casino.sacar_creditos("pepe", 2)

    casino.obtener_creditos_varios_jugadores("pepe", "pepe")

    casino.obtener_creditos("pepe")



