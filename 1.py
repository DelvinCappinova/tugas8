def perbandingan(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        baris1 = f1.readline().strip()
        baris2 = f2.readline().strip()
        while baris1 or baris2:
            if baris1 != baris2:
                print(f"  File 1: {baris1}")
                print(f"  File 2: {baris2}")
            line1 = f1.readline().strip() if baris1 else None
            line2 = f2.readline().strip() if baris2 else None
            break
perbandingan('file1.txt', 'file2.txt')