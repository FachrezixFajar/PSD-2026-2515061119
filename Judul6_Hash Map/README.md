TUGAS AKHIR JUDUL 6

a. Judul Program : Fungsi Binary Search Tree Dalam Sistem Level Boss Di Wuthering Waves

b. Deskripsi Singkat : Program tersebut berfungsi sebagai **sistem inventory dalam game Zenless Zone Zero (ZZZ)** menggunakan struktur data **HashMap Separate Chaining**. Pengguna dapat menambahkan item, mencari item berdasarkan key, menghapus item, serta menampilkan seluruh isi inventory. Setiap item disimpan menggunakan pasangan **key** dan **value**, di mana key berfungsi sebagai ID item, sedangkan value berisi nama item seperti W-Engine, Drive Disc, material, atau item lainnya. Jika beberapa key menghasilkan index hash yang sama, data tetap dapat disimpan menggunakan metode **separate chaining**, yaitu dengan linked list pada index yang sama. Cara kerja program ini mirip seperti sistem penyimpanan item dalam game, sehingga inventory dapat dikelola dengan lebih teratur dan mudah dicari.

c. Source Code :

<img width="1372" height="3522" alt="code jd 6" src="https://github.com/user-attachments/assets/2f602020-d94d-4f13-8ded-45a59816edae" />



