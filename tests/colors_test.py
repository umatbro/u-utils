import unittest
from um.visuals.color import hex, hex2rgb, Color


class TestColors(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(hex((0, 0, 0)), '#000000')
        self.assertEqual(hex((255, 255, 255)), '#ffffff')

    def test_invalid_hex_input(self):
        with self.assertRaises(ValueError):
            hex((1000, 1000, 1000))
        with self.assertRaises((ValueError, TypeError)):
            hex(10, 10, 10)

    def test_hex2rgb(self):
        self.assertTupleEqual(hex2rgb('#FFFFFF'), (255, 255, 255))
        self.assertTupleEqual(hex2rgb('#ffffff'), (255, 255, 255))
        self.assertTupleEqual(hex2rgb('000000'), (0, 0, 0))
        self.assertTupleEqual(hex2rgb('00ff00'), (0, 255, 0))
        self.assertEqual(hex2rgb('abcdef'), (171, 205, 239))

    def test_hex2rgb_with_invalid_code(self):
        with self.assertRaises(Exception):
            hex2rgb('random string')
        with self.assertRaises(ValueError):
            hex2rgb('abcdefg')
        with self.assertRaises(Exception):
            hex2rgb('0000001')
        with self.assertRaises(ValueError):
            hex2rgb('00g000')
        with self.assertRaises(ValueError):
            hex2rgb('-abcdf')

    def test_color_class_constructor(self):
        color = Color(0x11, 0x22, 0x33)
        self.assertEqual(color.r, 0x11)
        self.assertEqual(color.g, 0x22)
        self.assertEqual(color.b, 0x33)

        with self.assertRaises(ValueError):
            color = Color(0x00, 0x01, 0x100)

        with self.assertRaises(ValueError):
            color = Color(0x00, -0x01, 0x02)

    def test_color_hex(self):
        color = Color(0x21, 0xff, 0xa3)
        self.assertEqual('21ffa3', color.hex())

        black = Color(0, 0, 0)
        self.assertEqual('#000000', black.hex('#'))

        white = Color(255, 255, 255)
        self.assertEqual('0xffffff', white.hex('0x'))
