import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti1 = Maksukortti(0)
        self.kortti2 = Maksukortti(10000)
    
    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatteen_myydyt_edulliset_lounaat_0(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_myydyt_maukkaat_lounaat_0(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_onnistuu_kassan_rahamaara_kasvaa_oikein(self):
        rahaa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(300)
        rahaa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa_lopussa - rahaa_alussa, 240)
    
    def test_syo_edullisesti_kateisella_onnistuu_vaihtorahan_maara_on_oikea(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtorahat, 60)

    def test_syo_edullisesti_kateisella_osto_onnistuu_ja_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_osto_ei_onnistu_kassan_rahamaara_ei_muutu(self):
        rahaa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(230)
        rahaa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertTrue(rahaa_alussa == rahaa_lopussa)

    def test_syo_edullisesti_kateisella_osto_ei_onnistu_kaikki_rahat_palautetaan(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(palautus, 230)

    def test_syo_edullisesti_kateisella_osto_ei_onnistu_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_onnistuu_kassan_rahamaara_kasvaa_oikein(self):
        rahaa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(450)
        rahaa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa_lopussa - rahaa_alussa, 400)
    
    def test_syo_maukkaasti_kateisella_onnistuu_vaihtorahan_maara_on_oikea(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtorahat, 50)

    def test_syo_maukkaasti_kateisella_osto_onnistuu_ja_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_osto_ei_onnistu_kassan_rahamaara_ei_muutu(self):
        rahaa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(350)
        rahaa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertTrue(rahaa_alussa == rahaa_lopussa)

    def test_syo_maukkaasti_kateisella_osto_ei_onnistu_kaikki_rahat_palautetaan(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(palautus, 350)

    def test_syo_maukkaasti_kateisella_osto_ei_onnistu_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_jos_onnistuu_summa_veloitetaan_kortilta(self):
        kortin_saldo_alussa = self.kortti2.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.kortti2.saldo, kortin_saldo_alussa - 240)

    def test_syo_edullisesti_kortilla_palauttaa_true_jos_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti2))

    def test_syo_edullisesti_kortilla_jos_raha_riittaa_lounasten_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_jos_raha_riittaa_kassan_rahamaara_ei_muutu(self):
        kassa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kortilla(self.kortti2)
        kassa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertTrue(kassa_alussa == kassa_lopussa)
    
    def test_syo_edullisesti_kortilla_palauttaa_false_jos_rahat_eivat_riita(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti1))
    
    def test_syo_edullisesti_kortilla_kortin_rahamaara_ei_muutu_jos_rahat_eivat_riita(self):
        kortin_saldo_alussa = self.kortti1.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(self.kortti1.saldo, kortin_saldo_alussa)
    
    def test_syo_edullisesti_kortilla_myytyjen_lounaiden_maara_ei_muutu_jos_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_rahat_eivat_riita(self):
        palautusarvo = self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200))
        self.assertFalse(palautusarvo)
    
    def test_syo_edullisesti_kortilla_kassan_rahamaara_ei_muutu_jos_rahat_eivat_riita(self):
        kassa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200))
        kassa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertTrue(kassa_alussa == kassa_lopussa)

    def test_syo_maukkaasti_kortilla_jos_onnistuu_summa_veloitetaan_kortilta(self):
        kortin_saldo_alussa = self.kortti2.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.kortti2.saldo, kortin_saldo_alussa - 400)

    def test_syo_maukkaasti_kortilla_palauttaa_true_jos_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti2))

    def test_syo_maukkaasti_kortilla_jos_raha_riittaa_lounasten_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_jos_raha_riittaa_kassan_rahamaara_ei_muutu(self):
        kassa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti2)
        kassa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertTrue(kassa_alussa == kassa_lopussa)
    
    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_rahat_eivat_riita(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti1))
    
    def test_syo_maukkaasti_kortilla_kortin_rahamaara_ei_muutu_jos_rahat_eivat_riita(self):
        kortin_saldo_alussa = self.kortti1.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(self.kortti1.saldo, kortin_saldo_alussa)
    
    def test_syo_maukkaasti_kortilla_myytyjen_lounaiden_maara_ei_muutu_jos_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_rahat_eivat_riita(self):
        palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200))
        self.assertFalse(palautusarvo)
    
    def test_syo_maukkaasti_kortilla_kassan_rahamaara_ei_muutu_jos_rahat_eivat_riita(self):
        kassa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200))
        kassa_lopussa = self.kassapaate.kassassa_rahaa
        self.assertTrue(kassa_alussa == kassa_lopussa)
    
    def test_lataa_rahaa_kortille_positiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti1, 500)
        self.assertEqual(self.kortti1.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_lataa_rahaa_kortille_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti1, -500)
        self.assertEqual(self.kortti1.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)