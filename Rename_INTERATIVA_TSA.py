import os
print("INTERATIVA TSA")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))
os.rename("(Vlanif641) LINK-IPv4-WIRELINK 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-interativa-tsa_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif642) LINK-IPv6-WIRELINK 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-interativa-tsa_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif100) Servidores CDN GGC 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-ggc_rede-interativa-tsa_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif105) vlan105-servidor-netflix 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-nfx_rede-interativa-tsa_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.228) EBGP-INTERATIVA 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-ix-ora_rede-interativa-tsa_s{}-{}-2021.pdf".format(s,i))

