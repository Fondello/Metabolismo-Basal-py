from menu import Menu


try:
    menu = Menu()
    menu.exibir_menu()
except ValueError as er:
    print(f'Erro: {er}')
