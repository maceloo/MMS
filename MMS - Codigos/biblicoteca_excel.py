try:
    from openpyxl import Workbook
    print("Biblioteca importada com sucesso!")
except ImportError as e:
    print(f"Erro ao importar a biblioteca: {e}")
