import os
from time import sleep
import zipfile

print("INTERATIVA TSA")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª do dia do Relatorio"))

os.rename("(Vlanif641) LINK-IPv4-WIRELINK 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif642) LINK-IPv6-WIRELINK 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif100) Servidores CDN GGC 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-ggc_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif105) vlan105-servidor-netflix 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-nfx_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.228) EBGP-INTERATIVA 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-ix-ora_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))

pasta = r'./'
fileExt = r'.pdf'
lista = ([os.path.join(pasta, _) for _ in os.listdir(pasta) if _.endswith(fileExt)])
b = './'


def zipar(arqs):
    with zipfile.ZipFile('rede-interativa_tsa.zip','w', zipfile.ZIP_DEFLATED) as z:
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
