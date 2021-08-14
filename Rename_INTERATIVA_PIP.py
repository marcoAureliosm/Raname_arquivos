import os
print("INTERATIVA PIP")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))

os.rename("(et-0_0_0.192) EBGP-INTERATIVA-PIP 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom","relatorio_link-ipv4-ix-ora_rede-interativa-pip_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif70) vlan70-bgp-hw6720-wlk-piripiri 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-interativa-pip_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif72) vlan72-bgp-hw6720-wlk-piripiri 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-interativa-pip_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.193) EBGP-INTERATIVA-PIP-IPv6 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6-ix-ora_rede-interativa-pip_s{}-{}-2021.pdf".format(s,i))

