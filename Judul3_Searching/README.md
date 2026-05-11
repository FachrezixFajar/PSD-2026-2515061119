TUGAS AKHIR JUDUL 3

a. Judul Program : Fungsi Sequential Searching Untuk Mencari Senjata Pada Tas Genshin Impact

b. Deskripsi Singkat : Program tersebut berfungsi untuk mencari data senjata yang terdapat di dalam tas pada game Genshin Impact menggunakan metode Sequential Search. Pengguna dapat memasukkan nama senjata yang ingin dicari, lalu program akan memeriksa satu per satu isi daftar senjata dari awal hingga akhir. Jika senjata ditemukan, program akan menampilkan jumlah kemunculan senjata tersebut beserta posisi indeksnya di dalam list. Namun jika tidak ditemukan, program akan memberikan informasi bahwa senjata tersebut tidak ada di dalam tas. Cara kerja program ini mirip seperti pemain yang mengecek isi inventory secara manual untuk memastikan apakah suatu senjata sudah dimiliki atau belum.

c. Source Code :


Baris 1 membuat fungsi bernama bubble_sort yang menerima satu data masukkan berparameter berupa daftar bernama arr.<br/>
Baris 2 Menghitung jumlah elemen di dalam arr dan menyimpannya ke dalam variabel n.<br/>
Baris 3 Memulai perulangan luar (outer loop) untuk mengontrol tahapan pengurutan. Loop berjalan sebanyak jumlah elemen n dikurangi 1.<br/>
Baris 4 Memulai perulangan dalam (inner loop) untuk membandingkan dua data yang bersebelahan. Semakin jauh pengurutan berjalan (nilai i makin besar), elemen yang          perlu dicek makin sedikit karena elemen di ujung sudah pasti berada di posisi yang benar.<br/>
Baris 5 Mengecek apakah skor saat ini lebih kecil dari skor di posisi berikutnya. Karena tandanya < (kurang dari), data dengan skor besar akan didorong ke depan           (menghasilkan urutan menurun/descending).<br/>
Baris 6 Jika kondisi di Baris 5 benar, tukar posisi kedua data tersebut.<br/>
Baris 7 
Baris 8 Membuat fungsi bernama tampilkan untuk mencetak daftar pemain ke layar dengan rapi.<br/>
Baris 9 Mencetak teks judul tabel<br/>
Baris 10 Mencetak garis pemisah berupa tanda strip (-) sebanyak 35 kali (sebagai hiasan saja agar rapi).<br/> 
Baris 11 Melakukan perulangan untuk membaca isi daftar pemain satu per satu. enumerate(pemain, 1) berguna untuk memberikan nomor urut otomatis (variabel i) yang             dimulai dari angka 1. Variabel p mewakili data pemainnya. <br/>
Baris 12 Mencetak data pemain ke layar. f"{...}" merupakan fitur f-string di Python.<br/>
Baris 13 <br/>
Baris 14 Menyiapkan tempat penampungan list kosong bernama pemain untuk menyimpan data yang akan diketik oleh user. <br/> 
Baris 15 <br/>
Baris 16 Memulai perulangan tanpa henti. Tujuannya agar program terus menanyakan jumlah pemain sampai user memasukkan input yang<br/>
Baris 17 Memulai blok untuk "mencoba" perintah. Jika ada error (misal user mengetik huruf alih-alih angka), program tidak akan langsung crash/error.<br/>
Baris 18 Meminta user memasukkan jumlah pemain, lalu mengubah inputnya menjadi tipe data angka bulat<br/>
Baris 19 Mengecek apakah jumlah pemain yang dimasukkan lebih dari 0.<br/>
Baris 20 Jika iya, perulangan while True dihentikan.<br/>
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
Baris 36 Menambahkan (append) data nama dan skor tersebut ke dalam list pemain dalam format dictionary.<br/>
Baris 37 <br/>
Baris 38 Mencetak teks judul batas.<br/>
Baris 39 Memanggil fungsi tampilkan untuk mencetak tabel data pemain yang masih acak/belum diurutkan.<br/>
Baris 40 <br/>
Baris 41 Memanggil fungsi bubble_sort agar komputer mulai mengurutkan data pemain di dalam memori.<br/>
Baris 42 <br/>
Baris 43 Mencetak teks judul batas (ini sudah secara Descending, skor tertinggi di atas).<br/>
Baris 44 Memanggil kembali fungsi tampilkan untuk mencetak tabel data pemain yang kali ini sudah terurut dengan rapi.<br/>
Baris 45 <br/>
Baris 46 Mencetak nama pemenang beserta skornya. Program cukup mengambil data di indeks ke-0 (pemain[0]), karena setelah diurutkan, otomatis data dengan skor tertinggi akan berada di posisi paling pertama (indeks 0).<br/>

d. Output Program :
<img width="1717" height="503" alt="Screenshot 2026-05-05 011224" src="https://github.com/user-attachments/assets/2e222ab0-f977-4e66-8dde-0d715dc856f0" />

Output dari program tersebut akan menampilkan daftar senjata yang ada di dalam tas terlebih dahulu, kemudian pengguna diminta memasukkan nama senjata yang ingin dicari. Setelah input diberikan, program akan melakukan proses pencarian menggunakan metode Sequential Search dengan memeriksa setiap data senjata satu per satu dari awal hingga akhir list.
Jika senjata yang dicari ditemukan, program akan menampilkan nama senjata, jumlah kemunculannya, serta posisi indeks tempat senjata tersebut berada. Contohnya ketika pengguna memasukkan `"Rust"`, maka output akan menunjukkan bahwa senjata tersebut ditemukan beberapa kali beserta indeksnya, misalnya `[1, 4, 7]`. Hal ini berarti senjata Rust berada pada posisi ke-1, ke-4, dan ke-7 dalam list.
Sedangkan jika pengguna memasukkan nama senjata yang tidak ada di dalam daftar, misalnya `"Wolf Gravestone"`, maka program akan menampilkan pesan bahwa senjata tersebut tidak ditemukan dalam tas. Dengan demikian, output program membantu pengguna mengetahui apakah suatu senjata tersedia dan di posisi mana senjata itu berada pada inventory.

e. Link Youtube :
