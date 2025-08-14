# Kalkulator Pengiriman Barang (Django + Vue)

Aplikasi web full-stack untuk mensimulasikan perhitungan biaya pengiriman barang internasional dan domestik, dibangun sebagai latihan teknis.

## Fitur Utama

-   Backend REST API dengan Django Rest Framework.
-   Frontend interaktif yang dibangun menggunakan Vue.js.
-   Sistem registrasi dan login dengan autentikasi token JWT.
-   Kalkulasi biaya dinamis berdasarkan negara asal, kategori produk, dan berat.
-   Pencarian kota tujuan di seluruh Indonesia.

## Teknologi

-   **Backend**: Python, Django, Django Rest Framework
-   **Frontend**: JavaScript, Vue.js, Vite
-   **Database**: SQLite (default)
-   **Autentikasi**: SimpleJWT
-   **API Pihak Ketiga**: RajaOngkir/Komerce (disimulasikan karena masalah jaringan)

## Cara Menjalankan Secara Lokal

### Backend (Django)

1.  Clone repositori ini.
2.  Navigasi ke folder proyek.
3.  Buat virtual environment: `python -m venv venv`
4.  Aktifkan: `.\venv\Scripts\activate`
5.  Install semua dependensi: `pip install -r requirements.txt`
6.  Buat file `.env` dan isi variabel yang dibutuhkan (`SECRET_KEY`).
7.  Jalankan migrasi: `python manage.py migrate`
8.  Buat superuser: `python manage.py createsuperuser`
9.  Jalankan server: `python manage.py runserver`

### Frontend (Vue)

1.  Navigasi ke folder `freight-frontend`.
2.  Install dependensi: `npm install`
3.  Jalankan server pengembangan: `npm run dev`