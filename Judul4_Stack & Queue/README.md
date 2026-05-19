TUGAS AKHIR JUDUL 4

a. Judul Program : Fungsi QueueArray untuk melihat giliran menyerang pada game honkai star rail

b. Deskripsi Singkat : Program tersebut berfungsi untuk mengatur urutan giliran karakter menyerang dalam game RPG sederhana bertema Honkai: Star Rail  menggunakan struktur data Queue berbasis Array. Pengguna dapat menambahkan nama karakter ke dalam antrean giliran, melihat karakter yang akan menyerang lebih dulu, menampilkan seluruh urutan giliran, serta menjalankan aksi serangan karakter secara bergantian. Karakter yang masuk lebih awal akan mendapat giliran menyerang lebih dahulu sesuai prinsip First In First Out (FIFO). Cara kerja program ini mirip seperti sistem turn-based battle, yaitu karakter menyerang berdasarkan urutan giliran yang telah tersusun. 


Baris 1 Membuat class bernama `QueueArray` yang digunakan untuk mengatur antrean giliran karakter menyerang.<br/>
Baris 2 Membuat fungsi konstruktor `__init__` yang akan dijalankan otomatis saat objek `QueueArray` dibuat. Parameter `max_size=100` berarti kapasitas maksimal antrean adalah 100 data.<br/>
Baris 3 Menyimpan nilai kapasitas maksimal antrean ke dalam variabel `MAXN`.<br/>
Baris 4 Membuat array atau list bernama `q` dengan isi awal `None` sebanyak ukuran `MAXN`. List ini digunakan untuk menyimpan nama karakter yang masuk giliran menyerang.<br/>
Baris 5 Membuat variabel `front_idx` dengan nilai awal `-1`, yang menandakan bahwa posisi depan antrean masih kosong.<br/>
Baris 6 Membuat variabel `rear_idx` dengan nilai awal `-1`, yang menandakan bahwa posisi belakang antrean juga masih kosong.<br/>
Baris 7<br/>
Baris 8 Membuat fungsi `is_empty()` untuk mengecek apakah antrean giliran karakter masih kosong atau tidak.<br/>
Baris 9 Mengembalikan nilai `True` jika `front_idx` bernilai `-1`, artinya belum ada karakter dalam antrean.<br/>
Baris 10<br/>
Baris 11 Membuat fungsi `is_full()` untuk mengecek apakah antrean sudah penuh.<br/>
Baris 12 Mengecek kondisi penuh menggunakan rumus circular queue. Jika posisi setelah `rear_idx` sama dengan `front_idx`, berarti antrean sudah tidak memiliki ruang kosong.<br/>
Baris 13<br/>
Baris 14 Membuat fungsi `enqueue()` dengan parameter `karakter`, digunakan untuk menambahkan nama karakter ke urutan giliran menyerang.<br/>
Baris 15 Mengecek apakah antrean sudah penuh dengan memanggil fungsi `is_full()`.<br/>
Baris 16 Jika antrean penuh, program menampilkan pesan `"Urutan giliran penuh"`.<br/>
Baris 17 Menghentikan fungsi `enqueue()` agar karakter baru tidak dimasukkan ke dalam antrean.<br/>
Baris 18<br/>
Baris 19 Mengecek apakah antrean masih kosong dengan memanggil fungsi `is_empty()`.<br/>
Baris 20 Jika antrean kosong, maka `front_idx` diatur menjadi `0` sebagai posisi awal data pertama.<br/>
Baris 21 `rear_idx` juga diatur menjadi `0` karena data pertama menjadi sekaligus posisi depan dan belakang antrean.<br/>
Baris 22 Jika antrean tidak kosong, program masuk ke blok `else`.<br/>
Baris 23 Menggeser posisi `rear_idx` ke indeks berikutnya menggunakan sistem circular queue dengan operator modulo `%`.<br/>
Baris 24<br/>
Baris 25 Menyimpan nama karakter ke dalam array `q` pada posisi `rear_idx`.<br/>
Baris 26 Menampilkan pesan bahwa karakter berhasil masuk ke urutan giliran menyerang.<br/>
Baris 27<br/>
Baris 28 Membuat fungsi `dequeue()` yang digunakan untuk mengeluarkan karakter paling depan dari antrean, dalam konteks game berarti karakter tersebut melakukan serangan.<br/>
Baris 29 Mengecek apakah antrean sedang kosong dengan memanggil fungsi `is_empty()`.<br/>
Baris 30 Jika antrean kosong, program menampilkan pesan `"Tidak ada karakter dalam giliran!"`.<br/>
Baris 31 Menghentikan fungsi `dequeue()` agar tidak memproses data kosong.<br/>
Baris 32<br/>
Baris 33 Menampilkan pesan bahwa karakter pada posisi paling depan sedang menyerang musuh.<br/>
Baris 34<br/>
Baris 35 Mengecek apakah hanya tersisa satu karakter dalam antrean, yaitu ketika `front_idx` sama dengan `rear_idx`.<br/>
Baris 36 Jika hanya ada satu karakter, `front_idx` diubah kembali menjadi `-1` untuk menandakan antrean kosong.<br/>
Baris 37 `rear_idx` juga diubah menjadi `-1` agar seluruh antrean kembali ke kondisi awal.<br/>
Baris 38 Jika antrean masih memiliki lebih dari satu karakter, program masuk ke blok `else`.<br/>
Baris 39 Menggeser posisi `front_idx` ke indeks berikutnya karena karakter sebelumnya sudah menyerang dan keluar dari antrean.<br/>
Baris 40<br/>
Baris 41 Membuat fungsi `peek()` untuk melihat karakter yang akan menyerang berikutnya tanpa mengeluarkannya dari antrean.<br/>
Baris 42 Mengecek apakah antrean kosong dengan fungsi `is_empty()`.<br/>
Baris 43 Jika antrean kosong, program menampilkan pesan `"Tidak ada karakter dalam giliran!"`.<br/>
Baris 44 Menghentikan fungsi `peek()` agar tidak mengambil data dari antrean kosong.<br/>
Baris 45<br/>
Baris 46 Menampilkan nama karakter yang berada di posisi paling depan antrean sebagai karakter yang akan menyerang berikutnya.<br/>
Baris 47<br/>
Baris 48 Membuat fungsi `display()` untuk menampilkan seluruh urutan giliran karakter menyerang.<br/>
Baris 49 Mengecek apakah antrean kosong dengan fungsi `is_empty()`.<br/>
Baris 50 Jika kosong, program menampilkan pesan `"Urutan giliran kosong"`.<br/>
Baris 51 Menghentikan fungsi `display()` karena tidak ada data yang dapat ditampilkan.<br/>
Baris 52<br/>
Baris 53 Menampilkan teks awal `"Urutan giliran menyerang:"` tanpa langsung pindah baris karena menggunakan `end=""`.<br/>
Baris 54 Membuat variabel `i` yang nilainya diambil dari `front_idx`, yaitu posisi karakter pertama dalam antrean.<br/>
Baris 55<br/>
Baris 56 Memulai perulangan `while True` untuk membaca isi antrean dari depan sampai belakang.<br/>
Baris 57 Menampilkan nama karakter pada posisi indeks `i`.<br/>
Baris 58 Mengecek apakah indeks `i` sudah sama dengan `rear_idx`, artinya data terakhir sudah ditampilkan.<br/>
Baris 59 Jika benar, perulangan dihentikan menggunakan `break`.<br/>
Baris 60 Menampilkan tanda panah `" -> "` sebagai pemisah antar karakter dalam urutan giliran.<br/>
Baris 61 Menggeser indeks `i` ke posisi berikutnya dengan sistem circular queue menggunakan operator modulo `%`.<br/>
Baris 62<br/>
Baris 63 Menampilkan baris kosong setelah seluruh urutan karakter selesai ditampilkan.<br/>
Baris 64<br/>
Baris 65 Membuat fungsi utama bernama `main()` sebagai pusat jalannya program.<br/>
Baris 66 Membuat objek bernama `queue` dari class `QueueArray`.<br/>
Baris 67 Membuat variabel `pilih` dengan nilai awal `0`, digunakan untuk menyimpan pilihan menu dari pengguna.<br/>
Baris 68<br/>
Baris 69 Membuat perulangan `while` yang akan terus berjalan selama pengguna belum memilih menu nomor `5`.<br/>
Baris 70 Menampilkan judul program game giliran menyerang RPG Honkai: Star Rail.<br/>
Baris 71 Menampilkan pilihan menu nomor 1 yaitu menambahkan karakter ke giliran.<br/>
Baris 72 Menampilkan pilihan menu nomor 2 yaitu menjalankan giliran karakter menyerang.<br/>
Baris 73 Menampilkan pilihan menu nomor 3 yaitu melihat karakter yang akan menyerang berikutnya.<br/>
Baris 74 Menampilkan pilihan menu nomor 4 yaitu menampilkan seluruh urutan giliran.<br/>
Baris 75 Menampilkan pilihan menu nomor 5 yaitu keluar dari program.<br/>
Baris 76<br/>
Baris 77 Memulai blok `try` untuk menangani kemungkinan kesalahan input dari pengguna.<br/>
Baris 78 Meminta pengguna memasukkan pilihan menu, lalu mengubahnya menjadi tipe data integer.<br/>
Baris 79 Jika input tidak dapat diubah menjadi angka, program masuk ke blok `except`.<br/>
Baris 80 Menampilkan pesan `"Input tidak valid!"`.<br/>
Baris 81 Menggunakan `continue` agar program kembali ke awal perulangan dan menampilkan menu lagi.<br/>
Baris 82<br/>
Baris 83 Mengecek apakah pengguna memilih menu nomor `1`.<br/>
Baris 84 Jika benar, program meminta pengguna memasukkan nama karakter.<br/>
Baris 85 Memanggil fungsi `enqueue()` untuk menambahkan karakter tersebut ke antrean giliran menyerang.<br/>
Baris 86<br/>
Baris 87 Mengecek apakah pengguna memilih menu nomor `2`.<br/>
Baris 88 Jika benar, program memanggil fungsi `dequeue()` agar karakter paling depan melakukan serangan lalu keluar dari urutan giliran.<br/>
Baris 89<br/>
Baris 90 Mengecek apakah pengguna memilih menu nomor `3`.<br/>
Baris 91 Jika benar, program memanggil fungsi `peek()` untuk melihat karakter yang akan menyerang berikutnya.<br/>
Baris 92<br/>
Baris 93 Mengecek apakah pengguna memilih menu nomor `4`.<br/>
Baris 94 Jika benar, program memanggil fungsi `display()` untuk menampilkan semua karakter yang berada dalam urutan giliran.<br/>
Baris 95<br/>
Baris 96 Mengecek apakah pengguna memilih menu nomor `5`.<br/>
Baris 97 Jika benar, program menampilkan pesan `"Pertarungan selesai."`.<br/>
Baris 98<br/>
Baris 99 Jika input pilihan menu tidak sesuai dari angka 1 sampai 5, program masuk ke blok `else`.<br/>
Baris 100 Menampilkan pesan `"Pilihan tidak valid!"`.<br/>
Baris 101<br/>
Baris 102 Mengecek apakah file Python dijalankan secara langsung atau tidak.<br/>
Baris 103 Jika dijalankan langsung, maka fungsi `main()` dipanggil sehingga seluruh program mulai berjalan.<br/>
