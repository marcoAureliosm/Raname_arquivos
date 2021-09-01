import os
import zipfile

print("ITECH")
i=int(input("Nª do mês do Relatorio: "))
s=int(input("Nª da Dia do Relatorio: "))

os.rename("(Vlanif62) link-wlk-ipv4 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif63) link-wlk-ipv6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif203) BGP-V4-WLK-via-amarante 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-itech-amarante_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif204) sessao-v6-amarante 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-itech-amarante_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif154) ggc 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-ggc_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif153) netflix 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-nfx_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif155) fna 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-fna_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.227) EBGP-ITECH 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-ix-ora-antigo_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif324) ip-ora-ipv6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix-ora-antigo_rede-itech_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif313) sessao-v6-ix-amarante 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6-ix-amarante_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif261) ipv4-ix-ora-amarante 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf", "relatorio_link-ipv4-ix-ora-amarante_{}-0{}-2021.pdf".format(s,i))   


pasta = r'./'
fileExt = r'.pdf'
lista = ([os.path.join(pasta, _) for _ in os.listdir(pasta) if _.endswith(fileExt)])
b = './'


def zipar(arqs):
    with zipfile.ZipFile('rede-itech.zip','w', zipfile.ZIP_DEFLATED) as z:
        for arq in arqs:
            if (os.path.isfile(arq)):            
                z.write(arq)


for j in range(len(lista)):
    for i in range(0,len(b)):
        lista[j] = lista[j].replace(b[i], "")
        
    

for u in range(len(lista)):
    lista[u] = lista[u][:len(lista[u]) - 3] + '.' + lista[u][len(lista[u]) - 3:]

zipar(lista)

