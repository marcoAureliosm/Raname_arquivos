import os
from time import sleep
import zipfile

print("INTERATIVA PIP")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª di dia do Relatorio"))

os.rename("(et-0_0_0.192) EBGP-INTERATIVA-PIP 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.193) EBGP-INTERATIVA-PIP-IPv6 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif70) vlan70-bgp-hw6720-wlk-piripiri 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif72) vlan72-bgp-hw6720-wlk-piripiri 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.193) EBGP-INTERATIVA-PIP-IPv6 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))

pasta = r'./'
fileExt = r'.pdf'
lista = ([os.path.join(pasta, _) for _ in os.listdir(pasta) if _.endswith(fileExt)])
b = './'


def zipar(arqs):
    with zipfile.ZipFile('rede-interativa_PIPs.zip','w', zipfile.ZIP_DEFLATED) as z:
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
