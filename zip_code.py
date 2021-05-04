import requests

class Cep:

    def __init__(self, cep):
        if len(cep) == 8:
            self.cep = cep
        else:
            raise ValueError("CEP deve conter 8 dígitos!")

    def cep_valido(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        check_cep = requests.get(url)
        try:
            dados = check_cep.json()
            return   [dados['localidade'],
                      dados['uf'],
                      dados['logradouro'],
                      dados['bairro']]
        except KeyError:
            raise ValueError("CEP inválido!!!!")

    def formata_cep(self):
        dados = self.cep_valido()
        info = self.cep_valido()
        return "CEP: {}-{}\nCidade: {}\nEstado: {}\nRua: {}\nBairro: {}\n".format(self.cep[:5],self.cep[5:],info[0],
                                                                                  info[1],info[2],info[3])

    def __str__(self):
        return self.formata_cep()

#teste
cep_usuario = input("Digite o seu CEP: ")
obj_cep = Cep(cep_usuario)
print(obj_cep)




