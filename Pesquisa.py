#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import csv
from datetime import datetime

class Pesquisa:
    def __init__(self):
        self.dados_respostas = []
    
    # Função criada para coletar dados e respostas da pesquisa
    def coletar_respostas(self):

        # Utilizando while para dar segmento na pesquisa até que seja encerrada via o comando solicitado
        while True:
            print('-'*100)
            print('\033[33mOlá! Esta é uma pesquisa sobre equilíbrio entre vida pessoal, trabalho e saúde mental.')
            idade = input("\033[0;0mInforme sua idade (ou '00' para sair): ")
            print('-'*100)
            if idade == '00':
                break
            
            print('-'*100)
            genero = input("Informe seu gênero\n1 - Feminino\n2 - Masculino\n3 - Transgênero\n4 - Outro\n ")
            print('-'*100)
            # Dicionário para guardar os valores correspondetes à pesquisa de gênero, utilizando .get para acessá-lo na entrada 'genero'
            genero_opcao = {
                '1': 'Feminino',
                '2': 'Masculino',
                '3': 'Transgênero',
                '4': 'Outro'}.get(genero)
            
            # Entradas para coletar as respostas da pesquisa
            resposta1 = input("A sua empresa oferece suporte adequado à saúde mental dos funcionários?\n1-Sim\n2-Não\n3-Não sei responder\n ")
            print('-'*100)
            resposta2 = input("Você ja passou por situações de sobrecarga no seu trabalho?\n1-Sim\n2-Não\n3-Não sei responder\n ")
            print('-'*100)
            resposta3 = input("Na empresa em que você trabalha existem políticas para promover equilíbrio entre vida pessoal e trabalho?\n1-Sim\n2-Não\n3-Não sei responder\n ")
            print('-'*100)
            resposta4 = input("Você acha importante que as empresas adotem políticas/programas de bem-estar para cuidar da saúde\nmental dos seus funcionários?\n1-Sim\n2-Não\n3-Não sei responder\n ")
            print('-'*100)
            print('\033[36mObrigado por responder nossa pesquisa!')
            print('-'*100)

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Dicionário para guardar em forma de valor as entradas pedidas ao usuário
            respostas = { 
                          'idade': idade,
                          'genero': genero_opcao,
                          'lista_respostas': [resposta1, resposta2, resposta3, resposta4],
                          'data_hora': data_hora
                          }

            self.dados_respostas.append(respostas)
    
    def salvar_csv(self):
        try:
            nome_arquivo = input("Informe o nome do arquivo para salvar os dados: ")
            
            # Verifica se a extensão .csv está presente no nome do arquivo
            if not nome_arquivo.endswith('.csv'):
                nome_arquivo += '.csv'
            
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
                
                print('Os dados foram salvos no arquivo CSV com sucesso!')
        except IOError:
            print('Erro ao salvar o arquivo. Verifique o nome e a permissão do diretório.')
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {str(e)}')

# Execução do programa
pesquisa = Pesquisa()
pesquisa.coletar_respostas()
pesquisa.salvar_csv()

