#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Pesquisa


# In[ ]:


def main():
    pesquisa = Pesquisa.Pesquisa()
    pesquisa.coletar_respostas()
    pesquisa.salvar_csv()
    
main()

