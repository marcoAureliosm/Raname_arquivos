import os
print("MEGAVIA")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))
os.rename("(Vlanif2034) sessao-bgp-wirelink 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_rede-megavia_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif2036) Sessao-Wirelink-IPv6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-megavia_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.229) EBGP-MEGAVIA 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-ix-ora_rede-megavia-s{}-{}-2021.pdf".format(s,i))

