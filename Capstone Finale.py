from tabulate import tabulate

data = [
        {'ID':10001, 'Nama': 'Maxi Clean', 'Kategori' : 'Laundry', 'Lokasi' : 'Jakarta', 'Nomor Telp':6292240926730, 'Rating' : 5},
        {'ID':10002, 'Nama': 'Kenangan Spa','Kategori' : 'Pijat', 'Lokasi' : 'Bandung', 'Nomor Telp':6287439565046, 'Rating' : 4.5},
        {'ID':10003,'Nama': 'Top Laundry', 'Kategori' : 'Laundry', 'Lokasi' : 'Bandung', 'Nomor Telp':6295981221148, 'Rating' : 4.6},
        {'ID':10004,'Nama': 'Olive Chicken', 'Kategori' : 'Restoran', 'Lokasi' : 'Jogja', 'Nomor Telp':6289762911576, 'Rating' : 4.9},
        {'ID':10005, 'Nama': 'Healing Spa','Kategori' : 'Pijat', 'Lokasi' : 'Jakarta', 'Nomor Telp':6234309381503, 'Rating' : 4.5},
        {'ID':10006,'Nama': 'Serenity Spa', 'Kategori' : 'Pijat', 'Lokasi' : 'Bandung', 'Nomor Telp':6251735077098, 'Rating' : 4.8},
        {'ID':10007, 'Nama': 'Pasti Bersih', 'Kategori' : 'Laundry', 'Lokasi' : 'Bandung', 'Nomor Telp':6237570926730, 'Rating' : 4.3},
        {'ID':10008,'Nama': 'Agung Motor', 'Kategori' : 'Bengkel', 'Lokasi' : 'Jakarta', 'Nomor Telp':6218833833214, 'Rating' : 4.8},
        {'ID':10009,'Nama': 'Auto Tuntas', 'Kategori' : 'Bengkel', 'Lokasi' : 'Malang', 'Nomor Telp':6275832982663, 'Rating' : 4.5},
        {'ID':10010, 'Nama': 'Mager Londre', 'Kategori' : 'Laundry', 'Lokasi' : 'Jakarta', 'Nomor Telp':6292240975700, 'Rating' : 3.2},
        {'ID':10011,'Nama': 'Pagi Siang', 'Kategori' : 'Restoran', 'Lokasi' : 'Jakarta', 'Nomor Telp':6280095285013, 'Rating' : 3.9},
        {'ID':10012,'Nama': 'Mie Gacoan', 'Kategori' : 'Restoran', 'Lokasi' : 'Malang', 'Nomor Telp':6249201854145, 'Rating' : 4.9},
        {'ID':10013,'Nama': 'Auto Bersih', 'Kategori' : 'Laundry', 'Lokasi' : 'Jogja', 'Nomor Telp':6289021299724, 'Rating' : 4.4},
        {'ID':10014,'Nama': 'Sate Senayan', 'Kategori' : 'Restoran', 'Lokasi' : 'Jakarta', 'Nomor Telp':6284024729567, 'Rating' : 4.4},
        {'ID':10015,'Nama': 'Dimas Otomotif', 'Kategori' : 'Bengkel', 'Lokasi' : 'Malang', 'Nomor Telp':6291880910855, 'Rating' : 4.7},
        {'ID':10016,'Nama': 'So Clean', 'Kategori' : 'Laundry', 'Lokasi' : 'Jogja', 'Nomor Telp':6289021234756, 'Rating' : 4.1},
        {'ID':10017,'Nama': 'Bakso Joss', 'Kategori' : 'Restoran', 'Lokasi' : 'Jakarta', 'Nomor Telp':6286719375028, 'Rating' : 3}
        ]

# Read = Done

def read_data(data):
    print(tabulate(data, headers='keys', tablefmt='pretty'))


def input_alfabet (prompt):
    while True :
        huruf = input(prompt)
        if huruf.replace(" ","").isalpha() :
                return huruf.title()
        else :
                print ("Inputan harus huruf")

def input_numerik (prompt):
      while True:
            angka = input (prompt)
            if angka.replace(" ",'').isdigit() :
                  return int(angka)
            else :
                  print ("Inputan harus bilangan bulat")

def inp_rating (prompt):
      while True:
            try: 
                  req_rating = float(input('masukan rating antara 1 -5 '))
                  if req_rating >= 1 and req_rating <= 5 :     # 1 < = x <= 5
                        return float(req_rating)
                  else :
                        print ("Inputan harus antara 1 - 5")
            except ValueError: 
                  print ("Mohon masukkan angka antara 1-5")

