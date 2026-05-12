TUGAS AKHIR JUDUL 3

a. Judul Program : Fungsi Sequential Searching Untuk Mencari Senjata Pada Tas Genshin Impact

b. Deskripsi Singkat : Program tersebut berfungsi untuk mencari data senjata yang terdapat di dalam tas pada game Genshin Impact menggunakan metode Sequential Search. Pengguna dapat memasukkan nama senjata yang ingin dicari, lalu program akan memeriksa satu per satu isi daftar senjata dari awal hingga akhir. Jika senjata ditemukan, program akan menampilkan jumlah kemunculan senjata tersebut beserta posisi indeksnya di dalam list. Namun jika tidak ditemukan, program akan memberikan informasi bahwa senjata tersebut tidak ada di dalam tas. Cara kerja program ini mirip seperti pemain yang mengecek isi inventory secara manual untuk memastikan apakah suatu senjata sudah dimiliki atau belum.

c. Source Code :
<img width="1720" height="683" alt="Screenshot 2026-05-12 211616" src="https://github.com/user-attachments/assets/ba5911f9-6a63-4e15-83c6-51062f4d7242" />
<img width="1731" height="472" alt="Screenshot 2026-05-12 211631" src="https://github.com/user-attachments/assets/1d8ee4d4-0174-4a7b-8ccc-87489e8528b6" />



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
Baris 11<br/>
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
Baris 29 <br/>
Baris 30 Menampilkan text daftar senjata dalam tas.<br/>
Baris 31 Menampilkan seluruh isi list tas_senjata ke layar<br/>
Baris 32 <br/>
Baris 33 <br/>
Baris 34 Meminta pengguna memasukkan nama senjata yang ingin dicari lalu menyimpannya ke variabel target.<br/>
Baris 35 <br/>
Baris 36 <br/>
Baris 37 Memanggil fungsi sequential_search untuk mencari target pada list tas_senjata lalu menyimpan hasilnya ke variabel hasil.<br/>
Baris 38 
Baris 39 
Baris 40 Mengecek apakah jumlah data pada variabel hasil lebih dari 0, artinya senjata berhasil ditemukan.<br/>>
Baris 41 Jika benar, program menampilkan pesan bahwa senjata ditemukan beserta jumlah kemunculannya.<br/
Baris 42 Menampilkan posisi indeks tempat senjata ditemukan di dalam list.<br/>
Baris 43 Jika kondisi pada Baris 40 salah, maka program masuk ke blok else.<br/>
Baris 44 Menampilkan pesan bahwa senjata yang dicari tidak ditemukan dalam tas.<br/>
Baris 45 <br/>
Baris 46 <br/>
Baris 47 Mengecek apakah file Python dijalankan secara langsung atau tidak.<br/>
Baris 48 Jika dijalankan langsung, maka fungsi main() akan dipanggil sehingga seluruh program mulai berjalan.<br/>


d. Output Program :
<img width="1721" height="178" alt="Screenshot 2026-05-12 211125" src="https://github.com/user-attachments/assets/cab71935-fe36-4fa4-b48d-bceba3e0ba4e" />

Output dari program tersebut akan menampilkan daftar senjata yang ada di dalam tas terlebih dahulu, kemudian pengguna diminta memasukkan nama senjata yang ingin dicari. Setelah input diberikan, program akan melakukan proses pencarian menggunakan metode Sequential Search dengan memeriksa setiap data senjata satu per satu dari awal hingga akhir list.
Jika senjata yang dicari ditemukan, program akan menampilkan nama senjata, jumlah kemunculannya, serta posisi indeks tempat senjata tersebut berada. Contohnya ketika pengguna memasukkan `"Rust"`, maka output akan menunjukkan bahwa senjata tersebut ditemukan beberapa kali beserta indeksnya, misalnya `[1, 4, 7]`. Hal ini berarti senjata Rust berada pada posisi ke-1, ke-4, dan ke-9, ke-12 dalam list.
Sedangkan jika pengguna memasukkan nama senjata yang tidak ada di dalam daftar, misalnya `"Wolf Gravestone"`, maka program akan menampilkan pesan bahwa senjata tersebut tidak ditemukan dalam tas. Dengan demikian, output program membantu pengguna mengetahui apakah suatu senjata tersedia dan di posisi mana senjata itu berada pada inventory.

e. Link Youtube : https://youtu.be/bVIjnNiRTE4
