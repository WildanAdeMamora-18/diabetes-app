# Aplikasi Prediksi Diabetes dengan Flask 🩺

Proyek ini merupakan aplikasi web sederhana untuk memprediksi risiko diabetes menggunakan algoritma Machine Learning **Decision Tree** dan framework **Flask**.

---

## 🧠 Dataset

Dataset yang digunakan adalah **Pima Indians Diabetes Dataset** yang terdiri dari 768 data dan 8 fitur utama seperti:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 🚀 Fitur Aplikasi

- Input data pasien melalui form web
- Prediksi risiko diabetes (Positif / Negatif)
- Tampilan antarmuka dengan HTML dan CSS
- Backend Flask menggunakan model `.pkl` (pickle)

---

## 🔧 Cara Menjalankan Aplikasi

1. **Aktifkan Virtual Environment (opsional):**

   ```bash
   python -m venv venv
   venv\Scripts\activate

   ```

2. **Install Dependensi secara manual : **

  ```bash
   pip install flask
   pip install scikit-learn
   pip install numpy

  ```

3. **Jalankan Aplikasi : **

   ```bash
   python app.py

  ```
   

4. **Buka di browser : **
   http://localhost:5000
