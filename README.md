a. Judul Program : Fungsi Singly Linked List Pada Playlist Lagu

b. Deskripsi Singkat : Program tersebut berfungsi sebagai gambaran fungsi sederhana dalam playlist lagu, di mana pengguna bisa menambahkan lagu ke dalam playlist, menghapus lagu pertama, dan menampilkan seluruh isi dari playlist. Cara kerjanya seperti youtube music/spotify, tetapi dalam bentuk yang sangat sederhana, setiap lagu disimpan sebagai satu elemen, lalu dihubungkan dengan lagu berikutnya sehingga membentuk urutan yang bisa ditelusuri oleh pengguna dari awal hingga akhir.

Struktur data yang saya guanakan adalah Singly Linked List, karena pada playlist tersebut saya hanya membuat playlist yang dapat di setel maju dan tidak bisa mundur, gambaran implementasinya yaitu kumpulan node yang saling terhubung satu arah. Setiap node menyimpan data yang berisi judul lagu dan pointer menuju ke node lagu berikutnya. Algoritma yang saya terapkan meliputi operasi dasar linked list seperti insertion di akhir (menambahkan lagu di selanjutnya), deletion di awal (menghapus lagu pertama) jika pengguna ingin menghapusnya, dan traversal (menampilkan semua lagu dalam playlist). Hal lain yang membuat saya pilih Singly Linked List ini karena fleksibel dan tidak perlu ukuran yang tetap seperti array, dan penambahan data bisa dilakukan secara dinamis. Jadinya sangat cocok jika ingin membuat program dalam bentuk playlist lagu yang sederhana.

c. Source Code :
<img width="378" height="138" alt="image" src="https://github.com/user-attachments/assets/a4d4dcbe-ee7d-4630-8693-4cda4d9dca44" />


   = membuat class dengan nama Node
   = membuat fungsi untuk menyimpan lagu di dalam node
   = menyimpan nama lagu ke dalam node
   = pointer ke lagu selanjutnya, defaultnya berupa none

			     = membuat class dengan nama Playlist untuk menyimpan semua lagu
			     = membuat fungsi untuk playlist
			     = penunjuk untuk lagu pertama, jika none maka kosong

				          = membuat fungsi untuk menambah lagu
				          = membuat node baru yang berisi lagu
				          = jika pada head kosong
				          = lagu yang ditambahkan akan langsung jadi head/terdepan
				          = jika tidak maka
				          = memulai dari lagu pertama
				          = dan jalan sampai lagu terakhir

				          = lagu baru akan disambungkan di akhir

								      = membuat fungsi hapus lagu
								      = jika pada head kosong/none
								      = maka playlist kamu kosong
								      = jika tidak maka
								      = tampilkan lagu yang dihapus
								      = lalu geser head ke lagu
								         Setelahnya
						      = membuat fungsi untuk menampilkan playlist
						      = jika node kosong maka
						      = tampikan playlist kamu kosong!
						      = jika tidak maka
						      = memulai dari awal
						      = gunakan loop jika masih ada node
						      = maka tampilkan lagu tersebut
						      = dan pindah ke node depan lalu ulangi loop
						      = jika dalam playlist tidak ada lagu lagi maka
						         Tampilkan tidak ada lagu
						      = membuat fungsi utama yang bernama main
						      = membuat objek playlist()

						      = membuat loop ketika situasi true maka
						      = tampilkan menu playlist
						      = tampilkan 1. Tambah lagu
						      = tampilkan 2. Hapus lagu pertama
						      = tampilkan 3. Tampilkan Playlist
						      = tampilkan 4. Keluar

						      = user diminta memasukan input dari pilihan
						         menu
						      = jika memilih 1
						      = user diminta memasukan nama lagu
						      = memanggil fungsi tambah lagu

						      = jika memilih 2
						      = memanggil fungsi hapus lagu

						      = jika memilih 3
						      = memanggil fungsi tampilkan isi playlist

						      = jika memilih 4
						      = menampilkan program selesai
dengan break					      = menghentikan program dengan break

						      = jika user memasukan angka selain pilihan
						      = maka tampilkan pilihan tidak valid


						      = digunakan untuk menjalankan program
						         main/utama

d.  Output Program : 








Jika kita memilih opsi 1 maka user diminta untuk memasukan judul lagu yang ingin dimasukan ke dalam playlist.









Jika kita memilih opsi 2 maka program akan menghapus lagu yang paling pertama user masukan.









Jika kita memilih opsi 3 maka menampilkan seluruh isi playlist, ini gambarannya jika didalamnya hanya ada satu lagu, maka pointer selanjutnya menunjukan “tidak ada lagu”.









Jika kita memilih opsi 4 maka program akan selesai.
