import os
from time import sleep
import zipfile

print("INTERATIVA PIP")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª do dia do Relatorio"))

os.rename("(Vlanif59) cli.bonfimesoualtda.iptransito.as264991(cliente da infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-compunet_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif60) cli.bonfimesoualtda.ipt.v6.as264991(cliente da infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-compunet_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif61) cli.bonfimesousa.cdn.as264991(cliente infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-cdn_rede-compunet_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif62) cli.bonfimesousa.cdnv6.as264991(cliente infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6-cdn_rede-compunet_{}-0{}-2021.pdf".format(s,i))

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

