# RimbaGuide: Outdoor & Travel AI Assistant

RimbaGuide adalah aplikasi chatbot berbasis Artificial Intelligence yang dirancang khusus untuk membantu penggiat alam bebas dalam merencanakan petualangan mereka. Proyek ini dibangun menggunakan **Streamlit** untuk antarmuka web yang interaktif dan **Google Gemini 2.5 Flash** sebagai otak pemrosesan bahasa alaminya.

Aplikasi ini tidak hanya memberikan jawaban teks, tetapi juga menyajikan dashboard informasi yang membantu manajemen logistik dan persiapan fisik pendaki secara *real-time*.

---

## Fitur Utama

- **NLP Processing**: Memahami dan merespons pertanyaan seputar jalur pendakian, perlengkapan, dan tips keselamatan dengan gaya bahasa yang santai namun informatif.
- **Persistent Chat Memory**: Menggunakan `st.session_state` untuk mengingat konteks percakapan selama sesi berlangsung.
- **Interactive Dashboard**: Dilengkapi dengan *checklist* persiapan perlengkapan dan kartu informasi cuaca.
- **Responsive UI**: Tata letak dua kolom yang dioptimalkan untuk memberikan pengalaman pengguna yang padat informasi namun tetap rapi.
- **Privacy-First API Integration**: Pengguna memasukkan API Key mereka sendiri secara manual untuk memastikan keamanan dan manajemen kuota yang transparan.

## Tech Stack

- **Language**: Python
- **Framework UI**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash (via `google-genai`)
- **Deployment**: Streamlit Community Cloud

## Tampilan Aplikasi

![Cuplikan Antarmuka RimbaGuide](https://github.com/arizalirsyad/rimbaguide-chatbot/blob/main/Screenshot%202026-05-10%20141145.png)

## Cara Mencoba

Aplikasi ini sudah dideploy secara publik. Kamu bisa mencobanya langsung melalui tautan berikut:

**[https://rimbaguide-chatbot-uhaedfbjmovhyuk2itpjxp.streamlit.app/]**

**Langkah Penggunaan:**
1. Dapatkan API Key Google AI secara gratis di [Google AI Studio](https://aistudio.google.com/).
2. Buka aplikasi RimbaGuide.
3. Masukkan API Key kamu pada kolom pengaturan di panel sebelah kiri.
4. Mulailah mengobrol dengan RimbaGuide seputar rencana pendakianmu!

## Instalasi Lokal

Jika kamu ingin menjalankan proyek ini di mesin lokal kamu:

1. Clone repositori ini:
   git clone https://github.com/arizalirsyad/rimbaguide-chatbot.git
   cd rimbaguide-chatbot

2. Instal dependensi yang diperlukan:
   pip install -r requirements.txt
   
3. Jalankan aplikasi:
   streamlit run rimbaguide_app.py
