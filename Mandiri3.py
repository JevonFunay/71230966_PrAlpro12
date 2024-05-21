try:
    text1 = input("Nama Text 1 :")
    text2 = input("Nama Text 2 :")
    with open(text1, 'r') as file1, open(text2, 'r') as file2:
        file1 = file1.read().lower().split()
        file2 = file2.read().lower().split()
    semua = set(file1)&set(file2)
    for i in sorted(semua):
        print(i)
except:
    print("Text tidak ditemukan/Text salah(typo)!")