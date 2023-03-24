import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 1500)
    
    def test_saldo_vahenee_oikein_jos_rahat_riittavat(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 500)      

    def test_saldo_ei_muutu_jos_ei_ole_tarpeeksi_katetta(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo, 1000)          

    def test_palauttaa_true_jos_rahat_riittivat(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_palauttaa_false_jos_rahat_eivat_riittaneet(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1500))         