def admin_customer ():
     while True :
            menu_1 = input_alfabet(' apa yang ingin anda lakukan hari ini ? jika ingin login sebagai admin masukan y, dan n sebagai customer (y/n)').lower().strip().replace(" ",'')
            password = 1234567
            if menu_1 == 'y' :
                  while True :
                        inp_password = input_numerik ('masukan password anda')
                        if inp_password == password :
                              print ('selamat datang admin')
                              break
                        else :
                              print ('password salah')
                  break
            elif menu_1 == 'n' :
                  print ('selamat datang customer yang budiman')
                  break
            else :
                  print ('inputan salah. Ketik "y" jika anda admin, "n" jika anda customer')
                  

def print_menu_create ():
    print('''
            Mohon Masukan Informasi Di Bawah ini :
          Nama Bisnis/Perusahaan
          Kategori Usaha
          Lokasi (Kota)
          Nomor Telp
          rating antara 1-5
            ''')

def is_duplicate(new_entry, existing_data):
    for item in existing_data:
        if item['Nama'] == new_entry['Nama'] and item['Kategori'] == new_entry['Kategori'] and item['Lokasi'] == new_entry['Lokasi']:
            return True
    return False



# Create Data = Done

def create_data():
    print('Anda akan menambahkan data baru.')
    read_data(data)
    input_data = int(input("Berapa Banyak Data Yang Ingin Ditambahkan? "))
    list_new_data = []
    new_id = data[-1]["ID"]

    for i in range(input_data):
        new_id += 1
        new_nama = input_alfabet("Masukan Nama Bisnis/Perusahaan: ")
        new_kategori = input_alfabet("Masukan Kategori Usaha: ")
        new_lokasi = input_alfabet("Masukan Lokasi (Kota): ")
        new_hp = input_numerik("Masukkan Nomor Telp: ")
        new_rating = inp_rating("Masukan rating antara 1-5: ")

        new_data = {
            'ID': new_id,
            'Nama': new_nama,
            'Kategori': new_kategori,
            'Lokasi': new_lokasi,
            'Nomor Telp': new_hp,
            'Rating': new_rating
        }

        if is_duplicate(new_data, data):
            print("Data duplikat ditemukan. Data tidak ditambahkan.")
        else:
            list_new_data.append(new_data)
            data.extend(list_new_data)
            print('Anda akan menambahkan data dibawah ini:')
            read_data(list_new_data)
            print('Selamat, data baru telah ditambahkan ke dalam list.')
            read_data(data)





# Update = done

def update_data () :
      id_to_update = input_numerik('masukan id dari bisnis yang ingin anda update : ')
      for index, busines in enumerate(data) : # 0,{..} 1,{...}
            found = True
            if busines ["ID"] == id_to_update :
                  read_data([data[index]])
                  print ('''
                        data apa yang ingin anda update ?
                        (Nama/Kategori/Lokasi/Nomor Telp/Rating
                        ''')
                  update_field = input_alfabet ('masukkan kolom mana ingin anda update datanya (ex; Nama, Kategori, Lokasi, No Telp, Rating)')
                  if update_field in list(busines.keys()) : # ['ID','Nama', ...]
                        if update_field in ["Nomor Telp", "Rating"]:
                              try:
                                    if update_field == "Nomor Telp":
                                          new_data = input_numerik(f'Masukkan data baru untuk {update_field}: ')
                                          new_data = int(new_data)
                                          break  
                                    else : 
                                          new_data = input_numerik(f'Masukkan data baru untuk {update_field}: ')
                                          new_data = float(new_data)
                                          break
                              except ValueError:
                                    print(f"Data baru untuk {update_field} harus berupa angka.")
                                    break
                        else:
                              new_data = input_alfabet(f'Masukkan data baru untuk {update_field}: ')
                        busines[update_field] = new_data # dict['kolom_yg_diambil'] = 'new_data' -> replace  
                        data_updated = [data[index]] # [{...}] -> dictionary dibungkus list
                        read_data(data_updated)    
                        print(f'Data {update_field} berhasil diperbarui menjadi {new_data}.')
                  else:
                        print('Kolom yang Anda masukkan tidak valid.')
                        break
            else:
                 found = False 
      if found == False:
           print("ga ketemu")




# Delete = done

