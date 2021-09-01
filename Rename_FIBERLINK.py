import os
from time import sleep
import zipfile

print("FIBERLINK")
i=int(input("Nª do mês do Relatorio: "))
s=int(input("Nª do dia do Relatorio: "))

os.rename("(Vlanif321) v6-vlan321-ptp-borda-fblk 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link_ipv6_ix-ora_rede-fiberlink_{}0{}-2021.pdf".format(s,i))
os.rename("(Vlanif851) sessao.fortel.v4 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif852) sessao.fortel.v6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
os.rename("GGC _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_ggc_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
os.rename("(port-channel1) Lagg20G-NETFLIX 20 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_nfx_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
os.rename("(port-channel3) Lagg40G-FACEBOOK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_fna_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif297) cli-franweb-altos 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_cdn_fwb_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.96) EBGP-FIBERLINK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix-ora-antigo_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))      
os.rename("(Vlanif260) vlan260-ptp-borda-fiberlink 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link_ipv4_ix-ora-novo_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))
   


pasta = r'./'
fileExt = r'.pdf'
lista = ([os.path.join(pasta, _) for _ in os.listdir(pasta) if _.endswith(fileExt)])
b = './'


def zipar(arqs):
    with zipfile.ZipFile('rede-fiberlink.zip','w', zipfile.ZIP_DEFLATED) as z:
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
