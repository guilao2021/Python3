from excecoes import LanceInvalido
from leilao import Usuario,Leilao
import pytest

class TestUsuario:

    @pytest.fixture
    def gui(self):
        return Usuario("Gui", 500.0)

    @pytest.fixture
    def leilao(self):
        return Leilao("Celular")

    def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(self,gui, leilao):
        gui.propoe_lance(leilao, 50.0)

        assert gui.carteira == 450.0

    def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(self,gui, leilao):
        gui.propoe_lance(leilao, 10.0)

        assert gui.carteira == 490.0

    def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(self,gui, leilao):
        gui.propoe_lance(leilao, 500.0)

        assert gui.carteira == 0

    def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(self, gui, leilao):
        with pytest.raises(LanceInvalido):
            gui.propoe_lance(leilao, 600.0)