def delete_data():
    while True:
        id_to_delete = input_numerik('Masukkan ID yang ingin di hapus: ')
        if id_to_delete < 10001 or id_to_delete > data [-1]['ID']:
            print('data tidak ditemukan')
        else:
            delete_item = [data[id_to_delete - 10001]] # [{....}]
            read_data(delete_item)
            print (f'Yakin ingin menghapus data ID = {id_to_delete} (y/n) atau \'u\' ke menu utama:')
            konfirmasi = input_alfabet(f'Yakin ingin menghapus data ID = {id_to_delete} (y/n) atau \'u\' ke menu utama: ')
            if konfirmasi.lower() == 'y':
                del data[id_to_delete - 10001] # del data[0] 
                read_data (data)
                print('Data berhasil dihapus')
                break
            elif konfirmasi.lower() == 'n':
                read_data(data)
                print('Penghapusan data dibatalkan.')
                break
            elif konfirmasi.lower() == 'u':
                read_data(data)
                break





#Filter = done

list_found = []
list_found_2 = []
def filter_data () :
    global list_found, list_found_2
    list_found.clear()
    while True :
        inputan = input_alfabet('Apa yang ingin anda cari ? (exp. Jakarta, Restoran, Laundry dll)')
        for dict in data: # setiap dict akan looping -> {'nama':'aa', 'umur': 20, 'asal': 'jakarta'}
            for key in dict.keys(): # looping ['nama','umur','asal']
                # untuk yang KOLOM NON NUMERIK 
                if key in ['Nama', 'Kategori', 'Lokasi']: # if 'nama' in ['nama','asal']
                    if inputan == dict[key]: # if '20'(inputan) == dict['nama']
                        list_found.append(dict)
                        break
                # untuk yang KOLOM NUMERIK
                elif key in ['ID', 'Nomor Telp']: # looping kedua: if 'umur' in ['umur']
                    try:
                        if int(inputan) == dict[key]: # if int('20') == dict['umur] (20)
                            list_found.append(dict) # {'nama':'aa', 'umur': 20, 'asal': 'jakarta'}
                            break
                    except:
                        continue
                elif key in ['Rating']:
                    try:
                        if float(inputan) ==dict[key]:
                            list_found.append(dict) 
                            break
                    except:
                        break                  
        if len(list_found) == 0:
            print('yang anda cari tidak ada')
        else:
            print('Berikut data yang telah anda Filter')
            print(tabulate(list_found, headers='keys', tablefmt='pretty'))
        menu_2 = input('Apakah mau filter lagi (y/n)').lower().strip()
        print ('Apakah mau filter lagi (y/n)')
        if menu_2 == 'y':
            inputan2 = input_alfabet('Apa yang ingin anda cari lagi ? (exp. Jakarta, Restoran, Laundry dll)')
            for dict2 in list_found: # setiap dict akan looping -> {'nama':'aa', 'umur': 20, 'asal': 'jakarta'}
                for key in dict2.keys(): # looping ['nama','umur','asal']
                    # untuk yang KOLOM NON NUMERIK 
                    if key in ['Nama', 'Kategori', 'Lokasi']: # if 'nama' in ['nama','asal']
                        if inputan2 == dict2[key]: # if '20'(inputan) == dict['nama']
                            list_found_2.append(dict2)
                            break
                    # untuk yang KOLOM NUMERIK
                    elif key in ['ID', 'Nomor Telp']: # looping kedua: if 'umur' in ['umur']
                        try:
                            if int(inputan2) == dict2[key]: # if int('20') == dict['umur] (20)
                                list_found_2.append(dict2) # {'nama':'aa', 'umur': 20, 'asal': 'jakarta'}
                                break
                        except:
                            continue
                    elif key in ['Rating']:
                        try:
                            if float(inputan2) ==dict2[key]:
                                list_found_2.append(dict2) 
                                break
                        except:
                             break
            print(tabulate(list_found_2, headers='keys', tablefmt='pretty'))           
        elif menu_2 == 'n':
            print('Terima Kasih')
            return menu_2
        else:
            print('Input yang anda masukkan salah')
            break
        menu_3 = input('Apakah mau sorting data tersebut (y/n)').lower().strip()
        print ('Apakah mau sorting data tersebut (y/n)')
        if menu_3 == 'y':
            sorting_data(list_found_2)
            break
        elif menu_3 == 'n':
            print('Terima Kasih')
            return
        