Baris 1 Membuat class bernama `Node` yang digunakan untuk menyimpan satu data item dalam inventory ZZZ.<br/>
Baris 2 Membuat fungsi konstruktor `__init__` yang otomatis dijalankan saat objek `Node` dibuat.<br/>
Baris 3 Menyimpan nilai `key` ke dalam variabel `self.key`. Pada program ini, `key` digunakan sebagai ID item.<br/>
Baris 4 Menyimpan nilai `value` ke dalam variabel `self.value`. Pada program ini, `value` berisi nama item ZZZ.<br/>
Baris 5 Membuat variabel `self.next` dengan nilai awal `None`, yang digunakan untuk menunjuk node berikutnya jika terjadi collision.<br/>
Baris 6 Baris kosong sebagai pemisah agar kode lebih rapi.<br/>
Baris 7 Baris kosong sebagai pemisah antara class `Node` dan class berikutnya.<br/>
Baris 8 Membuat class bernama `HashMapSeparateChaining` yang digunakan untuk mengatur data inventory menggunakan HashMap.<br/>
Baris 9 Membuat fungsi konstruktor `__init__` dengan parameter `size=10`, artinya ukuran awal hash table adalah 10.<br/>
Baris 10 Menyimpan ukuran hash table ke dalam variabel `self.SIZE`.<br/>
Baris 11 Membuat list bernama `self.table` dengan isi awal `None` sebanyak ukuran hash table.<br/>
Baris 12 Baris kosong sebagai pemisah antar fungsi.<br/>
Baris 13 Membuat fungsi `hash_function()` dengan parameter `key`, digunakan untuk menentukan index penyimpanan item.<br/>
Baris 14 Menghitung index hash dari key menggunakan operasi modulo agar hasil index tetap berada dalam ukuran tabel.<br/>
Baris 15 Baris kosong sebagai pemisah antar fungsi.<br/>
Baris 16 Membuat fungsi `insert()` dengan parameter `key` dan `value`, digunakan untuk menambahkan item ke inventory.<br/>
Baris 17 Menentukan index penyimpanan item dengan memanggil fungsi `hash_function()`.<br/>
Baris 18 Membuat variabel `current` yang berisi data pertama pada index tersebut.<br/>
Baris 19 Membuat perulangan selama `current` tidak kosong, artinya masih ada node yang dicek pada index tersebut.<br/>
Baris 20 Mengecek apakah key pada node saat ini sama dengan key item yang ingin dimasukkan.<br/>
Baris 21 Jika key sudah ada, maka value lama akan diganti dengan value baru.<br/>
Baris 22 Menghentikan fungsi karena item sudah berhasil diperbarui.<br/>
Baris 23 Menggeser `current` ke node berikutnya untuk melanjutkan pengecekan.<br/>
Baris 24 Membuat node baru berisi key dan value item yang akan dimasukkan.<br/>
Baris 25 Menghubungkan node baru ke data lama yang sudah ada pada index tersebut.<br/>
Baris 26 Menjadikan node baru sebagai data pertama pada index tersebut.<br/>
Baris 27 Baris kosong sebagai pemisah antar fungsi.<br/>
Baris 28 Membuat fungsi `search()` dengan parameter `key`, digunakan untuk mencari item berdasarkan ID item.<br/>
Baris 29 Menentukan index tempat item kemungkinan disimpan.<br/>
Baris 30 Membuat variabel `current` yang berisi node pertama pada index tersebut.<br/>
Baris 31 Membuat perulangan selama `current` tidak kosong.<br/>
Baris 32 Mengecek apakah key pada node saat ini sama dengan key yang dicari.<br/>
Baris 33 Jika key ditemukan, maka program mengembalikan node tersebut.<br/>
Baris 34 Menggeser `current` ke node berikutnya jika key belum ditemukan.<br/>
Baris 35 Mengembalikan nilai `None` jika item dengan key tersebut tidak ditemukan.<br/>
Baris 36 Baris kosong sebagai pemisah antar fungsi.<br/>
Baris 37 Membuat fungsi `remove_key()` dengan parameter `key`, digunakan untuk menghapus item dari inventory.<br/>
Baris 38 Menentukan index tempat item yang akan dihapus kemungkinan berada.<br/>
Baris 39 Membuat variabel `current` yang berisi node pertama pada index tersebut.<br/>
Baris 40 Membuat variabel `prev` dengan nilai awal `None`, digunakan untuk menyimpan node sebelumnya.<br/>
Baris 41 Membuat perulangan selama `current` tidak kosong.<br/>
Baris 42 Mengecek apakah key pada node saat ini sama dengan key yang ingin dihapus.<br/>
Baris 43 Mengecek apakah node yang ingin dihapus adalah node pertama pada index tersebut.<br/>
Baris 44 Jika node pertama yang dihapus, maka isi index diganti dengan node setelahnya.<br/>
Baris 45 Jika node yang dihapus bukan node pertama, maka program masuk ke bagian `else`.<br/>
Baris 46 Menghubungkan node sebelumnya langsung ke node setelah node yang dihapus.<br/>
Baris 47 Mengembalikan nilai `True` sebagai tanda item berhasil dihapus.<br/>
Baris 48 Menggeser `prev` menjadi node saat ini sebelum lanjut ke node berikutnya.<br/>
Baris 49 Menggeser `current` ke node berikutnya.<br/>
Baris 50 Mengembalikan nilai `False` jika item dengan key tersebut tidak ditemukan.<br/>
Baris 51 Baris kosong sebagai pemisah antar fungsi.<br/>
Baris 52 Membuat fungsi `display()` yang digunakan untuk menampilkan seluruh isi inventory.<br/>
Baris 53 Menampilkan judul isi inventory ZZZ dengan metode Separate Chaining.<br/>
Baris 54 Membuat perulangan dari index 0 sampai index terakhir pada hash table.<br/>
Baris 55 Menampilkan nomor index hash table.<br/>
Baris 56 Membuat variabel `current` yang berisi node pertama pada index tersebut.<br/>
Baris 57 Membuat perulangan selama `current` tidak kosong.<br/>
Baris 58 Menampilkan key dan value item yang tersimpan pada node saat ini.<br/>
Baris 59 Menggeser `current` ke node berikutnya.<br/>
Baris 60 Menampilkan `NULL` sebagai tanda akhir dari linked list pada index tersebut.<br/>
Baris 61 Baris kosong sebagai pemisah.<br/>
Baris 62 Baris kosong sebagai pemisah antara class dan fungsi utama.<br/>
Baris 63 Membuat fungsi utama bernama `main()` sebagai pusat jalannya program.<br/>
Baris 64 Membuat objek bernama `inventory` dari class `HashMapSeparateChaining`.<br/>
Baris 65 Baris kosong sebagai pemisah agar kode lebih rapi.<br/>
Baris 66 Menambahkan item dengan key `1` dan value `"W-Engine: Demara Battery Mark II"` ke dalam inventory.<br/>
Baris 67 Menambahkan item dengan key `11` dan value `"Drive Disc: Shockstar Disco"` ke dalam inventory.<br/>
Baris 68 Menambahkan item dengan key `21` dan value `"Material: Senior Investigator Log"` ke dalam inventory.<br/>
Baris 69 Menambahkan item dengan key `2` dan value `"Item: Ether Battery"` ke dalam inventory.<br/>
Baris 70 Baris kosong sebagai pemisah.<br/>
Baris 71 Memanggil fungsi `display()` untuk menampilkan seluruh isi inventory.<br/>
Baris 72 Baris kosong sebagai pemisah.<br/>
Baris 73 Mencari item dengan key `11` dan menyimpan hasilnya ke dalam variabel `hasil`.<br/>
Baris 74 Mengecek apakah hasil pencarian tidak kosong.<br/>
Baris 75 Jika item ditemukan, program menampilkan pesan bahwa item dengan key `11` ditemukan beserta value-nya.<br/>
Baris 76 Jika item tidak ditemukan, maka program masuk ke bagian `else`.<br/>
Baris 77 Menampilkan pesan bahwa item dengan key `11` tidak ditemukan.<br/>
Baris 78 Baris kosong sebagai pemisah.<br/>
Baris 79 Menghapus item dengan key `11` dari inventory.<br/>
Baris 80 Menampilkan teks bahwa item dengan key `11` sudah dihapus.<br/>
Baris 81 Memanggil fungsi `display()` lagi untuk menampilkan isi inventory setelah penghapusan.<br/>
Baris 82 Baris kosong sebagai pemisah.<br/>
Baris 83 Baris kosong sebagai pemisah sebelum bagian akhir program.<br/>
Baris 84 Mengecek apakah file Python dijalankan secara langsung.<br/>
Baris 85 Jika file dijalankan langsung, maka fungsi `main()` dipanggil sehingga program mulai berjalan.<br/>

