nama_file = "soal.txt"
with open(nama_file, "r") as file:
    hasil= file.readlines()
for soal in hasil:
    soalan = soal.strip().split("||")
    if len(soalan) == 2:
        pertanyaan, benar = soalan
    else:
        print("Format soal tidak sesuai.")
        continue
    pertanyaan = pertanyaan.strip().rstrip("=")
    print(f"{pertanyaan} =\nJawab: ", end="")
    jawaban = input().strip()
    if jawaban.lower() == benar.lower().strip():
        print("Jawaban benar!\n")
    else:
        print("Jawaban salah!\n")