def sorting_data(data):
    pilih_kolom = input_alfabet('Apa yang mau diurutkan? (Nama, Kategori, Lokasi, Nomor Telp, Rating): ')
    pilih_urutan = input_alfabet('Urutkan berdasarkan apa? ketik "A"(ascending) atau "D"(descending): ')
    
    if pilih_kolom not in ['ID', 'Nama', 'Kategori', 'Lokasi', 'Nomor Telp', 'Rating']:
        print("Kunci pengurutan tidak valid, hasil tidak akan diurutkan.")
        return

    try:
        if pilih_urutan == 'A':
            sorted_data = sorted(data, key=lambda x: x[pilih_kolom])
        elif pilih_urutan == 'D':
            sorted_data = sorted(data, key=lambda x: x[pilih_kolom], reverse=True)
        else:
            print("Pilihan urutan tidak valid.")
            return
        print('Berikut hasil sorting data anda')
        print(tabulate(sorted_data, headers='keys', tablefmt='pretty'))
    except KeyError:
        print("Kunci pengurutan tidak valid, hasil tidak akan diurutkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")



def print_main_menu():
    print('''
            Selamat Datang
            APA YANG INGIN ANDA LAKUKAN HARI INI ?:
                1. LOGIN SEBAGAI USER 
                2. LOGIN SEBAGAI ADMIN
                3. Exit
            ''')


def print_menu_Admin ():
    print('''
            Selamat Datang Admin
            ADMIN MAU NGAPAIN HARI INI ? :
                1. Create Data
                2. Update Data
                3. Delete Data
                4. Filter Data
                5. Keluar
            ''')

def lanjut_loop2():
    while True:
        menu_3 = input('Apakah mau lanjut? (y/n)').lower().strip()
        if menu_3 == 'y':
            return menu_admin()
        elif menu_3 == 'n':
            print('Terima Kasih')
            break
        else:
            print('Input yang anda masukkan salah')
            break


def menu_admin():
      while True:
        print_menu_Admin ()
        output_admin = input('ADMIN MAU NGAPAIN HARI INI ? :')   # ADMIN MAU NGAPAIN HARI INI ?:
        if output_admin == '1':
                create_data()
                lanjut_loop2()
                break
        elif output_admin == '2':
                update_data()
                lanjut_loop2()
                break
        elif output_admin == '3':
                delete_data()
                lanjut_loop2()
                break
        elif output_admin == '4':
                filter_data()
                lanjut_loop2()
                break
        elif output_admin == '5':
                print ('Baik, terimakasih and have a nice day')
                break
        else:
                print ('Maaf, pilihan tidak tersedia dan terimakasih ')
                break


def main_menu():
    while True:
        print_main_menu ()
        output = input('APA YANG INGIN ANDA LAKUKAN HARI INI ? 1.LOGIN SEBAGAI USER/ 2.LOGIN SEBAGAI ADMIN / 3.EXIT') # APA YANG INGIN ANDA LAKUKAN HARI INI ?
        if output == '1':
            print ('Selamat datang pada Yellow Page, apa yang ingin anda lakukan/cari') 
            read_data(data) #
            while True :
                menu_filter = input('Apakah mau melakukan filter data? (y/n)').lower().strip()
                if menu_filter == 'y':
                    filter_data ()
                    break
                elif menu_filter == 'n':
                    print ('Terima kasih') # disini udh berhenti jika "no"
                    break
                else:
                    print ('Input yang anda masukkan salah, mohon masukkan input yang benar. y = melakukan filter, n = tidak melakukan filter') # akan ngeloop ke menu_filter lagi

        elif output == '2':
            while True :
                menu_1 = input_alfabet(' anda akan login sebagai admin. Jika yakin untuk login sebagai admin masukan y, dan n untuk kemenu utama').lower().strip().replace(" ",'')
                password = 1234567
                if menu_1 == 'y' :
                    while True :
                            inp_password = input_numerik ('masukan password anda')
                            if inp_password == password :
                                print ('selamat datang admin')
                                read_data(data)
                                break
                            else :
                                print ('input password salah, masukkan password yang benar')
                    break
                elif menu_1 == 'n' :
                    print ('YELLOW PAGE')
                    return print_main_menu ()
                else :
                    print ('inputan salah. Ketik "y" jika anda admin, "n" jika anda customer')
            menu_admin()
            break
        elif output == '3':
             print ('Terimakasih')
             break
        else :
             print ('inputan salah. Ketik "1" jika anda customer, "2" jika anda admin, "3" jika anda ingin keluar')

main_menu()
