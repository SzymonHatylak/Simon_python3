#Obliczanie cen z podatkiem vat

vat = 1.23
jablka_netto = 2.5
gruszki_netto = 3
chleb_netto = 100

jablka_brutto = jablka_netto * vat
gruszki_brutto = gruszki_netto * vat
chleb_brutto = chleb_netto * vat

print ("Chleb z vatem:",chleb_brutto ,"\nGruszki z vatem:",gruszki_brutto ,"\nJablka z vatem:" , jablka_brutto)
print ("\n")
print (f"Chleb z vatem: {chleb_brutto}" ,f"\nGruszki z vatem: {gruszki_brutto}" ,f"\nJablka z vatem: {jablka_brutto}")

netto = chleb_brutto / vat
print (netto)

#a = b = c = False
a = 5; b = 6; c = 6
print(a , b , c)

x = 5
x **=2
print(x)

dlugiString = """To jest badzo dlugi tekst To jest badzo dlugi tekst
To jest badzo dlugi tekst To jest badzo dlugi tekst
To jest badzo dlugi tekst To jest badzo dlugi tekst
To jest badzo dlugi tekst"""

"""
dlugiString = "To jest badzo dlugi tekst To jest badzo dlugi tekst\
To jest badzo dlugi tekst To jest badzo dlugi tekst\
To jest badzo dlugi tekst To jest badzo dlugi tekst\
To jest badzo dlugi tekst"
"""
print (dlugiString)

imie = "Anna"
print (imie)
print (imie[0])
print (imie[3])
print (imie[-1])
print (imie[:])
print (imie[1:])
print (imie[:-1])
print (imie[0:3])

