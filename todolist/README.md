# Application Deployment Link
### main deployment: https://pbp-assignment-deploy.herokuapp.com/
### todolist page (Login Required): https://pbp-assignment-deploy.herokuapp.com/todolist/


## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
csrf_token merupakan tools yang disediakan oleh django yang berguna untuk mencegah adanya serangan CSRF atau Cross-Site Request Forgery. Tanpa adanya csrf_token dapat mengakibatkan error pada django project

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, dengan menggunakan tag-tag yang disediakan oleh HTML seperti tag input yang dapat menjadi radio button atau input field yang dapat diketik oleh user.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah user selesai mengisi form dan telah di click button submit maka akan terjadi suatu request yang berlabel POST atau request yang ingin memasukan data pada database. Pada todolist, diberikan beberapa batasan sehingga sebelum terjadi request POST maka data yang diinput oleh user akan divalidasi terlebih dahulu, jika tidak lolos maka user akan diminta untuk input ulang serta ditunjukan error message. Jika berhasil maka POST request akan terjadi dan data yang telah diinput oleh user akan dimasukan pada database. Data pada database tersebut kemudian dapat dipanggil oleh function pada views yang membutuhkan data dan kemudian dapat di parse sebagai dictionary lalu di display pada HTML yang di return oleh function views tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. run 
```
python3 manage.py startapp todolist
```
2. Menambahkan path todolist/ pada urls.py project_django yang menginclude urls.py pada todolist serta menambahkan todolist pada INSTALLED_APPS settings.py pada project_django

3. Membuat path-path pada urls.py todolist yang berisi path utama pada todolist/ kemudian anak path todolist yang terdiri atas login/, register/, logout/ dan create-task/

4. Membuat models pada models.py pada todolist sesuai ketentuan soal. Untuk model user yang memerlukan model User dari django juga diimport
```
from django.contrib.auth.models import User 
```
sehingga dapat digunakan pada urls.py

5. Membuat fungsi-fungsi seperti login, register, todolist (require login -> menggunakan syntax @login_required lalu meredirect ke login page jika belum login), dan create-task pada views.py todolist

6. Membuat file-file HTML untuk setiap pagenya

7. run
```
python manage.py makemigrations
python manage.py migrate
```

<hr>
Timeframe local deployment broke, change repo and change project, and redo step 1 to 7
<hr>

8. Untuk deployment perlu setup database heroku pg (SQL not working in heroku) dengan add heroku postgre di heroku website dan mengganti credentials pada DATABASES pada settings.py project_django agar sesuai dengan credentials yang diberikan oleh heroku pg.

9. Create 2 account dengan 3 dummy data each pada deployment.

# CSS - Tugas 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline CSS: inline CSS adalah sebuah CSS yang dituliskan secara langsung pada sebuah tag HTML menggunakan attribute style="" yang akan berisi attribute CSS yang ingin diberikan hanya pada tag tersebut.
2. Internal CSS: internal CSS adalah sebuah CSS yang diletakan secara langsung (biasanya diletakan pada bagian tag head sebuah file HTML). pada sebuah file HTML menggunakan tag 
```
<style></style> 
```
3. External CSS: external CSS adalah sebuah file CSS yang terpisah dari file HTML dimana nanti file HTML yang membutuhkan file CSS tersebut dapat menginclude file CSS tersebut (biasanya diletakan pada bagian tag head sebuah file HTML) menggunakan 
```
<link rel="stylesheet" type="text/css" href="namaFile.css" />
```

## Jelaskan tag HTML5 yang kamu ketahui.
Pada HTML5 terdapat berbagai macam tag baru yang ditambahkan. Dari tag-tag yang ditambahkan yang menurut saya cukup familiar antara lain adalah:
1. &lt;embed&gt; : tag embed adalah sebuah tag yang dapat menampung external interactive content atau plug-in.
2. &lt;footer&gt; : tag footer adalah sebuah tag yang mensimbolkan bagian bawah / footer dari sebuah HTML.
3. &lt;header&gt; : tag header adalah sebuah tag yang mensimbolkan bagian atas / header dari sebuah HTML.
4. &lt;nav&gt; tag nav adalah sebuah tag yang mensimbolkan bagian navigasi dari sebuah HTML.
5. &lt;video&gt; tag video adalah tag yang menyimbolkan sebuah file video.
6. &lt;section&gt; tag yang secara umum mensimbolkan bagian dari suatu file HTML.

Extra:
1. Untuk tag lengkap HTML5 (Termaksud tag sebelum HTML5) dan deskripsinya: https://www.tutorialrepublic.com/html-reference/html5-tags.php
2. Untuk tag tambahan pada HTML5 dan deskripsinya: https://www.tutorialspoint.com/html5/html5_new_tags.htm

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Secara dasar terdapat 4 jenis selector antara lain:
1. id selector: selector pada CSS yang berdampak pada elemen yang memiliki suatu id dimana pada CSS dapat digunakan simbol hash (#) yang diikuti dengan nama id yang ingin diberikan efek CSS.
2. class selector: selector pada CSS yang berdampak pada elemen yang diberikan nama class tertentu dimana pada CSS digunakan simbol titik (.) yang diikuti dengan nama class yang ingin diberikan efek CSS.
3. element selector: selector pada CSS yang berdampak pada elemen tag HTML dimana pada CSS hanya perlu dituliskan nama tag yang ingin diberikan efek CSS.
4. universal selector: selector pada CSS yang berdampak pada semua elemen pada HTML dimana pada CSS digunakan tanda bintang (*) untuk menyimbolkan universal selector.

Dari keempat selector dasar tersebut dapat dibentuk kombinasi selector-selector dasar antara lain:
1. element class selector: Penggunaan kombinasi ini adalah dengan element.class dimana hal tersebut pada CSS hanya akan berdampak pada elemen yang memiliki nama class tertentu.
2. group selector: Penggunaan ini di CSS ditujukan agar elemen atau class yang ingin memiliki efek yang sama, CSS nya tidak dituliskan secara terus menerus (repetition). Hal ini dapat digunakan pada css dengan elemen / class diikuti dengan tanda koma (,) dan dilanjutkan lagi dengan elemen / class berikutnya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pada tugas ini, karena diperlukan framework CSS maka saya memutuskan untuk menggunakan bootstrap (tailwind broken for some reason) sehingga untuk dapat memasukan bootstrap pada project ini, diperlukan tag
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```
2. Setelah tag tersebut sudah ada, maka dapat dibuat juga file style.css (mengikuti nama pada template base.html) pada directory ~/static/css dimana CSS ini akan menjadi CSS external dan utama pada project_django.
3. Mengimplementasikan CSS pada style.css dan menggunakan bootstrap untuk memodifikasi todolist pada page login, register, create-task, dan main page todolist. Setelah itu, mengganti table pada todolist.html dengan model cards seperti yang diminta soal sekaligus menambahkan efek hover (mengubah warna) dengan menggunakan class:hover pada external CSS.
4. Setelah modifikasi selesai, mengecek responsiveness webpage agar dapat digunakan pada berbagai jenis device dengan ukuran yang berbeda-beda. Implementasi menggunakan @media diikuti dengan max-width dan lebar device pada external CSS.