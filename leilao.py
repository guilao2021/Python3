from excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self.valor_eh_valido(valor):
            raise LanceInvalido("Valor não disponível na sua carteira!")

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def valor_eh_valido(self, valor):
        return valor <= self.__carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self.lance_eh_valido(lance):
            if not self.tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def tem_lances(self):
        return self.__lances

    def usuario_eh_diferente(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não deve dar dois lances seguidos!")

    def lance_eh_maior_que_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance deve ser maior que o anterior!")

    def lance_eh_valido(self, lance):
        return not self.tem_lances() or (self.usuario_eh_diferente(lance) and
                                       self.lance_eh_maior_que_anterior(lance))
