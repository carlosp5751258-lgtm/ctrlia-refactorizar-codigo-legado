"""Tests de CARACTERIZACIÓN de facturas.total: fijan lo que hace HOY, rarezas incluidas, no lo que debería hacer."""
import unittest

from facturas import total


class TotalHoy(unittest.TestCase):
    # Cada línea es [concepto, precio, cantidad]

    def test_suma_precio_por_cantidad(self):
        self.assertEqual(total([["a", 10, 2], ["b", 5, 1]], "normal"), 25)

    def test_cantidad_none_cuenta_como_1(self):
        self.assertEqual(total([["a", 10, None]], "normal"), 10)

    def test_rareza_modifica_la_lista_de_entrada(self):
        lineas = [["a", 10, None]]
        total(lineas, "normal")
        self.assertEqual(lineas[0][2], 1)  # el llamador ve el cambio

    def test_cantidad_0_se_queda_en_0(self):
        self.assertEqual(total([["a", 10, 0]], "normal"), 0)

    def test_vip_descuenta_10_por_ciento(self):
        self.assertEqual(total([["a", 100, 1]], "VIP"), 90.0)

    def test_rareza_vip_en_minusculas_no_tiene_descuento(self):
        self.assertEqual(total([["a", 100, 1]], "vip"), 100)

    def test_mas_de_1000_resta_50(self):
        self.assertEqual(total([["a", 1100, 1]], "normal"), 1050)

    def test_exactamente_1000_no_resta_50(self):
        self.assertEqual(total([["a", 1000, 1]], "normal"), 1000)

    def test_rareza_vip_se_aplica_antes_y_puede_anular_los_50(self):
        self.assertEqual(total([["a", 1100, 1]], "VIP"), 990.0)    # sin VIP serían 1050
        self.assertEqual(total([["a", 2000, 1]], "VIP"), 1750.0)  # 1800 - 50

    def test_rareza_lista_vacia_devuelve_int_o_float_segun_cliente(self):
        sin_vip, con_vip = total([], "normal"), total([], "VIP")
        self.assertEqual((sin_vip, type(sin_vip)), (0, int))
        self.assertEqual((con_vip, type(con_vip)), (0.0, float))

    def test_redondea_a_2_decimales(self):
        self.assertEqual(total([["a", 0.1, 3]], "normal"), 0.3)

    def test_rareza_precio_none_lanza_type_error(self):
        with self.assertRaises(TypeError):
            total([["a", None, 1]], "normal")


if __name__ == "__main__":
    unittest.main()
