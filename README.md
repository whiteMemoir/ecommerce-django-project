# ecommerce-django-project

Repository ini berisi proyek e-commerce yang dikembangkan menggunakan Django.

## Fitur yang Ditambahkan

 - [x] Tampilan Produk per Kategori
 - [x] Pencarian Produk

## Tambahan Selanjutnya

- [ ] Laman Kontak yang Beirisi Alamat
- [ ] Improve Styling

## Fitur Tambahan

Jika memungkinkan, mungkin akan ditambahkan:

- [ ] Fitur Rating
- [ ] Fitur Komentar

## Instalasi

1. Clone repositori ini:
     ```
     git clone https://github.com/whiteMemoir/ecommerce-django-project.git
     ```
2. Masuk ke folder proyek:
    ```
    cd ecommerce-django-project
    ```
3. Buat virtual environment (opsional):
    ```
    python3 -m venv ecommenv
    ```
4. Aktifkan virtual environment, untuk Linux atau MacOS:
    ```
    source ecommenv/bin/activate
    ```
    Untuk Windows:
    ```
    ecommenv\Scripts\activate
    ```
5. Instal dependensi
    ```
    pip install -r requirements.txt
    ```
6. Buat database lalu jalankan migrasi:
    ```
    python manage.py migrate
    ```
7. Jalankan server lokal:
    ```
    python manage.py runserver
    ```
