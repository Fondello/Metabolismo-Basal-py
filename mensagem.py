class Mensagem:
    """Uma classe para imprimir mensagens no programa"""

    @staticmethod
    def imprimir_mensagem():
        """Imprime uma mensagem de boas vindas"""

        print('Muito bem-vindo(a) à Calculadora de Metabolismo Basal. \n'
              'Informaremos a você os níveis de atividade: \n\n'
              'Sedentário (pouco ou nenhum exercício) fator = 1.2 \n'
              'Levemente ativo (exercício leve de 1 a 3 dias por semana) fator = 1.375 \n'
              'Moderadamente ativo (exercício moderado, pratica esportes de 3 a 5 dias por semana) fator = 1.55 \n'
              'Altamente ativo (exercício pesado de 5 a 6 dias por semana) fator = 1.725 \n'
              'Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia) fator = 1.9 \n\n')

    @staticmethod
    def imprimir_fatores():
        """Imprime os valores dos niveis de atividade"""

        print('\n- Nível de Atividade: \n'
              '1. Sedentário - fator = 1.2 \n'
              '2. Levemente ativo - fator = 1.375 \n'
              '3. Moderadamente ativo - fator = 1.55 \n'
              '4. Altamente ativo - fator = 1.725 \n'
              '5. Extremamente ativo - fator = 1.9 \n')
