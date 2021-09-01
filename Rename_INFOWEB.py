import os
from time import sleep
import zipfile

print("INFOWEB")
i=int(input("Nª do mês do Relatorio: "))
s=int(input("Nª do dia do Relatorio: "))


os.rename("(et-0_0_0.1111) EBGP-IPV4-WIRELINK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.1112) EBGP-IPV6-WIRELINK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(ae2.1295) EBGP-GOOGLE 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_ggc01_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(ae2.1296) EBGP-GOOGLE-2 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_ggc02_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(ae2.1294) EBGP-NETFLIX 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_nfx_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(ae2.1000) EBGP-FACEBOOK 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_fna_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(lt-0_0_0.7) IX-ORA-ROUTER-MASTER-IPV4 100 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix-ora-antigo_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(lt-0_0_0.9) IX-ORA-ROUTER-MASTER-IPV6 100 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix-ora-antigo_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif300) Vlanif300 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix-ora-novo_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(Vlanif301) vlan301-ptp-CORE-IFW-V6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix-ora-novo_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.1008) EBGP-IPV4-IX-THE 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix_tsa_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.1009) EBGP-IPV6-IX-THE 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix_tsa_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(ae2.2012) EBGP-IPV4-IX-SLZ 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix_slz_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
os.rename("(ae2.2013) EBGP-IPV6-IX-SLZ 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix_slz_rede-infoweb_{}-0{}-2021.pdf".format(s,i))


pasta = r'./'
fileExt = r'.pdf'
lista = ([os.path.join(pasta, _) for _ in os.listdir(pasta) if _.endswith(fileExt)])
b = './'


def zipar(arqs):
    with zipfile.ZipFile('rede-infoweb.zip','w', zipfile.ZIP_DEFLATED) as z:
        for arq in arqs:
            if (os.path.isfile(arq)):            
                z.write(arq)


for j in range(len(lista)):
    for i in range(0,len(b)):
        lista[j] = lista[j].replace(b[i], "")
        
    

for u in range(len(lista)):
    lista[u] = lista[u][:len(lista[u]) - 3] + '.' + lista[u][len(lista[u]) - 3:]

zipar(lista)





