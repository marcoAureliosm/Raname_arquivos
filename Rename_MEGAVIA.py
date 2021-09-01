import os
from time import sleep
import zipfile
print("MEGAVIA")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª do dia do Relatorio"))
os.rename("(Vlanif2034) sessao-bgp-wirelink 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_rede-megavia_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif2036) Sessao-Wirelink-IPv6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-megavia_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.229) EBGP-MEGAVIA 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-ix-ora_rede-megavia-{}-0{}-2021.pdf".format(s,i))

pasta = r'./'
fileExt = r'.pdf'
lista = ([os.path.join(pasta, _) for _ in os.listdir(pasta) if _.endswith(fileExt)])
b = './'


def zipar(arqs):
    with zipfile.ZipFile('rede-megavia.zip','w', zipfile.ZIP_DEFLATED) as z:
        for arq in arqs:
            if (os.path.isfile(arq)):            
                z.write(arq)


for j in range(len(lista)):
    for i in range(0,len(b)):
        lista[j] = lista[j].replace(b[i], "")
        
    

for u in range(len(lista)):
    lista[u] = lista[u][:len(lista[u]) - 3] + '.' + lista[u][len(lista[u]) - 3:]
    print(lista[u])

zipar(lista)

print(lista)

sleep(5)

