# Vypište prvních N členů následujících posloupností:
# lichá čísla
def kek_1(N):
    for i in range(1, N, 2):
        print(i)
        
# mocniny dvojky
def kek_2(N):
    for i in range(1, N):
        print(2**i)
        
# druhé mocniny   ????? of what 
# Fibonacciho čísla
def fibonachi(N):
    start = [0,1]
    for i in range(2, N):
        start.append(start[i-1] + start[i-2])
    print(start)
    
# Collatzova posloupnost
"""
vezmi přirozené číslo:
pokud je sudé, vyděl jej dvěma
pokud je liché, vynásob jej třemi a přičti jedničku
tento postup opakuj, dokud nedostaneš číslo jedna
"""
def collatz(x, N):  # x je číslo z kt. to začne, N kolko sa má zobrazit
    list = []
    while x != 1:
        if x % 2 == 0: # sudé
            x = x / 2
        else:
            x = x * 3 + 1
        list.append(int(x))
    if N < len(list):
        print(list[0:N])
    else:
        print(list)
# prvočísla
# obecná aritmetická posloupnost
def arit_posl(x, n):    # x je velkost posunu, n kolko zobrazi
    for i in range(1, n*x + 1, x):
        print(i)
        
# obecná geometrická posloupnost

# Pro zadané přirozené číslo N vypište:
# seznam všech jeho dělitelů
def divisors(n):
    list = []
    for i in range(1, n + 1):
        if n % i == 0:
            list.append(i)
    return list
print(divisors(100))

# počet jeho dělitelů
def divisors_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
print(divisors_count(100))

# největšího dělitele (menšího než N)
def max_divisor(n):
    list = []
    for i in range(1, n + 1):
        if n % i == 0:
            list.append(i)
    return list[len(list)-2]
print(max_divisor(100))

# ciferný součet N
# faktoriál čísla N
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
print(recur_factorial(5))

# číslo N zapsané pozpátku
# nejmenší prvočíslo větší než N
# informaci o tom, zda je N druhou mocninou přirozeného čísla
# informaci o tom, zda jde N vyjádřit jako součet druhých mocnin přirozených čísel
# informaci o tom, zda je N prvočíslo
# zápis čísla N ve dvojkové soustavě
# zápis čísla N v šestnáctkové soustavě

# Pro zadaná přirozená čísla A, B vypište:
# informaci o tom, které z nich je větší a o kolik
# informaci o tom, zda jedno z nich dělí to druhé
# počet jejich společných dělitelů
# jejich největší společný dělitel
# jejich nejmenší společný násobek
# počet prvočísel v intervalu (A, B)
# seznam všech druhých mocnin v intervalu (A, B)

# Pro zadaný text S vypište:
# informaci o tom, zda text obsahuje víckrát A nebo B
# informaci o tom, zda jde o palindrom
# první písmena slov v textu
# poslední slovo v textu
# nejdelší slovo v textu

# Pro zadaný text S a číslo N vypište:
# text S, ve kterém je každé písmeno zopakováno N krát
# text S, ve kterém jsou vynechána písmena na pozicích dělitelných N
# text S zašifrovaný Caesarovou šifrou (posun písmen v abecedě o 3)
# text S zašifrovaný transpoziční šifrou, která otočí vždy skupiny N po sobě jdoucích písmen
# text S, ve kterém je každé N-té písmeno nahrazeno za X
# N-té slovo z textu

# Pro zadané texty A, B vypište:
# který z nich obsahuje víc znaků X
# písmeno, které se vyskytuje v textu A, ale nevyskytuje se v textu B
# zda jsou texty vzájemné přesmyčky
# zda texty obsahují stejná písmena
# zazipuje řetězce ("prase" + "kos" = "pkroasse")

# Pro zadaný seznam čísel S vypočítejte:
# medián S
# průměr S
# součin kladných čísel v S
# počet prvočísel v S
# třetí nejvyšší číslo v S
# nejvyšší součet dvou po sobě jdoucích čísel v S

# Napište funkci, která pro zadaný seznam čísel S vrátí seznam obsahující:
# čísla v seznamu S seřazená od nejvyššího po nejmenší
# lichá čísla v seznamu S seřazená od nejmenšího po největší 
# všechna čísla v S vynásobená třemi
# každé druhé číslo z S
# čísla na sudých pozicích vynásobená pěti, čísla na lichých pozicích vydělená pěti
# čísla z S, která jsou dělitelná pěti
# dvojnásobný počet čísel, každé číslo z S je duplikováno

# Pomocí "textové grafiky" ("ascii art") vykreslete (o zadané velikosti N):
# trojúhelník
# kosočtverec
# kruh
# šachovnici
# spirálu
# domeček
# vlnovku
# písmena abecedy "ve velkém"

# Pro zadané N vypište tabulku čísel velikosti NxN obsahující:
# tabulka sčítání
# tabulka sčítání modulo N
# tabulka násobení
# jedničky po okrajích, dvojky vedle okrajů a tak dále

# Pro zadanou matici čísel (seznam seznamů) vypište:
# souřadnice největšího prvku
# řádek s největším součtem
# transponovanou matici

# Pro zadaný text vypište:
# písmena seřazená podle počtu výskytů v textu
# slova seřazená podle počtu výskytů v textu
# nejčastější bigram (dvojice po sobě jdoucích písmen)

# Pomocí želví grafiky vykreslete:
