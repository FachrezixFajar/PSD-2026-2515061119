TUGAS AKHIR JUDUL 2

a. Judul Program : Fungsi Bubble Sorting dalam mengurutkan skor game

b. Deskripsi Singkat : Program tersebut berfungsi untuk mengelola dan mengurutkan data pemain berdasarkan skor yang mereka peroleh. Pengguna diminta memasukkan jumlah pemain, lalu mengisi nama dan skor masing-masing pemain dengan validasi input agar tidak terjadi kesalahan. Cara kerjanya mirip seperti sistem leaderboard pada game, di mana setelah semua data dimasukkan, program akan menampilkan daftar pemain sebelum diurutkan, kemudian mengurutkannya menggunakan metode bubble sort berdasarkan skor tertinggi ke terendah. Setelah itu, hasil peringkat ditampilkan kembali secara rapi lengkap dengan posisi masing-masing pemain, dan pemain dengan skor tertinggi akan diumumkan sebagai pemenang.

c. Source Code :

Baris 1 membuat fungsi bernama bubble_sort yang menerima satu data masukkan (parameter) berupa daftar bernama arr.<br/>
Baris 2 Menghitung jumlah elemen di dalam arr dan menyimpannya ke dalam variabel n
Baris 3 Memulai perulangan luar (outer loop) untuk mengontrol tahapan pengurutan. Loop berjalan sebanyak jumlah elemen dikurangi 1
Baris 4 Memulai perulangan dalam (inner loop) untuk membandingkan dua data yang bersebelahan. Semakin jauh pengurutan berjalan (nilai i makin besar), elemen yang          perlu dicek makin sedikit karena elemen di ujung sudah pasti berada di posisi yang benar.
Baris 5 Mengecek apakah skor saat ini lebih kecil dari skor di posisi berikutnya. Karena tandanya < (kurang dari), data dengan skor besar akan didorong ke depan           (menghasilkan urutan menurun/descending).
Baris 6 Jika kondisi di Baris 5 benar, tukar posisi kedua data tersebut (proses swap).
Baris 7 Membuat fungsi bernama tampilkan untuk mencetak daftar pemain ke layar dengan rapi.
Baris 8 Mencetak teks judul tabel (Peringkat, Nama, Skor).
Baris 9 Mencetak garis pemisah berupa tanda strip (-) sebanyak 35 kali.
Baris 10 
Baris 11
Baris 12
Baris 13
Baris 14
Baris 15
Baris 16
Baris 17
Baris 18
Baris 19
Baris 20
Baris 21
Baris 22
Baris 23
Baris 24
Baris 25
Baris 26
Baris 27
Baris 28
Baris 29
Baris 30
Baris 31
Baris 32
Baris 33
Baris 34
Baris 35
Baris 36
Baris 37
Baris 38
Baris 39
Baris 40
Baris 41
Baris 42
Baris 43
Baris 44
Baris 45
Baris 46
Baris 47
Baris 48
Baris 49
Baris 50
Baris 51
