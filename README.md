# Cara Menggunakan

## 1. Prasyarat

- Docker Desktop sudah terpasang dan berjalan.
- Port `1883` (MQTT) dan `5000` (API) tidak dipakai aplikasi lain.

## 2. Jalankan Semua Service

Di root project, jalankan:

```bash
docker compose up --build
```

Service yang akan aktif:

- `broker` (Mosquitto MQTT) di port `1883`
- `api` (Flask) di port `5000`
- `publisher` (kirim suhu otomatis setiap 5 detik)
- `subscriber` (menerima semua data dari topic `sensor/suhu`)

## 3. Kirim Data Manual

### Opsi A - Lewat Browser

1. Buka browser ke `http://localhost:5000`
2. Isi nilai suhu di form.
3. Klik tombol **Kirim**.

Data manual akan dipublish ke topic MQTT `sensor/suhu`.

### Opsi B - Lewat Terminal (PowerShell)

Jalankan perintah berikut dari terminal:

```powershell
Invoke-RestMethod -Uri "http://localhost:5000/send" -Method Post -Body @{ suhu = "30" }
```

Ganti nilai `30` sesuai suhu yang ingin dikirim.

### Opsi C - Lewat Terminal (curl)

```bash
curl -X POST http://localhost:5000/send -d "suhu=30"
```

## 4. Cek Data Terbaru dari API

Buka:

`http://localhost:5000/data`

Endpoint ini mengembalikan JSON berisi data otomatis terbaru dan data manual terbaru.

## 5. Hentikan Service

Tekan `Ctrl + C` di terminal yang menjalankan compose, lalu:

```bash
docker compose down
```
