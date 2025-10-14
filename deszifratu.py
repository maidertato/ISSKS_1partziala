# Maider Tato Herrera
# deszifratu.py
# Counter erabiliz --> Mapen bidez egingo dugu bilaketa
from collections import Counter

mezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ DIEZ DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. Nueva Zelanda XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PLUMA TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

mezua = mezua.upper()

# Testuko ordena (frogak egin ondoren)
ohikoenak = ["E","A","R","O","I","N","L","D","C","U","T","S","M","P","B","F","Q","J","Y","V","G","H","X","Z","Ñ","Y","W"]

# Hizki-maiztasunak (Counter erabiliz)
kont = Counter(ch for ch in mezua if ch.isalpha())
elementuak = kont.most_common()

print(f"{len(kont)} hizki desberdin aurkitu dira.")
print("Hizkien maiztasuna (handienetik txikienera):")
for hizkia, kop in elementuak:
    print(f"{hizkia}: {kop}")

# Map bat: enkriptatutako hizkitik ordezkatu beharreko hizkira. Posiziorik ez badago, ez aldatu
mapa_ordeztu = {}
for pos, (hizkia, _) in enumerate(elementuak):
    if pos < len(ohikoenak):
        mapa_ordeztu[hizkia] = ohikoenak[pos]
    else:
        mapa_ordeztu[hizkia] = hizkia

# Testua ordezkatu mapa erabiliz 
mezu_desenkriptatu = "".join(
    mapa_ordeztu[ch] if ch.isalpha() else ch
    for ch in mezua
)

print("\nMezua desenkenkriptatuta:")
print(mezu_desenkriptatu)
