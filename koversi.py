while True:
    print("\n=== MENU OPERASI MATRIKS ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        A = [
            [1, 2],
            [3, 4]
        ]

        B = [
            [5, 6],
            [7, 8]
        ]

        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])
            C.append(row)

        print("C = A + B")
        for r in C:
            print(r)

    elif pilih == "2":
        A = [
            [1, 2],
            [3, 4]
        ]

        B = [
            [5, 6],
            [7, 8]
        ]

        C = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] - B[i][j])
            C.append(row)

        print("C = A - B")
        for r in C:
            print(r)

    elif pilih == "3":
        A = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        B = [
            [7, 8],
            [9, 10],
            [11, 12]
        ]

        C = []
        for i in range(len(A)):          # baris A
            row = []
            for j in range(len(B[0])):   # kolom B
                total = 0
                for k in range(len(A[0])):  # kolom A = baris B
                    total += A[i][k] * B[k][j]
                row.append(total)
            C.append(row)

        print("C = A * B")
        for r in C:
            print(r)

    elif pilih == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