d. Output Program :

<img width="1689" height="651" alt="Screenshot 2026-05-26 231834" src="https://github.com/user-attachments/assets/7feaf9e4-2f33-4b51-b858-3409ca52f415" />
<img width="1690" height="646" alt="Screenshot 2026-05-26 231845" src="https://github.com/user-attachments/assets/51b938c9-9a88-42de-b805-cbc69e66cb3c" />
<img width="1680" height="638" alt="Screenshot 2026-05-26 231854" src="https://github.com/user-attachments/assets/0fb3e8c9-9ecb-46bc-9840-85bbe01876dd" />
<img width="1638" height="625" alt="Screenshot 2026-05-26 231903" src="https://github.com/user-attachments/assets/e6115c0d-bb3b-467d-b094-7cd4e1db2745" />
<img width="1674" height="610" alt="Screenshot 2026-05-26 231912" src="https://github.com/user-attachments/assets/91c07033-131b-4e0e-9521-1bbcae83b44b" />
<img width="1676" height="616" alt="Screenshot 2026-05-26 231925" src="https://github.com/user-attachments/assets/c3aab870-63c9-45d0-adb9-fcf21818fdea" />
<img width="1692" height="300" alt="Screenshot 2026-05-26 231936" src="https://github.com/user-attachments/assets/0abbbff7-895e-4d45-a9ce-9ab0beb5c311" />




Output program menampilkan menu utama **Sistem Level Boss Wuthering Waves**. Pengguna dapat menambahkan level boss, mencari level tertentu, menampilkan level secara terurut, melihat preorder dan postorder, serta mengetahui level boss terendah, tertinggi, jumlah boss, dan total seluruh level boss. Program ini bekerja menggunakan struktur **Binary Search Tree (BST)**, sehingga data level boss disusun berdasarkan nilai kecil ke kiri dan nilai besar ke kanan. 

Pada output tersebut, pengguna memasukkan level boss **25, 50, 75, dan 100**. Setelah itu, program berhasil mencari level **75** dan menampilkan bahwa boss dengan level tersebut ditemukan. Ketika menu terurut dipilih, program menampilkan **25 50 75 100**. Program juga menampilkan level terendah yaitu **25**, level tertinggi yaitu **100**, jumlah boss sebanyak **4**, dan total seluruh level boss yaitu **250**. Saat pengguna memilih menu **10**, program menampilkan pesan **“Program selesai.”**


e. link youtube : [https://youtu.be/i-hNoEuMl-M](https://youtu.be/aK033Sb2lCk)
