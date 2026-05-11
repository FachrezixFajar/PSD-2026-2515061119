TUGAS AKHIR JUDUL 3

a. Judul Program : Fungsi Sequential Searching Untuk Mencari Senjata Pada Tas Genshin Impact

b. Deskripsi Singkat : Program tersebut berfungsi untuk mencari data senjata yang terdapat di dalam tas pada game Genshin Impact menggunakan metode Sequential Search. Pengguna dapat memasukkan nama senjata yang ingin dicari, lalu program akan memeriksa satu per satu isi daftar senjata dari awal hingga akhir. Jika senjata ditemukan, program akan menampilkan jumlah kemunculan senjata tersebut beserta posisi indeksnya di dalam list. Namun jika tidak ditemukan, program akan memberikan informasi bahwa senjata tersebut tidak ada di dalam tas. Cara kerja program ini mirip seperti pemain yang mengecek isi inventory secara manual untuk memastikan apakah suatu senjata sudah dimiliki atau belum.

c. Source Code :


Baris 1 Membuat fungsi bernama sequential_search yang memiliki dua parameter yaitu tas_senjata sebagai daftar data senjata dan target sebagai senjata yang ingin dicari.<br/>
Baris 2 Membuat list kosong bernama indeks_ditemukan yang digunakan untuk menyimpan posisi indeks senjata yang ditemukan.<br/>
Baris 3 <br/>
Baris 4 Memulai perulangan menggunakan for untuk membaca setiap data senjata berdasarkan indeks dari awal hingga akhir list tas_senjata.<br/>
Baris 5 Mengecek apakah nama senjata pada indeks saat ini sama dengan target yang dicari. Fungsi lower() digunakan agar pencarian tidak membedakan huruf besar dan kecil.<br/>
Baris 6 Jika kondisi pada Baris 5 benar, maka indeks senjata tersebut akan ditambahkan ke dalam list indeks_ditemukan menggunakan append().<br/>
Baris 7 <br/>
Baris 8 Mengembalikan nilai berupa daftar indeks yang ditemukan ke program utama.<br/>
Baris 9 <br/>
Baris 10 Membuat fungsi utama bernama main() sebagai tempat menjalankan seluruh program.<br/>
Baris 11 Komentar penjelasan bahwa data berikut merupakan daftar senjata dalam tas Genshin Impact.<br/>
Baris 12 Membuat variabel tas_senjata dalam bentuk list yang berisi beberapa nama senjata.<br/>
Baris 13 Memasukkan data senjata "Skyward Blade" ke dalam list.<br/>
Baris 14 Memasukkan data senjata "Rust" ke dalam list.<br/>
Baris 15 Memasukkan data senjata "Favonius Sword" ke dalam list.<br/>
Baris 16 Memasukkan data senjata "The Stringless" ke dalam list.<br/>
Baris 17 Memasukkan data senjata "Rust" ke dalam list.<br/>
Baris 18 Memasukkan data senjata "Aquila Favonia" ke dalam list.<br/>
Baris 19 Memasukkan data senjata "Sacrificial Sword" ke dalam list.<br/>
Baris 20 Memasukkan data senjata "Rust" ke dalam list.<br/>
Baris 21 Memasukkan data senjata "Favonius Sword" ke dalam list.<br/>
Baris 22 Memasukkan data senjata "The Stringless" ke dalam list.<br/>
Baris 23 Memasukkan data senjata "Rust" ke dalam list.<br/>
Baris 24 Memasukkan data senjata "Aquila Favonia" ke dalam list.<br/>
Baris 25 Memasukkan data senjata "Sacrificial Sword" ke dalam list.<br/>
Baris 26 Memasukkan data senjata "Rust" ke dalam list.<br/>
Baris 27 Menutup list tas_senjata.<br/>
Baris 28 <br/>
Baris 29 Menampilkan teks judul daftar senjata ke layar.<br/>
Baris 30 Menampilkan seluruh isi list tas_senjata ke layar.<br/>
Baris 31 <br/>
Baris 32 Komentar penjelasan bahwa program akan meminta input senjata yang ingin dicari.<br/>
Baris 33 Meminta pengguna memasukkan nama senjata yang ingin dicari lalu menyimpannya ke variabel target.<br/>
Baris 34 <br/>
Baris 35 Komentar penjelasan bahwa program akan mulai melakukan proses pencarian.<br/>
Baris 36 Memanggil fungsi sequential_search untuk mencari target pada list tas_senjata lalu menyimpan hasilnya ke variabel hasil.<br/>
Baris 37 <br/>
Baris 38 Komentar penjelasan bahwa bagian berikut digunakan untuk menampilkan hasil pencarian.<br/>
Baris 39 Mengecek apakah jumlah data pada variabel hasil lebih dari 0, artinya senjata berhasil ditemukan.<br/>
Baris 40 Jika benar, program menampilkan pesan bahwa senjata ditemukan beserta jumlah kemunculannya.<br/>
Baris 41 Menampilkan posisi indeks tempat senjata ditemukan di dalam list.<br/>
Baris 42 Jika kondisi pada Baris 39 salah, maka program masuk ke blok else.<br/>
Baris 43 Menampilkan pesan bahwa senjata yang dicari tidak ditemukan dalam tas.<br/>
Baris 44 <br/>
Baris 45 Mengecek apakah file Python dijalankan secara langsung atau tidak.<br/>
Baris 46 Jika dijalankan langsung, maka fungsi main() akan dipanggil sehingga seluruh program mulai berjalan.<br/>


d. Output Program :

Output dari program tersebut akan menampilkan daftar senjata yang ada di dalam tas terlebih dahulu, kemudian pengguna diminta memasukkan nama senjata yang ingin dicari. Setelah input diberikan, program akan melakukan proses pencarian menggunakan metode Sequential Search dengan memeriksa setiap data senjata satu per satu dari awal hingga akhir list.
Jika senjata yang dicari ditemukan, program akan menampilkan nama senjata, jumlah kemunculannya, serta posisi indeks tempat senjata tersebut berada. Contohnya ketika pengguna memasukkan `"Rust"`, maka output akan menunjukkan bahwa senjata tersebut ditemukan beberapa kali beserta indeksnya, misalnya `[1, 4, 7]`. Hal ini berarti senjata Rust berada pada posisi ke-1, ke-4, dan ke-7 dalam list.
Sedangkan jika pengguna memasukkan nama senjata yang tidak ada di dalam daftar, misalnya `"Wolf Gravestone"`, maka program akan menampilkan pesan bahwa senjata tersebut tidak ditemukan dalam tas. Dengan demikian, output program membantu pengguna mengetahui apakah suatu senjata tersedia dan di posisi mana senjata itu berada pada inventory.

e. Link Youtube :
