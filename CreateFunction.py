def convert_temperature(value, unit):
    if unit == 'C':  # Celsius ke Fahrenheit
        fahrenheit = (value * 9/5) + 32
        return f"{value}°C setara dengan {fahrenheit:.2f}°F"
    elif unit == 'F':  # Fahrenheit ke Celsius
        celsius = (value - 32) * 5/9
        return f"{value}°F setara dengan {celsius:.2f}°C"
    else:
        return "Unit tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

def input_temperature():
    try:
        value = float(input("Masukkan nilai suhu: "))
        unit = input("Masukkan unit suhu ('C' untuk Celsius atau 'F' untuk Fahrenheit): ").upper()
        print(convert_temperature(value, unit))
    except ValueError:
        print("Nilai yang dimasukkan tidak valid. Harap masukkan angka.")

# Contoh penggunaan
input_temperature()
