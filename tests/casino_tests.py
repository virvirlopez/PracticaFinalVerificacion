import unittest
from casino.Casino import Casino
from mock import Mock


class CasinoTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_ayadir_jugador(self):
        r = Mock()
        r.get= Mock(return_value=1)
        r.set = Mock(return_value=True)
        r.zadd = Mock(return_value=True)
        casino = Casino(r)
        self.assertEqual(casino.ayadir_jugador("pepe", 29), True)

    def test_escoger_juego(self):
        r = Mock()
        casino = Casino(r)
        self.assertEqual(casino.escoger_juego(2), True)
        self.assertEqual(casino.escoger_juego(1), True)

    def test_abandonar_juego(self):
        r = Mock()
        r.get= Mock(return_value=1)
        casino = Casino(r)
        self.assertEqual(casino.abandonar_juego("pepe", 2), True)

    def test_obtener_creditos(self):
        r = Mock()
        r.get = Mock(return_value=1)
        casino = Casino(r)
        self.assertEqual(casino.obtener_creditos("pepe"), True)

    def test_obtener_creditos_varios_jugadores(self):
        r = Mock()
        r.get = Mock(return_value=1)
        casino = Casino(r)
        self.assertEqual(casino.obtener_creditos_varios_jugadores("pepe", "pepe"), True)

    def test_ingresar_creditos(self):
        r = Mock()
        r.get = Mock(return_value=1)
        r.set = Mock(return_value=True)
        casino = Casino(r)
        self.assertEquals(casino.ingresar_creditos("pepe", 1), True)

    def test_sacar_creditos(self):
        r = Mock()
        r.get = Mock(return_value=1)
        r.set = Mock(return_value=True)
        casino = Casino(r)
        self.assertEquals(casino.sacar_creditos("pepe", 1), True)


    def test_fails_bool(self):
        r = Mock()
        r.get = Mock(return_value=1)
        r.set = Mock(return_value=True)
        r.zadd = Mock(return_value=True)
        casino = Casino(r)
        self.assertRaises(Exception, casino.ayadir_jugador("pepe", True))
        self.assertRaises(Exception, casino.sacar_creditos("pepe", True))
        self.assertRaises(Exception, casino.ingresar_creditos("pepe", True))
        self.assertRaises(Exception, casino.abandonar_juego("pepe", True))
        self.assertRaises(Exception, casino.obtener_creditos_varios_jugadores("pepe", True))
        self.assertRaises(Exception, casino.ayadir_jugador(True, "pepe"))
        self.assertRaises(Exception, casino.escoger_juego(True))
        self.assertRaises(Exception, casino.obtener_creditos(True))


    def test_fails_tupla(self):
        r = Mock()
        r.get = Mock(return_value=1)
        r.set = Mock(return_value=True)
        r.zadd = Mock(return_value=True)
        casino = Casino(r)
        self.assertRaises(Exception, casino.ayadir_jugador((1, 2, 3), 2))
        self.assertRaises(Exception, casino.ingresar_creditos((1, 2, 3), 2))
        self.assertRaises(Exception, casino.abandonar_juego((1, 2, 3), 2))
        self.assertRaises(Exception, casino.obtener_creditos_varios_jugadores((1, 2, 3), 2))
        self.assertRaises(Exception, casino.obtener_creditos((1, 2)))

    def test_fails_number_less_than_0(self):
        r = Mock()
        r.get = Mock(return_value=1)
        r.set = Mock(return_value=True)
        r.zadd = Mock(return_value=True)
        casino = Casino(r)
        self.assertRaises(casino.ayadir_jugador("pepe", -1))
        self.assertRaises(casino.escoger_juego(-1))
        self.assertRaises(casino.ingresar_creditos("pepe", -1))
        self.assertRaises(casino.sacar_creditos("pepe", -1))


    def test_fails_number_more_than_2(self):
        r = Mock()
        r.get = Mock(return_value=1)
        r.set = Mock(return_value=True)
        r.zadd = Mock(return_value=True)
        casino = Casino(r)
        self.assertRaises(casino.escoger_juego(3))


if __name__ == '__main__':
    unittest.main()