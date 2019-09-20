# Recommendation-System-Algorithms
Dalam repo ini, terdapat algoritma sebagai berikut:
1. Rekomendasi berdasarkan konten (Content based)
2. Rekomendasi berdasarkan user (Collaborative filtering)
3. Rekomendasi Hybrid (berdasarkan user & konten)
4. Asosiasi menggunakan algoritma Apriori
5. A/B Testing untuk menentukan UI yang lebih baik

Menjalankan program diatas menggunakan file "main.py", commandnya seperti dibawah,<br>
![Command untuk menjalankan](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/command.png)

Dari command tersebut, menghasilkan keluaran seperti pada berikut,
![Keluaran program](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/result_program.png)

Dalam repository ini, kita memiliki beberapa metode yang kita coba aplikasikan pada data yang berbeda pula. kita akan coba bahas satu persatu.
<br>
## 1. Rekomendasi berdasarkan konten (Content based)<br>
Pada algoritma ini, rekomendasi dititik beratkan pada karakteristik konten yang ada. Algoritma ini menggunakan data film untuk diolah, yang berisi jenis, genre, rating, dan durasi. Pada tahapan ini dilakukan normalisasi dahulu terhadap data yang ada, lalu dilakukan perhitungan cosine similarity untuk menghitung kesamaan antar kontennya. Hasilnya sebagai berikut
![Hasil content](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/result_content.png)
<br>
## 2. Rekomendasi berdasarkan user (Collaborative filtering)<br>
Collaborative filtering dapat menghasilkan banyak data, kita bisa mendapatkan user mana saja yang mengonsumsi konten yang sama, user yang memiliki selera yang sama dan bahkan dapat merekomendasikan konten kepada user berdasarkan rating yang diberikan oleh user lain. Pada algoritma ini digunakan data yang berisi user dan film yang sudah diberi rating oleh masing masing. Rating merupakan variable yang berisi dari angka 0 - 5, yang merepresentasikan skor yang diberikan oleh user kepada film yang telah ditonton. User akan memasukkan 0 jika belum pernah melihat, dan 5 jika user tersebut sangat suka konten filmnya. Hasilnya sebagai berikut
![Hasil Collaborative](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/result_collab.png)
<br>
## 3. Rekomendasi Hybrid (berdasarkan user & konten)<br>
Pada algoritma ini, digunakan 2 kali pembelajaran. Langkah pertama dilakukan analisa terhadap usernya, bagaimana pemberian rating terhadap filmnya. Setelah itu baru dilakukan pengecekan kesamaan dengan konten, sehingga bisa dihasilkan rekomendasi yang lebih wide dan cocok kepada user tersebut. Hasilnya sebagai berikut
![Confidence support](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/result_hybrid.png)
<br>
## 4. Asosiasi menggunakan algoritma Apriori<br>
Apriori didapatkan dari perhitungan yang menghasilkan angka support dan confidence tertentu. Angka yang dihasilkan menentukan asosiasi antar kedua atau lebih barang yang ditampilkan. Pada penggunaan kali ini, digunakan min_support dan min_confidence sebagai berikut
![Confidence support](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/support_confidence.png)
lalu menghasilkan sebagai berikut
![hasil apriori](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/result_apriori.png)
<br>
## 5. A/B Testing untuk menentukan UI yang lebih baik<br>
Pada penggunaan kali ini, kasus yang ada adalah bagaimana mengukur apakah UI yang baru bisa menggantikan UI yang lama berdasarkan banyaknya user yang me-klik tombol sehingga melanjutkan untuk mengeksplor lebih dalam lagi websitenya lalu dihitung P-Value-nya. Hipotesisnya adalah:<br>
H0 : Pengguna UI A lebih banyak me-klik tombol dibanding pengguna UI B
H1 : Pengguna UI A tidak lebih banyak me-klik tombol dibanding pengguna UI B
<br>
Lalu hasil yang didapatkan seperti berikut
![hasil A/B Testing](https://raw.githubusercontent.com/dzvlfi/Recommendation-System-Algorithms/master/image/result_AB.png)
