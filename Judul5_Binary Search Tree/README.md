TUGAS AKHIR JUDUL 5

a. Judul Program : Fungsi Binary Search Tree Dalam Sistem Level Boss Di Wuthering Waves

b. Deskripsi Singkat : Program tersebut berfungsi untuk mengatur level boss dalam game Wuthering Waves menggunakan struktur data Binary Search Tree (BST). Pengguna dapat menambahkan level boss, mencari level boss tertentu, menampilkan seluruh level boss secara terurut, serta melihat level boss terendah dan tertinggi. Setiap level boss yang dimasukkan akan disusun berdasarkan aturan BST, yaitu level yang lebih kecil ditempatkan di sebelah kiri dan level yang lebih besar ditempatkan di sebelah kanan. Cara kerja program ini mirip seperti sistem pendataan boss dalam game, sehingga pemain dapat mengetahui daftar level boss dari yang paling rendah hingga paling tinggi dengan lebih teratur

c. Source Code :

<img width="1724" height="6372" alt="judul 5" src="https://github.com/user-attachments/assets/94e6ce1e-0363-4156-9dc5-b5ab90dfb3bb" />


Baris 1 Membuat class bernama `Node` yang digunakan sebagai tempat menyimpan satu data level boss dalam Binary Search Tree.<br/>
Baris 2 Membuat fungsi konstruktor `__init__` yang otomatis dijalankan saat objek `Node` dibuat.<br/>
Baris 3 Menyimpan nilai `key` ke dalam variabel `self.key`. Pada program ini, `key` digunakan untuk menyimpan level boss.<br/>
Baris 4 Membuat variabel `self.left` dengan nilai awal `None`, yang digunakan untuk menunjuk node sebelah kiri.<br/>
Baris 5 Membuat variabel `self.right` dengan nilai awal `None`, yang digunakan untuk menunjuk node sebelah kanan.<br/>
Baris 6<br/>
Baris 7<br/>
Baris 8 Membuat class bernama `BSTDasar` yang digunakan untuk mengatur seluruh data level boss menggunakan struktur Binary Search Tree.<br/>
Baris 9 Membuat fungsi konstruktor `__init__` yang otomatis dijalankan saat objek `BSTDasar` dibuat.<br/>
Baris 10 Membuat variabel `self.root` dengan nilai awal `None`, yang menandakan bahwa pohon BST masih kosong.<br/>
Baris 11<br/>
Baris 12 Membuat fungsi `insert_node()` dengan parameter `root` dan `key`, digunakan untuk memasukkan level boss ke dalam BST.<br/>
Baris 13 Mengecek apakah `root` masih kosong.<br/>
Baris 14 Jika `root` kosong, maka program membuat node baru berisi level boss tersebut.<br/>
Baris 15 Mengecek apakah nilai `key` lebih kecil dari nilai `root.key`.<br/>
Baris 16 Jika lebih kecil, maka level boss dimasukkan ke bagian kiri tree.<br/>
Baris 17 Mengecek apakah nilai `key` lebih besar dari nilai `root.key`.<br/>
Baris 18 Jika lebih besar, maka level boss dimasukkan ke bagian kanan tree.<br/>
Baris 19 Mengembalikan nilai `root` setelah proses pemasukan data selesai.<br/>
Baris 20<br/>
Baris 21 Membuat fungsi `insert()` dengan parameter `key`, digunakan sebagai fungsi utama untuk menambahkan level boss.<br/>
Baris 22 Memanggil fungsi `insert_node()` dan menyimpan hasilnya ke dalam `self.root`.<br/>
Baris 23<br/>
Baris 24 Membuat fungsi `search_node()` dengan parameter `root` dan `key`, digunakan untuk mencari level boss dalam BST.<br/>
Baris 25 Mengecek apakah `root` kosong.<br/>
Baris 26 Jika `root` kosong, maka level boss tidak ditemukan dan mengembalikan nilai `False`.<br/>
Baris 27 Mengecek apakah nilai `root.key` sama dengan level boss yang dicari.<br/>
Baris 28 Jika sama, maka level boss ditemukan dan mengembalikan nilai `True`.<br/>
Baris 29 Mengecek apakah level boss yang dicari lebih kecil dari nilai `root.key`.<br/>
Baris 30 Jika lebih kecil, pencarian dilanjutkan ke bagian kiri tree.<br/>
Baris 31 Jika lebih besar, pencarian dilanjutkan ke bagian kanan tree.<br/>
Baris 32<br/>
Baris 33 Membuat fungsi `search()` dengan parameter `key`, digunakan sebagai fungsi utama untuk mencari level boss.<br/>
Baris 34 Mengembalikan hasil pencarian dari fungsi `search_node()` mulai dari akar tree.<br/>
Baris 35<br/>
Baris 36 Membuat fungsi `inorder()` dengan parameter `root`, digunakan untuk menampilkan level boss secara terurut dari kecil ke besar.<br/>
Baris 37 Mengecek apakah `root` kosong.<br/>
Baris 38 Jika kosong, maka fungsi dihentikan.<br/>
Baris 39 Memanggil fungsi `inorder()` ke bagian kiri tree terlebih dahulu.<br/>
Baris 40 Menampilkan nilai level boss pada node saat ini.<br/>
Baris 41 Memanggil fungsi `inorder()` ke bagian kanan tree.<br/>
Baris 42<br/>
Baris 43 Membuat fungsi `preorder()` dengan parameter `root`, digunakan untuk menampilkan data dengan urutan root, kiri, lalu kanan.<br/>
Baris 44 Mengecek apakah `root` kosong.<br/>
Baris 45 Jika kosong, maka fungsi dihentikan.<br/>
Baris 46 Menampilkan nilai level boss pada node saat ini terlebih dahulu.<br/>
Baris 47 Memanggil fungsi `preorder()` ke bagian kiri tree.<br/>
Baris 48 Memanggil fungsi `preorder()` ke bagian kanan tree.<br/>
Baris 49<br/>
Baris 50 Membuat fungsi `postorder()` dengan parameter `root`, digunakan untuk menampilkan data dengan urutan kiri, kanan, lalu root.<br/>
Baris 51 Mengecek apakah `root` kosong.<br/>
Baris 52 Jika kosong, maka fungsi dihentikan.<br/>
Baris 53 Memanggil fungsi `postorder()` ke bagian kiri tree.<br/>
Baris 54 Memanggil fungsi `postorder()` ke bagian kanan tree.<br/>
Baris 55 Menampilkan nilai level boss pada node saat ini setelah bagian kiri dan kanan selesai ditampilkan.<br/>
Baris 56<br/>
Baris 57 Membuat fungsi `find_min()` dengan parameter `root`, digunakan untuk mencari level boss terendah.<br/>
Baris 58 Mengecek apakah `root` kosong.<br/>
Baris 59 Jika kosong, maka fungsi mengembalikan nilai `-1` sebagai tanda tidak ada data.<br/>
Baris 60 Membuat variabel `current` yang berisi node awal atau `root`.<br/>
Baris 61 Membuat perulangan selama node sebelah kiri masih ada.<br/>
Baris 62 Menggeser `current` ke node kiri karena nilai terkecil dalam BST berada di bagian paling kiri.<br/>
Baris 63 Mengembalikan nilai `current.key` sebagai level boss terendah.<br/>
Baris 64<br/>
Baris 65 Membuat fungsi `find_max()` dengan parameter `root`, digunakan untuk mencari level boss tertinggi.<br/>
Baris 66 Mengecek apakah `root` kosong.<br/>
Baris 67 Jika kosong, maka fungsi mengembalikan nilai `-1` sebagai tanda tidak ada data.<br/>
Baris 68 Membuat variabel `current` yang berisi node awal atau `root`.<br/>
Baris 69 Membuat perulangan selama node sebelah kanan masih ada.<br/>
Baris 70 Menggeser `current` ke node kanan karena nilai terbesar dalam BST berada di bagian paling kanan.<br/>
Baris 71 Mengembalikan nilai `current.key` sebagai level boss tertinggi.<br/>
Baris 72<br/>
Baris 73 Membuat fungsi `count_nodes()` dengan parameter `root`, digunakan untuk menghitung jumlah boss yang tersimpan.<br/>
Baris 74 Mengecek apakah `root` kosong.<br/>
Baris 75 Jika kosong, maka mengembalikan nilai `0`.<br/>
Baris 76 Menghitung jumlah node dengan menjumlahkan node saat ini, node kiri, dan node kanan secara rekursif.<br/>
Baris 77<br/>
Baris 78 Membuat fungsi `sum_nodes()` dengan parameter `root`, digunakan untuk menghitung total seluruh level boss.<br/>
Baris 79 Mengecek apakah `root` kosong.<br/>
Baris 80 Jika kosong, maka mengembalikan nilai `0`.<br/>
Baris 81 Menjumlahkan nilai level boss pada node saat ini dengan seluruh nilai pada bagian kiri dan kanan tree.<br/>
Baris 82<br/>
Baris 83<br/>
Baris 84 Membuat fungsi utama bernama `main()` sebagai pusat jalannya program.<br/>
Baris 85 Membuat objek bernama `boss_level` dari class `BSTDasar` untuk menyimpan data level boss.<br/>
Baris 86 Membuat variabel `pilih` dengan nilai awal `0`, digunakan untuk menyimpan pilihan menu dari pengguna.<br/>
Baris 87<br/>
Baris 88 Membuat perulangan `while` yang akan terus berjalan selama pengguna belum memilih menu nomor `10`.<br/>
Baris 89 Menampilkan judul program sistem level boss Wuthering Waves.<br/>
Baris 90 Menampilkan pilihan menu nomor 1 untuk menambahkan level boss.<br/>
Baris 91 Menampilkan pilihan menu nomor 2 untuk mencari level boss.<br/>
Baris 92 Menampilkan pilihan menu nomor 3 untuk menampilkan level boss secara terurut.<br/>
Baris 93 Menampilkan pilihan menu nomor 4 untuk menampilkan preorder level boss.<br/>
Baris 94 Menampilkan pilihan menu nomor 5 untuk menampilkan postorder level boss.<br/>
Baris 95 Menampilkan pilihan menu nomor 6 untuk melihat level boss terendah.<br/>
Baris 96 Menampilkan pilihan menu nomor 7 untuk melihat level boss tertinggi.<br/>
Baris 97 Menampilkan pilihan menu nomor 8 untuk melihat jumlah boss yang tersimpan.<br/>
Baris 98 Menampilkan pilihan menu nomor 9 untuk menghitung total seluruh level boss.<br/>
Baris 99 Menampilkan pilihan menu nomor 10 untuk keluar dari program.<br/>
Baris 100<br/>
Baris 101 Memulai blok `try` untuk menangani kemungkinan kesalahan input dari pengguna.<br/>
Baris 102 Meminta pengguna memasukkan pilihan menu, lalu mengubahnya menjadi tipe data integer.<br/>
Baris 103 Jika input tidak dapat diubah menjadi angka, program masuk ke blok `except`.<br/>
Baris 104 Menampilkan pesan `"Input tidak valid!"`.<br/>
Baris 105 Menggunakan `continue` agar program kembali ke awal perulangan dan menampilkan menu lagi.<br/>
Baris 106<br/>
Baris 107 Mengecek apakah pengguna memilih menu nomor `1`.<br/>
Baris 108 Jika benar, program masuk ke blok `try` untuk meminta input level boss.<br/>
Baris 109 Meminta pengguna memasukkan level boss, lalu mengubahnya menjadi integer.<br/>
Baris 110 Memanggil fungsi `insert()` untuk memasukkan level boss ke dalam BST.<br/>
Baris 111 Menampilkan pesan bahwa level boss berhasil dimasukkan.<br/>
Baris 112 Jika input level boss bukan angka, program masuk ke blok `except`.<br/>
Baris 113 Menampilkan pesan `"Input tidak valid!"`.<br/>
Baris 114<br/>
Baris 115 Mengecek apakah pengguna memilih menu nomor `2`.<br/>
Baris 116 Jika benar, program masuk ke blok `try` untuk mencari level boss.<br/>
Baris 117 Meminta pengguna memasukkan level boss yang ingin dicari.<br/>
Baris 118 Mengecek apakah level boss tersebut ada dengan memanggil fungsi `search()`.<br/>
Baris 119 Jika level boss ditemukan, program menampilkan pesan bahwa boss dengan level tersebut ditemukan.<br/>
Baris 120 Jika level boss tidak ditemukan, program masuk ke blok `else`.<br/>
Baris 121 Menampilkan pesan bahwa boss dengan level tersebut tidak ditemukan.<br/>
Baris 122 Jika input bukan angka, program masuk ke blok `except`.<br/>
Baris 123 Menampilkan pesan `"Input tidak valid!"`.<br/>
Baris 124<br/>
Baris 125 Mengecek apakah pengguna memilih menu nomor `3`.<br/>
Baris 126 Menampilkan teks awal `"Level boss terurut:"` tanpa langsung pindah baris.<br/>
Baris 127 Memanggil fungsi `inorder()` untuk menampilkan level boss dari yang terkecil sampai terbesar.<br/>
Baris 128 Menampilkan baris baru setelah data selesai ditampilkan.<br/>
Baris 129<br/>
Baris 130 Mengecek apakah pengguna memilih menu nomor `4`.<br/>
Baris 131 Menampilkan teks awal `"Preorder level boss:"` tanpa langsung pindah baris.<br/>
Baris 132 Memanggil fungsi `preorder()` untuk menampilkan data dengan urutan root, kiri, dan kanan.<br/>
Baris 133 Menampilkan baris baru setelah data selesai ditampilkan.<br/>
Baris 134<br/>
Baris 135 Mengecek apakah pengguna memilih menu nomor `5`.<br/>
Baris 136 Menampilkan teks awal `"Postorder level boss:"` tanpa langsung pindah baris.<br/>
Baris 137 Memanggil fungsi `postorder()` untuk menampilkan data dengan urutan kiri, kanan, dan root.<br/>
Baris 138 Menampilkan baris baru setelah data selesai ditampilkan.<br/>
Baris 139<br/>
Baris 140 Mengecek apakah pengguna memilih menu nomor `6`.<br/>
Baris 141 Menampilkan level boss terendah dengan memanggil fungsi `find_min()`.<br/>
Baris 142<br/>
Baris 143 Mengecek apakah pengguna memilih menu nomor `7`.<br/>
Baris 144 Menampilkan level boss tertinggi dengan memanggil fungsi `find_max()`.<br/>
Baris 145<br/>
Baris 146 Mengecek apakah pengguna memilih menu nomor `8`.<br/>
Baris 147 Menampilkan jumlah boss yang tersimpan dengan memanggil fungsi `count_nodes()`.<br/>
Baris 148<br/>
Baris 149 Mengecek apakah pengguna memilih menu nomor `9`.<br/>
Baris 150 Menampilkan total seluruh level boss dengan memanggil fungsi `sum_nodes()`.<br/>
Baris 151<br/>
Baris 152 Mengecek apakah pengguna memilih menu nomor `10`.<br/>
Baris 153 Jika benar, program menampilkan pesan `"Program selesai."`.<br/>
Baris 154<br/>
Baris 155 Jika pilihan menu tidak sesuai angka 1 sampai 10, program masuk ke blok `else`.<br/>
Baris 156 Menampilkan pesan `"Pilihan tidak valid!"`.<br/>
Baris 157<br/>
Baris 158<br/>
Baris 159 Mengecek apakah file Python dijalankan secara langsung atau tidak.<br/>
Baris 160 Jika file dijalankan langsung, maka fungsi `main()` dipanggil sehingga program mulai berjalan.<br/>

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
