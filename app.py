# app.py

import streamlit as st
from utils.file_handler import read_email_content
from agent.email_processor import process_email_with_gpt

st.set_page_config(page_title="E-Posta Özetleyici & Cevaplayan Agent", layout="centered")

st.title("📧 E-Posta Özetleyici ve Cevaplayan AI Agent")
st.markdown("E-posta metninizi yazın ya da bir `.txt` dosyası yükleyin. GPT modeli sizin için analiz yapacak, özet çıkaracak ve cevap taslağı oluşturacak.")

# Kullanıcıdan giriş alma
text_input = st.text_area("✍️ E-posta Metni", height=200, placeholder="Buraya e-posta içeriğini yazın...")
file_input = st.file_uploader("📄 veya bir .txt dosyası yükleyin", type=["txt"])

if st.button("🧠 İşle"):
    # E-posta içeriğini oku
    email_text = read_email_content(text_input, file_input)

    if not email_text.strip():
        st.warning("Lütfen bir e-posta metni girin veya dosya yükleyin.")
    else:
        with st.spinner("🧠 GPT modeli çalışıyor, lütfen bekleyin..."):
            output = process_email_with_gpt(email_text)

        if "error" in output:
            st.error(f"Hata: {output['error']}")
        else:
            st.markdown("---")
            st.subheader("📌 Sonuçlar")

            st.subheader("📝 Özet")
            st.markdown(output["summary"])

            st.subheader("🏷️ Etiket (Kategori)")
            st.markdown(f"**{output['topic']}**")

            st.subheader("✍️ Cevap Taslağı")
            st.text_area("GPT'nin oluşturduğu yanıt:", value=output["reply_draft"], height=200)

            st.subheader("🧠 Eylem Önerisi")
            st.markdown(output["suggested_action"])

            st.subheader("⚡ Öncelik Skoru")
            st.progress(output["priority_score"] / 100)
            st.caption(f"Skor: {output['priority_score']}")

            st.subheader("📅 Tespit Edilen Tarih/Saat")
            st.markdown(output["datetime_info"])
