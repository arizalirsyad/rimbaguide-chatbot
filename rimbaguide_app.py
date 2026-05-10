import streamlit as st
from google import genai

# 1. Konfigurasi Halaman & Tema 
st.set_page_config(
    page_title="RimbaGuide ⛰️", 
    page_icon="https://cdn-icons-png.flaticon.com/512/2822/2822453.png", 
    layout="wide" 
)

st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stChatMessage {
        border-radius: 15px;
        margin-bottom: 10px;
    }

    [data-testid="stSidebar"] {
        background-color: #1b4332;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    .status-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar (Pengaturan & Info Tambahan) 
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=300", use_container_width=True)
    st.markdown("### ⚙️ Pengaturan")
    google_api_key = st.text_input("Google AI API Key:", type="password")
    
    st.divider()
    
    st.markdown("### 🚩 Jalur Populer")
    st.info("**Gunung Ungaran**\n\nJalur Mawar & Perantunan.")
    st.warning("**Gunung Merbabu**\n\nJalur Thekelan (Favorit).")
    
    st.divider()
    
    if st.button("🗑️ Reset Percakapan", use_container_width=True):
        st.session_state.pop("chat", None)
        st.session_state.pop("messages", None)
        st.rerun()

# 3. Header & Banner 

col_title, col_img = st.columns([2, 1])

with col_title:
    st.title("⛰️ RimbaGuide: Pemandu Virtual")
    st.markdown("""
    Selamat datang di pusat informasi pendakian. Aku siap membantu persiapan fisik, 
    manajemen logistik, hingga rekomendasi perlengkapan terbaik untuk petualanganmu.
    """)

st.divider()

# 4. Layout Utama (Chat & Dashboard) 

chat_col, info_col = st.columns([2, 1])

with info_col:
    st.subheader("📋 Checklist Persiapan")
    st.checkbox("Sepatu Trail/Hiking")
    st.checkbox("Carrier & Raincover")
    st.checkbox("Logistik (Minimal 3 hari)")
    st.checkbox("P3K & Emergency Lamp")
    
    st.subheader("💡 Tips Cepat")
    with st.expander("Persiapan Fisik"):
        st.write("Lakukan jogging rutin dan latihan beban 2 minggu sebelum pendakian.")
    with st.expander("Etika Pendaki"):
        st.write("Jangan tinggalkan apapun selain jejak, jangan ambil apapun selain foto.")

with chat_col:
    if not google_api_key:
        st.warning("Silakan masukkan API Key di sidebar untuk mengaktifkan AI.")
        st.stop()

    if ("genai_client" not in st.session_state) or getattr(st.session_state, "_last_key", None) != google_api_key:
        try:
            st.session_state.genai_client = genai.Client(api_key=google_api_key)
            st.session_state._last_key = google_api_key
            st.session_state.pop("chat", None)
            st.session_state.pop("messages", None)
        except:
            st.error("API Key Bermasalah.")
            st.stop()

    persona = "Kamu adalah RimbaGuide, asisten pendakian yang suportif dan sangat ahli dalam jalur gunung di Indonesia khususnya Jawa Tengah."
    if "chat" not in st.session_state:
        st.session_state.chat = st.session_state.genai_client.chats.create(
            model="gemini-2.5-flash",
            config={"system_instruction": persona}
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_placeholder = st.container(height=500)
    with chat_placeholder:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    if prompt := st.chat_input("Tanya tentang jalur pendakian atau logistik..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_placeholder:
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                response = st.session_state.chat.send_message(prompt)
                answer = response.text if hasattr(response, "text") else str(response)
                st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
