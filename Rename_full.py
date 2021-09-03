from os import getcwd, listdir
import os
import re
import shutil

i=int(input("Nª do mês do Relatorio: "))
s=int(input("Nª do dia do Relatorio: "))
#===========================Leitura de arquivos na pasta =============================
print(getcwd())
doc=[]
for c in listdir():
    doc.append(c)
qt = len(doc)
#=============================== Leitura de conteudo do arquivo para poder utitiliza a expessão regular=====================
#REDE FIBERLINK
for i in range (qt):
    if doc[i].find('fiberlink-IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('fiberlink-IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('fiberlink-GGC') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_ggc_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('fiberlink-NFX') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_nfx_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('fiberlink-FNA') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_fna_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('fiberlink-CDN-Fanweb') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_cdn_fwb_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('fiberlink-ixOra-IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_ix-ora_rede-fiberlink_{}-0{}-2021.pdf".format(s,i))      
    if doc[i].find('fiberlink-ixOra-IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link_ipv6_ix-ora_rede-fiberlink_{}0{}-2021.pdf".format(s,i))
#REDE INFOWEB
    if doc[i].find('infoweb_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb_GGCI') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_ggc01_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb_GGCII') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_ggc02_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb_NFX') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_nfx_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb_FNA') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_cdn_fna_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb_ixOra_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_ix-ora_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb-_ixOra_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_ix-ora_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb-TSA_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_ix_tsa_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb-TSA_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_ix_tsa_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb-SLZ_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_ix_slz_rede-infoweb_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('infoweb-SLZ_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_ix_slz_rede-infoweb_{}-0{}-2021.pdf".format(s,i))
#REDE ITECH
    if doc[i].find('itech_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_IPV4_amarante') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_rede-itech-amarante_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_IPV6_amarante') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-itech-amarante_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_GGC') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-v6-cdn-ggc_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_NFX') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-v6-cdn-nfx_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_FNA') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-v6-cdn-fna_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_ix_ora_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_ix_ora_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_ix-ora_rede-itech_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_ix_Amarante_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6-ix-amarante_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('itech_ix_Amarante_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar, "relatorio_link-ipv4-ix-ora-amarante_{}-0{}-2021.pdf".format(s,i))   

#REDE MEGAVIA
    if doc[i].find('megavia_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_v6_rede-megavia_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('megavia_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-megavia_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('megavia_ix_Ora_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-megavia-{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('megavia_ix_Ora_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6-ix-ora_rede-megavia-{}-0{}-2021.pdf".format(s,i))

 #REDE iNTERATIVA TSA  
    if doc[i].find('interativa_tsa_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_tsa_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_tsa_GGC') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-v6-cdn-ggc_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_tsa_NFX') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-v6-cdn-nfx_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_tsa_ix_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_tsa_ix_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6-ix-ora_rede-interativa-tsa_s{}-0{}-2021.pdf".format(s,i))
#REDE INTERATIVA PIP
    if doc[i].find('interativa_pip_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_pip_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_pip_ix_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('interativa_pip_ix_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6-ix-ora_rede-interativa-pip_{}-0{}-2021.pdf".format(s,i))
#REDE COMPUNET
    if doc[i].find('compunet_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4_rede-compunet_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('compunet_IPV6') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6_rede-compunet_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('compunet_CDN_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv4-cdn_rede-compunet_{}-0{}-2021.pdf".format(s,i))

    if doc[i].find('compunet_CDN_IPV4') >=0:
        procurar = doc[i]
        os.rename(procurar,"relatorio_link-ipv6-cdn_rede-compunet_{}-0{}-2021.pdf".format(s,i))

        
        
    