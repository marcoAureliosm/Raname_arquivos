import os
print("FIBERLINK")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))
os.rename("(Vlanif851) sessao.fortel.v4 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif852) sessao.fortel.v6 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
os.rename("GGC _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_ggc_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
os.rename("(port-channel1) Lagg20G-NETFLIX 20 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_nfx_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
os.rename("(port-channel3) Lagg40G-FACEBOOK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_fna_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
os.rename("(Vlanif297) cli-franweb-altos 1 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_cdn_fwb_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.96) EBGP-FIBERLINK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix-ora_rede-fiberlink_s{}-{}-2021.pdf".format(s,i))
          
