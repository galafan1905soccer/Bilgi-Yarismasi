print("Bilgi yarismasina hosgeldiniz ! ")

isim=input("oyuncunun adi: ")

puan=0

sorular =[
["osmanlinin en sonki baskenti neressidir ?","istanbul"],
["bir haftada kac saat vardir ? ","168"],
["Pythonda ekrana yazi yazdiran fonksiyonun ismi nedir","print" ],
["Dunyanin dogal uydusu nedir ? ","ay"]

]

for soru in sorular:
    print("\n"+soru[0])
    cevap = input("cevabin:").strip().lower()

if cevap == soru [1]:
    print("Dogru! +10 puan")
    puan += 10
else:
    print("Dogru! +10 puan")
    puan += 10

maksimum_puan = len(sorular)*10

print(f"\n Tebrikler {isim},yarismayi tamamladin")

print(f"Puanin : {puan}/{maksimum_puan}")


