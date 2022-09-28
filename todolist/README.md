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