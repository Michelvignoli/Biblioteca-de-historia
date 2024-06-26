import json
from typing import List, Dict

class Documento:
    def __init__(self, titulo: str, data: str, tema: str, autor: str):
        self.titulo = titulo
        self.data = data
        self.tema = tema
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.documentos: List[Documento] = []

    def adicionar_documento(self, documento: Documento):
        self.documentos.append(documento)

    def salvar_documentos(self, arquivo: str):
        try:
            with open(arquivo, 'w') as f:
                json.dump([doc.__dict__ for doc in self.documentos], f)
            print("Documentos salvos com sucesso.")
        except IOError:
            print("Erro ao salvar os documentos.")

    def carregar_documentos(self, arquivo: str):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                self.documentos = [Documento(**doc) for doc in dados]
            print("Documentos carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")

    def ordenar_documentos_por_titulo(self):
        # Implementação do algoritmo Bubble Sort
        n = len(self.documentos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.documentos[j].titulo > self.documentos[j + 1].titulo:
                    self.documentos[j], self.documentos[j + 1] = self.documentos[j + 1], self.documentos[j]

    def listar_documentos(self):
        for doc in self.documentos:
            print(f"Título: {doc.titulo}, Data: {doc.data}, Tema: {doc.tema}, Autor: {doc.autor}")

def main():
    biblioteca = Biblioteca()

    
    biblioteca.adicionar_documento(Documento("História do Brasil", "1999", "História", "Pedro Silva"))
    biblioteca.adicionar_documento(Documento("A Revolução Francesa", "2005", "História", "Maria Santos"))
    biblioteca.adicionar_documento(Documento("Segunda Guerra Mundial", "2010", "História", "João Oliveira"))

    
    biblioteca.salvar_documentos("documentos.json")

   
    biblioteca.carregar_documentos("documentos.json")

    print("\nDocumentos antes da ordenação:")
    biblioteca.listar_documentos()

    
    biblioteca.ordenar_documentos_por_titulo()

    print("\nDocumentos após a ordenação por título:")
    biblioteca.listar_documentos()

if __name__ == "__main__":
    main()
