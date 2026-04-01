import streamlit as st
import PyPDF2
import google.generativeai as genai
import pickle
import re
import time
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(
    page_title="Hoax Buster Indonesia",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_resources():
    try:
        with open('model_hoax_svm.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
            vectorizer = pickle.load(vec_file)

        return model, vectorizer
    except FileNotFoundError:
        return None, None


def cleaning_text(text):
    text = text.lower()

    text = re.sub(r'[^a-z\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text).strip()

    return text


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text


def ask_gemini(text_berita):
    try:
        model_ai = genai.GenerativeModel('gemini-flash-latest')

        prompt = f"""
        Kamu adalah pakar verifikasi berita. 
        Teks: "{text_berita[:1000]}..."
        Jelaskan singkat kenapa ini terindikasi HOAX.
        """
        response = model_ai.generate_content(prompt)
        return response.text

    except Exception as e:
        if "429" in str(e):
            return "⚠️ AI sedang sibuk (Kuota Free Tier Penuh). Mohon tunggu 30 detik lalu coba lagi."
        else:
            return f"Gagal menghubungi AI: {e}"




st.title("🛡️ Hoax Buster Indonesia")
st.markdown("Sistem Deteksi Berita Palsu Berbasis **SVM** & **Generative AI**")

model, vectorizer = load_resources()

if model is None or vectorizer is None:
    st.error("❌ FILE MODEL TIDAK DITEMUKAN!")
    st.warning("Pastikan file 'model_svm.pkl' dan 'tfidf_vectorizer.pkl' ada di folder yang sama dengan app.py")
    st.stop()

tab1, tab2 = st.tabs(["📝 Input Teks", "📂 Upload PDF"])
final_input_text = ""

with tab1:
    text_input = st.text_area("Masukkan teks berita yang ingin dicek:", height=200)
    if text_input:
        final_input_text = text_input

with tab2:
    uploaded_file = st.file_uploader("Upload dokumen surat/berita (PDF)", type="pdf")
    if uploaded_file:
        with st.spinner("Mengekstrak teks dari PDF..."):
            extracted = extract_text_from_pdf(uploaded_file)
            st.success("PDF Berhasil dibaca!")
            with st.expander("Lihat isi teks asli"):
                st.text(extracted[:1000] + "...")
            final_input_text = extracted

if st.button("🔍 Cek Fakta Sekarang", type="primary"):
    if not final_input_text:
        st.warning("Mohon masukkan teks atau upload file terlebih dahulu.")
    else:
        # 1. Tampilkan status processing
        progress_text = "Memproses teks..."
        my_bar = st.progress(0, text=progress_text)

        # 2. Preprocessing
        my_bar.progress(30, text="Membersihkan teks (Cleaning)...")
        clean_data = cleaning_text(final_input_text)

        # 3. Vectorizing
        my_bar.progress(60, text="Mengubah teks ke angka (Vectorization)...")
        vector_data = vectorizer.transform([clean_data])

        # 4. Prediksi Model Utama
        my_bar.progress(80, text="Kalkulasi Model SVM...")
        prediction = model.predict(vector_data.toarray())[0]

        my_bar.progress(100, text="Selesai!")
        time.sleep(0.5)
        my_bar.empty()

        st.divider()

        if prediction == 1:
            st.error("### 🔴 HASIL: TERINDIKASI HOAX")
            st.write("Sistem mendeteksi pola bahasa yang tidak wajar atau ciri berita palsu.")

            with st.spinner("🤖 Meminta penjelasan ahli (AI Assistant)..."):
                explanation = ask_gemini(final_input_text)

            st.info(f"**Analisis AI:**\n\n{explanation}")

        else:
            st.success("### ✅ HASIL: BERITA VALID / FAKTA")
            st.write("Struktur bahasa terlihat normal dan informatif.")
            st.balloons()