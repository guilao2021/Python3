from unittest import TestCase
from excecoes import LanceInvalido
from leilao import Usuario, Lance, Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario("Gui", 500.0)
        self.bia = Usuario("Bia", 500.0)

        self.lance_bia = Lance(self.bia, 150.0)
        self.lance_gui = Lance(self.gui, 100.0)

        self.leilao = Leilao("PS5")

    def test_deve_retornar_maior_e_menor_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(self.lance_bia)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_bia)
            self.leilao.propoe(self.lance_gui)

    def test_deve_retornar_maior_e_menor_lance_quando_adicionado_um_lance(self):
        self.leilao.propoe(self.lance_gui)

    def test_deve_retornar_maior_e_menor_lance_quando_adicionados_tres_lances(self):
        ze = Usuario("Zé", 500.0)
        lance_ze = Lance(ze, 200.0)

        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(self.lance_bia)
        self.leilao.propoe(lance_ze)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_gui)
        qtd_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, qtd_lances_recebidos)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(self.lance_bia)
        qtd_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, qtd_lances_recebidos)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_gui2 = Lance(self.gui,210.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui2)
