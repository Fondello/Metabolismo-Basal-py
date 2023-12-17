from calculadora import Calculadora


class GetValores:

    @staticmethod
    def get_valores():
        """Pega os valores passados para serem armazenados na classe Calculadora"""
        print('Informe-nos seus dados para podermos fazer os cálculos necessários: \n')

        altura = float(input('Altura em cm: '))
        peso = float(input('Peso em kg: '))
        idade = float(input('Idade: '))
        sexo = input('Sexo (m/f): ')
        fator = input('Fator: ')

        armazenamento = Calculadora(altura, peso, idade, sexo, fator)
        valor = armazenamento.calculo_metabolismo()
        print(valor)

    @staticmethod
    def get_opcoes():
        """Pega a opçao passado pelo usiario"""

        valor_passado = int(input('Digite 1 para continuar... '))
        return valor_passado

    @staticmethod
    def get_opcao_menu():
        """Pega a opçao passada pelo usuario para voltar ou nao ao menu"""
        resposta = input('\nGostaria de voltar para o menu principal s/n? ')
        return resposta
