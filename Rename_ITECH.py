import os
print("ITECH")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))

os.rename("(Vlanif203) BGP-V4-WLK-via-amarante 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-itech-amarante_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif204) sessao-v6-amarante 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-itech-amarante_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif154) ggc 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-v6-cdn-ggc_rede-itech_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif153) netflix 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.","relatorio_link-ipv4-v6-cdn-nfx_rede-itech_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif155) fna 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom","relatorio_link-ipv4-v6-cdn-fna_rede-itech_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.227) EBGP-ITECH 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom","relatorio_link-ipv4-ix-ora_rede-itech-amarante_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif62) link-wlk-ipv4 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-itech_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif63) link-wlk-ipv6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-itech_{}-{}-2021.pdf".format(s,i))


