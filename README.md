Django UserCreationForm merupakan suatu calss pada django untuk membuat form pembuatan akun baru yang berisi username, password1 dan password2, password2 hanya untuk  memverifikasi bahwa password yang dimasukkan sudah benar.  Kelebihannya ialah ia menyediakan validasi standar, serta mencegah duolikasi username. Kelemahannya ialah kita tidak bisa emnambahkan bidang lain seperti emal dll.

Autentikasi merupakan proses validasi penggguna, apakah valid atau tidak. Sedangkan otorisasi ialah proses selanjutnya setelah autentikasi, untuk menentukan hak ases untuk pengguna.

Cookies merupakan file teks yang berisi data yang dikirim oleh server web kepada browser pengguna, Django menggunakan cookie untuk mengelola data sesi pengguna, seperti waktu login dan logout.

Penggunaan cookies secara umum tidak aman secara default dalam pengembangan web, karena ada risiko yang harus diwaspadai, seperti:
a. Cookies dapat dicuri oleh pihak ketiga yang dapat mengakses jaringan yang sama dengan pengguna, misalnya dengan menggunakan teknik sniffing atau man-in-the-middle. Hal ini dapat menyebabkan pencurian identitas, penyalahgunaan data, atau serangan session hijacking. Untuk mencegah hal ini, cookies harus dikirimkan melalui protokol HTTPS yang terenkripsi, dan disetel dengan atribut secure=True2.
b. Cookies dapat dimodifikasi oleh pengguna atau pihak ketiga yang dapat mengakses browser web pengguna, misalnya dengan menggunakan alat pengembang atau ekstensi browser. Hal ini dapat menyebabkan data yang tidak valid, tidak konsisten, atau berbahaya dikirimkan ke server web. Untuk mencegah hal ini, cookies harus divalidasi dan disaring oleh server web sebelum diproses, dan disetel dengan atribut httponly=True2 agar tidak dapat diakses oleh kode JavaScript di sisi klien.
c. Cookies dapat mengandung informasi pribadi atau sensitif yang dapat membahayakan privasi pengguna jika dibocorkan, disalahgunakan, atau disimpan terlalu lama. Untuk mencegah hal ini, cookies harus dienkripsi, dihapus setelah masa berlaku habis, dan meminta persetujuan pengguna sebelum disetel, sesuai dengan hukum dan regulasi yang berlaku.

Mengimplementasikan fungsi registrasi login dan logout dengan cara membuat fungsi register, login dan logout pada views.py pada direktori main.

Menampilkan detail informasi pengguna itu dengan mengunakan request.COOKIE.



TUGAS 5

1. a. Element Selector, berguna untuk mengubah properti dengan tag HTML yang sama. element selector ini cocok digunakan saat kita hanya ingin mengubah beberapa komponen dengan tag yang sama.

b. id selector, berguna untuk mengubah properti dengan menandakan id untuk tag yang ingin diubah. cocok digunakan saat ingin mengubah bagian tertentu saja pada dokumen.

c. class selector, berguna unengubah properti pada class tertentu saja.

2. tag table untuk membuat table, tag header untuk membuat header, tag footer untuk membuat footer, tag head untuk membuat kepala dari program, body untuk membuat badan dari program.