from mensagem import Mensagem
from get_valores import GetValores
from limpar import Limpar


class Menu:
    """Uma classe para exibir o menu"""

    @staticmethod
    def exibir_menu():
        """Exibe o menu"""

        mensagem = Mensagem()
        mensagem.imprimir_mensagem()

        valores = GetValores()
        selecionador = valores.get_opcoes()

        if selecionador == 1:
            limpador = Limpar()
            limpador.limpador_de_tela()

            mensagem.imprimir_fatores()
            valores.get_valores()

            resposta = valores.get_opcao_menu()

            if resposta == 's':
                limpador.limpador_de_tela()
                voltar_para_o_menu = Menu()
                voltar_para_o_menu.exibir_menu()
            else:
                print('Ok...')
        else:
            limpador = Limpar()
            limpador.limpador_de_tela()
            voltar_para_o_menu = Menu()
            voltar_para_o_menu.exibir_menu()
