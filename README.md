# 🌏📚 Proyek Tengah Semester F01: LiteraLoka

## 🌟 Anggota Kelompok F01 
* [Muhammad Hilmy Erryanto](https://github.com/m-hilmy-erryanto) (2206025905)
* [Fernando Valentino Sitinjak](https://github.com/Scarletra) (2206081332)
* [Fathirahma Alyssa Pristanti](https://github.com/alyssapristanti) (2206082215)
* [Chika Marsya Diandra Lumban Gaol](https://github.com/chikamarsyaa) (2206083344)
* [Pradipta Arya Pramudita](https://github.com/Pradiptaa) (2206083685)
* [Leticia Kalila Darlene](https://github.com/leticiakalila) (2206830561)

## 📖 Latar Belakang LiteraLoka
Kami berencana untuk membuat website toko buku bernama LiteraLoka. Website ini pada awalnya dibuat untuk memecahkan masalah terkait literasi di Indonesia yang menempati posisi 64,48 dari skala 1-100. Oleh karena itu, kelompok kami berinisiatif untuk membuat LiteraLoka yang berfokus kepada penjualan buku untuk dapat memudahkan akses kepada buku-buku yang berkualitas bagi masyarakat Indonesia. Di LiteraLoka, user dapat membeli, menjual, bahkan menulis resensi buku. Dengan adanya website ini, kami berharap dapat membantu mengatasi permasalahan literasi di Indonesia dan meningkatkan minat baca masyarakat Indonesia melalui kemudahan dalam mengakses sumber bacaan.

## 📁 Daftar dan Pembagian Tugas Modul
Berikut ini fitur-fitur yang tersedia di LiteraLoka:
### 🗃️ Manajemen Inventori - Nando
Modul khusus untuk super admin, sehingga hanya admin yang bisa mengakses page ini. Fungsionalitas dari page ini adalah sebagai kontrol utama terhadap semua data yang ada di website, mulai dari mengatur buku, hingga mengakses data tiap user. Untuk selain admin yang melakukan login ataupun tidak, akan land di page main

### 💰 Penjualan Buku User - Chika
Modul ini hanya dapat digunakan oleh user yang sedang login untuk menjual buku mereka ke LiteraLoka. Pada page penjualan buku, user dapat menjual buku dengan cara menginput judul, tahun terbit, dan lainnya pada form pengisian. Pada form ini user juga dapat menginput foto dari buku yang akan dijual. Setelah submit form, buku akan ditampilkan pada dataset penjualan.

### 🛒 Shopping Cart & Checkout - Dipta
Modul ini hanya dapat digunakan oleh user yang sedang login. User dapat membeli buku dengan menambahkan ke shopping cart. Setelah user sudah menentukan buku-bukunya, page shopping cart dapat diteruskan ke page checkout, di mana pada page checkout user diminta untuk mengisi form terkait data pengiriman. Setelah form diisi, buku-buku pada shopping cart akan berpindah ke inventori user untuk diakses. 

### 📃 Wishlist - Alyssa
Modul ini hanya dapat digunakan oleh user yang sedang login. Pada halaman wishlist ini nantinya user dapat memasukkan buku yang ingin mereka minati. Untuk memasukkan buku ke dalam wishlist, akan disediakan form khusus bagi user. Pada form ini nantinya user akan diminta judul buku dan kategori buku. Setelah user mengisi form, buku yang dimasukkan akan otomatis berada di halaman wishlist. Wishlist bersifat personalized untuk masing-masing user yang berbeda.

### ✍️ Resensi - Kalila
Modul ini hanya dapat digunakan oleh user yang sedang login untuk menulis resensi. Modul ini akan menampilkan halaman yang berisi daftar semua buku yang ada di katalog, dimana user dapat membuat resensi mereka terhadap suatu buku dengan mengklik buku spesifik mulai menulis pada form yang telah disiapkan. Resensi yang sudah ditulis user akan terlihat di bagian buku tersebut beserta resensi user-user lainnya.

### 🗣️ Review - Hilmy
Modul ini hanya dapat digunakan oleh user yang sedang login. Modul ini bertujuan untuk menampilkan urutan buku-buku terbaik menurut user yang dinilai dari rating yang diberikan untuk buku tersebut. Pada modul ini user dapat memberi rating sekaligus menulis komentar singkat untuk buku tersebut.

## 📑 Sumber Dataset Katalog Buku
[Google API](https://developers.google.com/books/)

## 👥 Roles
| Role  | Description |
| ------------- | ------------- |
| Admin | Admin satu-satunya role yang dapat mengakses modul manajemen inventori |
| User | User disini adalah pengunjung yang punya akun dan sedang login, user bisa menggunakan semua modul kecuali manajemen inventori |
| Guest | Guest adalah pengunjung tanpa akun atau sedang tidak login, guest hanya bisa melihat main page, katalog, halaman review, dan halaman resensi. Guest tidak bisa membeli, menjual, dan mengunggah hal apapun ke website LiteraLoka |