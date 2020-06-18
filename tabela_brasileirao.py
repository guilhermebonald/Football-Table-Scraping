from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

# Title Requests.
html = urlopen(
    'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a')
bs = BeautifulSoup(html, 'html.parser')

time01 = bs.findAll('span', {'class': 'hidden-xs'})
t1 = time01
lista_time = []

pontos01 = bs.findAll('th', {'scope': 'row'})
p1 = pontos01
lista_pontos = []

for g in t1:
    lista_time.append(g.get_text())

for h in p1:
    lista_pontos.append(h.get_text())

df = pd.DataFrame(data=lista_time, columns=['Posição:'])
df.insert(loc=1, column='Pontos:', value=lista_pontos)

print(df)
# time.sleep(60)
