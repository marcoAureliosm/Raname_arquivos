import os
print("INFOWEB")
i=int(input("Nª do mês do Relatorio"))
s=int(input("Nª da semana do Relatorio"))
os.rename("(et-0_0_0.1111) EBGP-IPV4-WIRELINK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.1112) EBGP-IPV6-WIRELINK 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(ae2.1295) EBGP-GOOGLE 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_ggc01_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(ae2.1296) EBGP-GOOGLE-2 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_ggc02_rede-infoweb_s01-08-2021.pdf".format(s,i))
os.rename("(ae2.1294) EBGP-NETFLIX 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_nfx_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(ae2.1000) EBGP-FACEBOOK 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_v6_cdn_fna_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(lt-0_0_0.7) IX-ORA-ROUTER-MASTER-IPV4 100 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix_ora_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(lt-0_0_0.9) IX-ORA-ROUTER-MASTER-IPV6 100 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix_ora_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.1008) EBGP-IPV4-IX-THE 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix_tsa_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(et-0_0_0.1009) EBGP-IPV6-IX-THE 40 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix_tsa_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(ae2.2012) EBGP-IPV4-IX-SLZ 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv4_ix_slz_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
os.rename("(ae2.2013) EBGP-IPV6-IX-SLZ 70 GBit_s _ Relatório _ PRTG - NOC Ora Telecom.pdf","relatorio_link-ipv6_ix_slz_rede-infoweb_s{}-{}-2021.pdf".format(s,i))
