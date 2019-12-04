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
import re
def freq_analysis(text):  # Naivne vypéše počet slov, upraviť podla potreby 
    word_list = re.split(" ", text)
    freq_dict = {}
    for word in word_list:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] = freq_dict.get(word) + 1
    ordered_words = sorted(freq_dict)
    for word in ordered_words:
        print(word, freq_dict[word])

dummy = """Monty Python and Monty Python all over here."""
freq_analysis(dummy)
# informaci o tom, zda jde o palindrom

def reverse(s):
    return s[::-1]
def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
print(isPalindrome("malayalam"))

# první písmena slov v textu
def first_letter(text):
    string_text = re.split(" ", text)
    for word in string_text:
        print(word[0])
first_letter(dummy)

# poslední slovo v textu
def last_word(text):
    string_text = re.split(" ", text)
    print(string_text[len(string_text)-1])
last_word(dummy)

# nejdelší slovo v textu
def longest_word(text):
    longest = ""
    string_text = re.split(" ", text)
    for word in string_text:
        if int(len(word)) > len(longest):
            longest = word
    print(longest)
longest_word(dummy)

# Pro zadaný text S a číslo N vypište:
# text S, ve kterém je každé písmeno zopakováno N krát
def xxx(n):
    print("s"* n)
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
def median(list):
    new_list = sorted(list)
    if len(new_list) % 2 == 1:
        return new_list[int(round(len(new_list)/2)-1)]
    else:
        return (new_list[int(round(len(new_list)/2))] + new_list[int(round(len(new_list)/2)-1)]) / 2
my_list = [1,2,3,4,5,6,7,8]
print(median(my_list))

# průměr S
# součin kladných čísel v S
# počet prvočísel v S
# třetí nejvyšší číslo v S  --> sorted(list) -> [len(list)-3]
# nejvyšší součet dvou po sobě jdoucích čísel v S

# Napište funkci, která pro zadaný seznam čísel S vrátí seznam obsahující:
# čísla v seznamu S seřazená od nejvyššího po nejmenší  ->sorted() / .sort
# lichá čísla v seznamu S seřazená od nejmenšího po největší 
# všechna čísla v S vynásobená třemi  --> loop   for i in range(len(s))   \n   new_list.append(list[i]*3)
# každé druhé číslo z S   for i in range(0, len(s), 2)    new_list.append(list[i])
# čísla na sudých pozicích vynásobená pěti, čísla na lichých pozicích vydělená pěti
def xyz(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] = my_list[i] * 5
        else:
            my_list[i] = my_list[i] * 3
    print(my_list)
xyz(my_list)
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
# souřadnice největšího prvku  -> loop in loop  a do vairable is vzdy uložíš novu naj. premmenu, po skončení oboch cyklov list.index(naj hodnota)
# řádek s největším součtem
# transponovanou matici

# Pro zadaný text vypište:
# písmena seřazená podle počtu výskytů v textu
# slova seřazená podle počtu výskytů v textu
# nejčastější bigram (dvojice po sobě jdoucích písmen)

# Pomocí želví grafiky vykreslete:
