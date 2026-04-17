def fibonacci(n):
    a, b = 1, 1
    print("Barisan fibonacci sebanyak", n, "suku :")
    for i in range(n):
        print(a, end=", ")
        a, b = b, a + b
    print("\n")


def perkalian(m, n):
    hasil = m * n
    print(f"Hasil dari {m} x {n} = {hasil}\n")


while True:
    print("Menu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah suku: "))
        fibonacci(jumlah)

    elif pilihan == "2":
        m = int(input("Masukkan suatu bilangan bulat (M): "))
        n = int(input("Masukkan suatu bilangan pengali (N): "))
        perkalian(m, n)

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!\n")
