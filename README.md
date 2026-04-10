📊 Engagement Rate Calculator (Flask)

📌 Deskripsi

Aplikasi web sederhana menggunakan Python Flask untuk menghitung Engagement Rate pada media sosial berdasarkan jumlah like, comment, share, dan followers.

Engagement Rate dihitung dengan rumus:

[
(Like + Comment + Share) / Followers \times 100%
]

---

🎯 Fitur

- Input jumlah Like, Comment, Share, Followers
- Validasi input (tidak boleh kosong / negatif / nol)
- Menghitung Engagement Rate otomatis
- Menampilkan hasil dalam bentuk persentase
- Keterangan hasil:
  - Engagement Rendah
  - Engagement Sedang
  - Engagement Tinggi
- Tampilan web sederhana dengan HTML & CSS
- Menggunakan Flask ("render_template")

---

🗂️ Struktur Folder

project_engagement/
│
├── app.py
└── templates/
    └── index.html

---

⚙️ Teknologi yang Digunakan

- Python
- Flask
- HTML
- CSS

---

▶️ Cara Menjalankan

1. Install Flask

pip install flask

2. Masuk ke folder project

cd project_engagement

3. Jalankan program

python app.py

4. Buka di browser

http://127.0.0.1:5000/

---

🧠 Cara Kerja Program

1. User menginput data (like, comment, share, followers)
2. Program memvalidasi input menggunakan "if-else"
3. Data dihitung menggunakan fungsi:
   def hitung_engagement(...)
4. Hasil ditampilkan di halaman web
5. Program memberikan kategori engagement

---

⚠️ Validasi

- Input tidak boleh kosong
- Input harus berupa angka
- Followers tidak boleh nol
- Nilai tidak boleh negatif

---

📈 Kategori Engagement

- < 1% → Rendah
- 1% – 5% → Sedang
- «5% → Tinggi»

---

👩‍💻 Author

Safa Kamilah Putri Syam
Universitas Negeri Makassar
Jurusan Bisnis Digital