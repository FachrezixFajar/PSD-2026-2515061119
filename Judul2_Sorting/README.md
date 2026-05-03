TUGAS AKHIR JUDUL 2

a. Judul Program : Fungsi Bubble Sorting dalam mengurutkan skor game

b. Deskripsi Singkat : Program tersebut berfungsi sebagai gambaran fungsi sederhana dalam playlist lagu, di mana pengguna bisa menambahkan lagu ke dalam playlist, menghapus lagu pertama, dan menampilkan seluruh isi dari playlist. Cara kerjanya seperti youtube music/spotify, tetapi dalam bentuk yang sangat sederhana, setiap lagu disimpan sebagai satu elemen, lalu dihubungkan dengan lagu berikutnya sehingga membentuk urutan yang bisa ditelusuri oleh pengguna dari awal hingga akhir.

Struktur data yang saya guanakan adalah Singly Linked List, karena pada playlist tersebut saya hanya membuat playlist yang dapat di setel maju dan tidak bisa mundur, gambaran implementasinya yaitu kumpulan node yang saling terhubung satu arah. Setiap node menyimpan data yang berisi judul lagu dan pointer menuju ke node lagu berikutnya. Algoritma yang saya terapkan meliputi operasi dasar linked list seperti insertion di akhir (menambahkan lagu di selanjutnya), deletion di awal (menghapus lagu pertama) jika pengguna ingin menghapusnya, dan traversal (menampilkan semua lagu dalam playlist). Hal lain yang membuat saya pilih Singly Linked List ini karena fleksibel dan tidak perlu ukuran yang tetap seperti array, dan penambahan data bisa dilakukan secara dinamis. Jadinya sangat cocok jika ingin membuat program dalam bentuk playlist lagu yang sederhana.

c. Source Code :
