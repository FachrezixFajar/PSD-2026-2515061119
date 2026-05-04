TUGAS AKHIR JUDUL 2

a. Judul Program : Fungsi Bubble Sorting dalam mengurutkan skor game

b. Deskripsi Singkat : Program tersebut berfungsi untuk mengelola dan mengurutkan data pemain berdasarkan skor yang mereka peroleh. Pengguna diminta memasukkan jumlah pemain, lalu mengisi nama dan skor masing-masing pemain dengan validasi input agar tidak terjadi kesalahan. Cara kerjanya mirip seperti sistem leaderboard pada game, di mana setelah semua data dimasukkan, program akan menampilkan daftar pemain sebelum diurutkan, kemudian mengurutkannya menggunakan metode bubble sort berdasarkan skor tertinggi ke terendah. Setelah itu, hasil peringkat ditampilkan kembali secara rapi lengkap dengan posisi masing-masing pemain, dan pemain dengan skor tertinggi akan diumumkan sebagai pemenang.

c. Source Code :
<img width="1464" height="2040" alt="code jd2" src="https://github.com/user-attachments/assets/788a8e53-f588-456d-a7a9-3a501566f564" />


Baris 1 membuat fungsi bernama bubble_sort yang menerima satu data masukkan (parameter) berupa daftar bernama arr.<br/>
Baris 2 Menghitung jumlah elemen di dalam arr dan menyimpannya ke dalam variabel n.<br/>
Baris 3 Memulai perulangan luar (outer loop) untuk mengontrol tahapan pengurutan. Loop berjalan sebanyak jumlah elemen dikurangi 1.<br/>
Baris 4 Memulai perulangan dalam (inner loop) untuk membandingkan dua data yang bersebelahan. Semakin jauh pengurutan berjalan (nilai i makin besar), elemen yang          perlu dicek makin sedikit karena elemen di ujung sudah pasti berada di posisi yang benar.<br/>
Baris 5 Mengecek apakah skor saat ini lebih kecil dari skor di posisi berikutnya. Karena tandanya < (kurang dari), data dengan skor besar akan didorong ke depan           (menghasilkan urutan menurun/descending).<br/>
Baris 6 Jika kondisi di Baris 5 benar, tukar posisi kedua data tersebut (proses swap).<br/>
Baris 7 
Baris 8 Membuat fungsi bernama tampilkan untuk mencetak daftar pemain ke layar dengan rapi.<br/>
Baris 9 Mencetak teks judul tabel<br/>
Baris 10 Mencetak garis pemisah berupa tanda strip (-) sebanyak 35 kali.<br/> 
Baris 11 Melakukan perulangan untuk membaca isi daftar pemain satu per satu. enumerate(pemain, 1) berguna untuk memberikan nomor urut otomatis (variabel i) yang             dimulai dari angka 1. Variabel p mewakili data pemainnya. <br/>
Baris 12 Mencetak data pemain ke layar. f"{...}" adalah fitur f-string di Python. Tanda <11 dan <16 digunakan untuk memberikan ruang spasi ke kanan agar teks sejajar dan membentuk kolom tabel yang rapi. <br/>
Baris 13 <br/>
Baris 14 Menyiapkan tempat penampungan (list) kosong bernama pemain untuk menyimpan data yang akan diketik oleh user. <br/> 
Baris 15 <br/>
Baris 16 Memulai perulangan tanpa henti (infinite loop). Tujuannya agar program terus menanyakan jumlah pemain sampai user memasukkan input yang<br/>
Baris 17 Memulai blok untuk "mencoba" perintah. Jika ada error (misal user mengetik huruf alih-alih angka), program tidak akan langsung crash/error.<br/>
Baris 18 Meminta user memasukkan jumlah pemain, lalu mengubah inputnya menjadi tipe data angka bulat<br/>
Baris 19 Mengecek apakah jumlah pemain yang dimasukkan lebih dari 0.<br/>
Baris 20 Jika iya (input benar), perulangan while True dihentikan.<br/>
Baris 21 Jika input angka 0 atau negatif, program akan mencetak peringatan ini dan kembali mengulang pertanyaan karena belum terkena break.<br/>
Baris 22 Ini adalah penangkap error. Kalau di Baris 21 user mengetik teks seperti "lima" (bukan angka "5"), program akan lompat ke baris ini.<br/>
Baris 23 Mencetak pesan peringatan bahwa yang diinput bukan angka.<br/>
Baris 24 <br/>
Baris 25 Memulai perulangan sebanyak n kali (sesuai jumlah pemain yang diinput tadi).<br/>
Baris 26 Menampilkan teks giliran pemain ke berapa (karena i mulai dari 0, maka ditambah 1 agar tampilannya mulai dari "Pemain 1").<br/>
Baris 27 Meminta user mengetik nama pemain dan menyimpannya di variabel nama.<br/>
Baris 28 <br/>
Baris 29 Sama seperti sebelumnya, memulai perulangan tanpa henti khusus untuk memvalidasi input skor.<br/>
Baris 30 Mencoba menjalankan perintah input skor.<br/>
Baris 31 Meminta user memasukkan angka skor dan mengubahnya menjadi tipe data int.<br/>
Baris 32 Jika berhasil dan benar berupa angka, hentikan perulangan (lanjut ke baris bawahnya).<br/>
Baris 33 Menangkap error jika skor yang diinput berupa teks/huruf.<br/>
Baris 34 Menampilkan pesan error dan karena tidak ada break, program akan kembali ke Baris 35.<br/>
Baris 35 <br/>
Baris 36 Menambahkan (append) data nama dan skor tersebut ke dalam list pemain dalam format dictionary (seperti kamus data).<br/>
Baris 37 <br/>
Baris 38 Mencetak teks judul batas.<br/>
Baris 39 Memanggil fungsi tampilkan untuk mencetak tabel data pemain yang masih acak/belum diurutkan.<br/>
Baris 40 <br/>
Baris 41 Memanggil fungsi bubble_sort agar komputer mulai mengurutkan data pemain di dalam memori.<br/>
Baris 42 <br/>
Baris 43 Mencetak teks judul batas (sekali lagi, ini nyatanya beroperasi secara Descending, skor tertinggi di atas).<br/>
Baris 44 Memanggil kembali fungsi tampilkan untuk mencetak tabel data pemain yang kali ini sudah terurut dengan rapi.<br/>
Baris 45 <br/>
Baris 46 Mencetak nama pemenang beserta skornya. Program cukup mengambil data di indeks ke-0 (pemain[0]), karena setelah diurutkan, otomatis data dengan skor tertinggi akan berada di posisi paling pertama (indeks 0).<br/>

d. Output Program
<img width="1717" height="503" alt="Screenshot 2026-05-05 011224" src="https://github.com/user-attachments/assets/2e222ab0-f977-4e66-8dde-0d715dc856f0" />

Output dari program tersebut menampilkan proses pengolahan data pemain mulai dari input hingga penentuan pemenang. Awalnya, pengguna memasukkan jumlah pemain dan data masing-masing pemain berupa nama dan skor. Program kemudian menampilkan daftar pemain dalam kondisi awal (sebelum diurutkan), sesuai dengan urutan saat data dimasukkan. Setelah itu, program melakukan proses pengurutan menggunakan metode bubble sort berdasarkan skor dari yang tertinggi ke terendah, sehingga posisi pemain dengan skor lebih besar akan berpindah ke atas. Hasil pengurutan ini ditampilkan kembali dalam bentuk peringkat yang sudah rapi. Terakhir, program menentukan dan menampilkan pemenang, yaitu pemain yang berada di posisi pertama karena memiliki skor paling tinggi.
