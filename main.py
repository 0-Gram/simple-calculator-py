lanjutkan_program = True

while lanjutkan_program:
    print("\033[94m" + "=" * 42)
    print("\033[94mProgram Kalkulator Sederhana Dengan Python")
    print("\033[94m" + "=" * 42)

    input1 = float(input("Masukan Angka: "))
    operator = input("Pilih Operator (x, /, -, +): ")
    input2 = float(input(f"Angka {input1} Mau DI {operator} Berapa? :"))

    if operator == "x":
        hasil = input1 * input2 
    elif operator == "/":
        hasil = input1 / input2 
    elif operator == "-":
        hasil = input1 - input2 
    elif operator == "+":
        hasil = input1 + input2 
    else:
        print("Masukan Input Yang Benar Dongggg!\n")
        continue  # Melanjutkan ke iterasi berikutnya jika operator tidak valid

    print(f"\nHasil Dari {input1} Di {operator} {input2} Adalah : {hasil}\n")

    pilihan = input("Apakah Anda ingin melanjutkan (y/n)? ")
    lanjutkan_program = pilihan.lower() == 'y'

print("Program Selesai, Gak usah terima kasih:v")
