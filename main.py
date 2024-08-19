import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="My Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

def show_home():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        img = Image.open('me.png')
        st.image(img, width=300)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Hi, I'm Irsyad")
        st.write("""
        I am a fourth year student of Computer Science at Indraprasta PGRI University.
        Possesses strong analytical skills, capable of gathering and processing data, designing strategies and plans based on analyzed data, as well as creating predictive or estimations models from such data.
        Additionally, possesses excellent intrapersonal skills such as adaptability, teamwork, and enthusiasm for learning new things.
        """)

def show_projects():
    st.title("Projects")
    
    projects = [
        {
            "title": "Prediksi Penyakit Ginjal Kronis",
            "description": "Model prediksi penyakit ginjal kronis yang diimplementasikan dalam aplikasi web menggunakan Streamlit. Sebuah web app yang memungkinkan pengguna untuk melakukan diagnosa awal terhadap kemungkinan terjadinya penyakit ginjal kronis. Aplikasi ini memanfaatkan model prediksi yang telah dilatih untuk memberikan hasil yang akurat berdasarkan data input dari pengguna. Streamlit digunakan untuk membangun antarmuka pengguna yang interaktif dan mudah digunakan..",
            "link": "https://kidney-prediction.streamlit.app/"
        },
  
    ]
    
    for project in projects:
        st.subheader(project['title'])
        st.write(project['description'])
        st.markdown(f"[Go to {project['title']}]({project['link']})", unsafe_allow_html=True)
        st.markdown("---")

def show_dashboard():
    st.title("Dashboard")
    
    st.subheader("Prediksi Ginjal Kronis")
    grafik1 = Image.open('distribusi variabel kategorik.png')
    st.image(grafik1, caption="Distribusi Variabel Kategorik", width=300)
    
    st.subheader("Prediksi Ginjal Kronis")
    grafik2 = Image.open('distribusi variabel numerik.png')
    st.image(grafik2, caption="Distribusi Variabel Numerik", width=300)

menu = st.sidebar.radio("Menu", ["Home", "Projects", "Dashboard"])

if menu == "Home":
    show_home()
elif menu == "Projects":
    show_projects()
elif menu == "Dashboard":
    show_dashboard()
