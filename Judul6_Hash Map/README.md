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

<img width="1727" height="617" alt="Screenshot 2026-06-09 220805" src="https://github.com/user-attachments/assets/be6cbbd5-695d-4863-bae6-2aaedad57a0a" />


Output program menampilkan isi **Inventory ZZZ** yang disimpan menggunakan struktur data **HashMap Separate Chaining**. Pada tampilan awal, item dengan key **1**, **11**, dan **21** berada pada index yang sama, yaitu index **1**, karena ketiganya menghasilkan nilai hash yang sama saat dibagi dengan ukuran tabel 10. Karena terjadi collision, item tersebut disimpan secara berantai menggunakan linked list, sehingga tampil dalam bentuk **(21, Material: Senior Investigator Log) -> (11, Drive Disc: Shockstar Disco) -> (1, W-Engine: Demara Battery Mark II) -> NULL**.

Selain itu, item dengan key **2** masuk ke index **2**, yaitu **Item: Ether Battery**. Setelah inventory ditampilkan, program melakukan pencarian item dengan key **11** dan berhasil menemukan item **Drive Disc: Shockstar Disco**. Kemudian program menghapus item dengan key **11** dari inventory. Setelah penghapusan, isi inventory ditampilkan kembali dan item **Drive Disc: Shockstar Disco** sudah tidak ada. Pada index **1**, data yang tersisa adalah **Material: Senior Investigator Log** dan **W-Engine: Demara Battery Mark II**. Output ini menunjukkan bahwa program berhasil menambahkan, mencari, menghapus, dan menampilkan item inventory menggunakan metode **Separate Chaining**.



e. link youtube : [https://youtu.be/i-hNoEuMl-M](https://youtu.be/aK033Sb2lCk)
