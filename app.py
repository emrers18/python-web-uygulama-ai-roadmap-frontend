import streamlit as st 
import requests

BACKEND_URL = "https://python-web-uygulama-ai-roadmap-backend-e537.onrender.com/roadmap"

st.set_page_config(
    page_title = "AI Yol Haritası",
    page_icon = "🤖",
    layout = "centered"
)

st.title("AI Yol Haritası 🧭")
st.write("Bir alan seç: AI sana hazır yol haritası göndersin.")

secim = st.selectbox(
    "Alan Seçin",
    ["yapay_zeka", "derin_ogrenme", "nlp"]
)

if st.button("Yol Haritası Göster"):
    try:
        response = requests.post(BACKEND_URL, json = {"alan": secim}, timeout= 50)

        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.success(f"Seçilen alan: {data['alan']}")
            st.subheader("Yol Haritası")
            for i,adim in enumerate(data["adimlar"], start = 1):
                st.write(f"{i}. {adim}")
    except Exception as e:
        st.error(f"Hata oluştu: {str(e)}")
