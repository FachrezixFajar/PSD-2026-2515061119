a. Judul Program : Fungsi Singly Linked List Pada Playlist Lagu

b. Deskripsi Singkat : Program tersebut berfungsi sebagai gambaran fungsi sederhana dalam playlist lagu, di mana pengguna bisa menambahkan lagu ke dalam playlist, menghapus lagu pertama, dan menampilkan seluruh isi dari playlist. Cara kerjanya seperti youtube music/spotify, tetapi dalam bentuk yang sangat sederhana, setiap lagu disimpan sebagai satu elemen, lalu dihubungkan dengan lagu berikutnya sehingga membentuk urutan yang bisa ditelusuri oleh pengguna dari awal hingga akhir.

Struktur data yang saya guanakan adalah Singly Linked List, karena pada playlist tersebut saya hanya membuat playlist yang dapat di setel maju dan tidak bisa mundur, gambaran implementasinya yaitu kumpulan node yang saling terhubung satu arah. Setiap node menyimpan data yang berisi judul lagu dan pointer menuju ke node lagu berikutnya. Algoritma yang saya terapkan meliputi operasi dasar linked list seperti insertion di akhir (menambahkan lagu di selanjutnya), deletion di awal (menghapus lagu pertama) jika pengguna ingin menghapusnya, dan traversal (menampilkan semua lagu dalam playlist). Hal lain yang membuat saya pilih Singly Linked List ini karena fleksibel dan tidak perlu ukuran yang tetap seperti array, dan penambahan data bisa dilakukan secara dinamis. Jadinya sangat cocok jika ingin membuat program dalam bentuk playlist lagu yang sederhana.

c. Source Code :
<img width="1126" height="2952" alt="pyyyy" src="https://github.com/user-attachments/assets/272186b3-94b3-4afc-9872-d8f8fa98d1a0" />
<img width="879" height="424" alt="Screenshot 2026-04-28 210200" src="https://github.com/user-attachments/assets/5f7c3575-8bfc-4576-a02b-09ccfdefcb2f" />
<img width="888" height="677" alt="Screenshot 2026-04-28 210229" src="https://github.com/user-attachments/assets/6b9bf0d2-beb6-41eb-91e8-1c1e077fbe64" />
<img width="859" height="484" alt="Screenshot 2026-04-28 210252" src="https://github.com/user-attachments/assets/086e25d7-9fe2-4f69-ab7c-cc4efcbe6ea1" />

d.  Output Program : 
<img width="521" height="200" alt="image" src="https://github.com/user-attachments/assets/5108d9e9-6ddb-473e-89e3-382faa4abf30" />

Jika kita memilih opsi 1 maka user diminta untuk memasukan judul lagu yang ingin dimasukan ke dalam playlist.

<img width="514" height="198" alt="image" src="https://github.com/user-attachments/assets/e32a7c1c-6f3b-45b3-9ccc-ff8837fe581a" />

Jika kita memilih opsi 2 maka program akan menghapus lagu yang paling pertama user masukan.

<img width="441" height="210" alt="image" src="https://github.com/user-attachments/assets/ae1407d0-1de0-4315-8555-74298292308b" />

Jika kita memilih opsi 3 maka menampilkan seluruh isi playlist, ini gambarannya jika didalamnya hanya ada satu lagu, maka pointer selanjutnya menunjukan “tidak ada lagu”.

<img width="446" height="197" alt="image" src="https://github.com/user-attachments/assets/187cd501-21a4-4d78-a67e-c75038b74cc7" />

Jika kita memilih opsi 4 maka program akan selesai.
