import os


class Limpar:
    """Uma classe para limpar a tela"""

    @staticmethod
    def limpador_de_tela():
        """Limpa a tela"""

        os.system('cls' if os.name == 'nt' else 'clear')
