import time


class Calculadora:
    """Uma classe para calcular o metabolismo basal"""

    def __init__(self, altura, peso, idade, sexo, taxa_de_atividade):
        """Inicializa a instância da Calculadora."""

        self._altura = max(0, altura)
        self._peso = max(0, peso)
        self._idade = max(0, idade)
        self._sexo = sexo.upper()
        self.taxa_de_atividade = taxa_de_atividade

    @property
    def altura(self):
        return self._altura

    @property
    def peso(self):
        return self._peso

    @property
    def idade(self):
        return self._idade

    @property
    def sexo(self):
        return self._sexo.upper().strip()

    def calculo_metabolismo(self):
        """Calcula o metabolismo basal com base no sexo."""

        if self._sexo == 'M':
            print('Calculando metabolismo masculino...')
            time.sleep(2)
            calculo = float(self.taxa_de_atividade) * (66 + (self.peso * 13.7) + (self.altura * 5) - (self.idade * 6.8))
            return f'Seu metabolismo basal é de: {calculo:.2f} kcal'
        elif self._sexo == 'F':
            print('Calculando metabolismo feminino...')
            time.sleep(2)
            calculo = float(self.taxa_de_atividade) * (655 + (self.peso * 9.6) + (self.altura * 1.8) -
                                                       (self.idade * 4.7))
            return f'Seu metabolismo basal é de: {calculo:.2f} kcal'

    def __str__(self):
        """Retorna uma representação em string da instância."""

        return f'{self.altura:.0f} - {self.peso} - {self.idade:.0f} - {self.sexo.title()}'
