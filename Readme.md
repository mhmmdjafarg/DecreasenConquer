# Penentuan rencana studi penerapan algorima decrease and conquer menggunakan algoritma toposort

## Algoritma Topological Sorting (penerapan Decrease and conquer) :pencil2:
Buat kelas `CourseType` yang berfungsi seperti layaknya graf, memiliki atribut nama, array prerequisites dan derajat masuk. Kumpulkan masukkan dari file sebagai array of CourseType, sebut sebagai `ListCourse`.
Algoritma : 
1. Pilih seluruh mata kuliah yang memiliki derajat masuk nol(0), sebut sebagai `0degreeCourse`.
2. kemudian Setiap mata kuliah memiliki derajat masuk nol, telusuri mata kuliah lain yang memiliki 0degreeCourse sebagai prerequisites. Lalu hapus dari prerequisites.
3. Tampilkan ke layar nama mata kuliah 0degreeCourse beserta semesterya.
4. Hapus mata kuliah 0degreeCourse dari ListCourse
5. Ulangi langkah 1 - 4, sampai ListCourse kosong.

## Kebutuhan dan pemasangan :hammer:
Program ini telah teruji pada sistem operasi `windows` dan `python` versi `3.8.7`
*Jika terjadi infinite recursion pada program, perhatikan kembali format file .txt, program tidak menerima jika terdapat `tab`*
*Sesuaikan format seperti `<matakuliah1>, <matakuliah2>, <matakuliah3>.`*

## Pembuat :pushpin:
:runner: Muhammad Jafar Gundari - 13519197
:computer: Teknik Informatika 2019
:books: Institut Teknologi Bandung
:email: 13519197@std.stei.itb.ac.id
:date: Bandung, 1 Maret 2021