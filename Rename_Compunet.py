import os
print("INTERATIVA PIP")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))
os.rename("(Vlanif59) cli.bonfimesoualtda.iptransito.as264991(cliente da infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-compunet_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif60) cli.bonfimesoualtda.ipt.v6.as264991(cliente da infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-compunet_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif61) cli.bonfimesousa.cdn.as264991(cliente infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4-cdn_rede-compunet_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif62) cli.bonfimesousa.cdnv6.as264991(cliente infoweb) 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6-cdn_rede-compunet_s{}-{}-2021.pdf".format(s,i))

