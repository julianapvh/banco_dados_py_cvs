#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import csv
from datetime import datetime

class Pesquisa:
    def __init__(self):
        self.dados_respostas = []  # Inicializa a lista que irá armazenar as respostas dos participantes

    def coletar_respostas(self):
        while True:
            print('-' * 100)
            print('\033[33mOlá! Está é uma pesquisa sobre equilíbrio entre vida pessoal, trabalho e saúde mental.')

            try:
                idade = int(input("\033[0;0mInforme sua idade (ou '00' para sair): "))
                if idade == 0:  # Verifica se o usuário deseja sair da pesquisa
                    break
                elif idade < 0:  # Verifica se a idade é um valor válido
                    print("Idade inválida. Por favor, digite um valor numérico positivo para a idade.")
                    continue  # Reinicia o loop para solicitar a idade novamente em caso de valor inválido
            except ValueError:  # Captura o erro caso o usuário não digite um número
                print("Idade inválida. Por favor, digite um valor numérico para a idade.")
                continue  # Reinicia o loop para solicitar a idade novamente em caso de valor inválido

            print('-' * 100)

            genero = input("Informe seu Gênero\n1 - Feminino\n2 - Masculino\n3 - Transgênero\n4 - Outro\n ")
            print('-' * 100)

            genero_opcao = {'1': 'Feminino', '2': 'Masculino', '3': 'Transgênero', '4': 'Outro'}.get(genero)  # Mapeia a escolha do gênero para a opção correspondente

            resposta1 = self.obter_resposta("A sua empresa oferece suporte adequado à saúde mental dos funcionários?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")
            resposta2 = self.obter_resposta("Você já passou por situações de sobrecarga no seu trabalho?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")
            resposta3 = self.obter_resposta("Na empresa em que você trabalha, existem políticas para promover equilíbrio entre vida pessoal e trabalho?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")
            resposta4 = self.obter_resposta("Você acha importante que as empresas adotem políticas/programas de bem-estar para cuidar da saúde mental dos seus funcionários?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")

            print('-' * 100)
            print('\033[36mObrigado por responder nossa pesquisa!')
            print('-' * 100)

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém a data e hora atual

            respostas = {
                'idade': idade,
                'genero': genero_opcao,
                'lista_respostas': [resposta1, resposta2, resposta3, resposta4],
                'data_hora': data_hora
            }

            self.dados_respostas.append(respostas)  # Adiciona as respostas à lista de dados de respostas

    def obter_resposta(self, mensagem):
        while True:
            try:
                resposta = int(input(mensagem))
                if resposta not in [1, 2, 3]:  # Verifica se a resposta está dentro das opções válidas
                    print("Opção inválida. Por favor, selecione uma opção válida.")
                else:
                    return resposta
            except ValueError:  # Captura o erro caso o usuário não digite um número
                print("Opção inválida. Por favor, selecione uma opção válida.")

    def salvar_csv(self):
        nome_arquivo = input("Informe o nome do arquivo CSV para salvar os dados: ")
        
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            campos = ['idade', 'genero', 'resposta_1', 'resposta_2', 'resposta_3', 'resposta_4', 'data_hora_resposta']
            writer = csv.DictWriter(arquivo_csv, fieldnames=campos)
            writer.writeheader()
            
            for resposta in self.dados_respostas:
                writer.writerow({
                    'idade': resposta['idade'],
                    'genero': resposta['genero'],
                    'resposta_1': resposta['lista_respostas'][0],
                    'resposta_2': resposta['lista_respostas'][1],
                    'resposta_3': resposta['lista_respostas'][2],
                    'resposta_4': resposta['lista_respostas'][3],
                    'data_hora_resposta': resposta['data_hora']
                })

# Cria uma instância da classe Pesquisa e executa o fluxo do programa
pesquisa = Pesquisa()
pesquisa.coletar_respostas()
pesquisa.salvar_csv()
