def process_data(data):
    try:
        # Misalnya, kita coba mengonversi data ke integer
        value = int(data)
        
        # Misalnya kita ingin membagi nilai
        result = 100 / value
        
        # Misalnya kita ingin mengakses elemen list
        my_list = [10, 20, 30]
        print(my_list[value])  # Ini bisa menyebabkan IndexError
    except ValueError:
        print("Error: Data tidak dapat dikonversi menjadi integer.")
    except ZeroDivisionError:
        print("Error: Tidak dapat membagi dengan nol.")
    except IndexError:
        print("Error: Indeks di luar jangkauan list.")
    except Exception as e:
        print(f"Error tidak terduga: {e}")

# Uji fungsi
process_data("ojan")  # Menghasilkan ValueError
process_data("0")     # Menghasilkan ZeroDivisionError
process_data("5")     # Menghasilkan IndexError