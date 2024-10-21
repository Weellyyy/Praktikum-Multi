#1
def perubahansuhu(nilai_suhu, satuan_suhu):
    if satuan_suhu.upper() == 'C':
        
        hasil = (nilai_suhu * 9/5) + 32
        return f"{nilai_suhu}°C sama dengan {hasil:.2f}°F"
    elif satuan_suhu.upper() == 'F':
       
        hasil = (nilai_suhu - 32) * 5/9
        return f"{nilai_suhu}°F sama dengan {hasil:.2f}°C"
    else:
        return "Satuan suhu tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."


nilai_suhu = float(input("Masukkan nilai suhu: "))
satuan_suhu = input("Masukkan satuan suhu (C atau F): ")


hasil_konversi = perubahansuhu(nilai_suhu, satuan_suhu)
print(hasil_konversi)


