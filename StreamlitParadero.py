import streamlit as st
import requests
from PIL import Image
import pandas as pd

# ===== Page Configuration =====
st.set_page_config(page_title="Ivann James Paradero | Portfolio", layout="wide", page_icon=":sparkles:")

# ===== Sidebar (Profile + Contact only) =====
with st.sidebar:
    st.title("Ivann James Paradero")
    st.write("Bachelor of Science in Computer Science student at Cebu Institute of Technology – University")
    st.markdown("---")

    st.header("Contact")
    st.write("📧 paradero730@gmail.com")
    st.write("📧 ivannjames.paradero@cit.edu")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/Ivann%20James%20Paradero)")
    st.markdown("---")
    st.write("Followers: 4 · Following: 1")
    st.markdown("Achievements: 🦈 Pull Shark · ⚡ Quickdraw")

# ===== Floating Navigation Bar (bottom-right corner) =====
st.markdown("""
    <style>
    .floating-nav {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: rgba(14, 17, 23, 0.9);
        padding: 12px 16px;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .nav-btn {
        background-color: #262730;
        color: white;
        border: none;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        padding: 8px 14px;
        border-radius: 8px;
        text-align: left;
        transition: all 0.3s ease;
    }
    .nav-btn:hover {
        background-color: #1E90FF;
        color: white;
    }
    </style>

    <div class="floating-nav">
        <form action="" method="get">
            <button name="page" value="Home" class="nav-btn">🏠 Home</button>
            <button name="page" value="Goals" class="nav-btn">🎯 Goals</button>
            <button name="page" value="Education" class="nav-btn">🎓 Education</button>
            <button name="page" value="Skills" class="nav-btn">🧠 Skills</button>
            <button name="page" value="CV" class="nav-btn">📄 Curriculum Vitae</button>
        </form>
    </div>
""", unsafe_allow_html=True)

# ===== Get Current Page =====
page = st.query_params.get("page", ["Home"])
if isinstance(page, list):
    page = page[0]

# ==============================
# ===== PAGE 1: HOME =====
# ==============================
if page == "Home":
    st.markdown("""
        <style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
        h1 {font-family:'Poppins',sans-serif;color:#1E90FF;text-align:center;}
        </style><h1>Ivann James Paradero</h1>
    """, unsafe_allow_html=True)

    st.write("I’m **Ivann James Paradero**, a 21-year-old Bachelor of Science in Computer Science student at **Cebu Institute of Technology – University**.")
    st.write("Passionate about technology and problem-solving, I enjoy building applications ranging from games to practical systems. My projects reflect my curiosity and versatility—whether it’s developing **2D Java RPGs**, creating **platformer games**, designing a **parking management system**, or building a **Windows Forms calculator** in **C#**.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔭 I’m currently working on:")
        st.write("Improving my existing projects and exploring new ideas in game and application development.")

        st.subheader("🌱 I’m currently learning:")
        st.write("Python, Django Framework, and expanding my knowledge in web development and cybersecurity.")

    with col2:
        st.subheader("💬 Ask me about:")
        st.write("Java development, C# applications, PHP projects, and game design concepts.")

        st.subheader("⚡ Fun fact:")
        st.write("I love freediving, which helps me clear my mind and stay focused outside of coding.")

    st.markdown("---")

    # Tech Stack
    st.header("💻 Tech Stack")
    st.write("Java · AssemblyScript · C · C# · Kotlin · C++ · PHP · Python · HTML5 · CSS3 · MySQL · Firebase · Figma · Gimp · Canva · Aseprite")

    # Portfolio / Pinned Projects
    st.header("📌 Pinned Projects")
    projects = [
        {
            "title": "#DannyGerman: The Bugged World",
            "desc": "An engaging 2D pixel-art RPG developed in Java. The game immerses players in a mysterious forest journey.",
            "lang": "Java",
            "url": "https://github.com/Ivann0730/JAVA-Capstone"
        },
        {
            "title": "Official-Statement",
            "desc": "CyberSecurity Official Statement.",
            "lang": "Markdown",
            "url": "https://github.com/Ivann0730/Official-Statement"
        },
        {
            "title": "The Adventures of Joe and Marie",
            "desc": "A fun and challenging platformer game where two characters work together to explore tricky levels.",
            "lang": "Java",
            "url": "https://github.com/Smoll05/hardstack-capstone"
        },
        {
            "title": "PARKYU",
            "desc": "A parking management system tailored for university students and staff, providing a seamless parking experience.",
            "lang": "PHP",
            "url": "https://github.com/SuperaNova/PARKYU"
        },
        {
            "title": "InfoSys Calculator",
            "desc": "A Windows Forms application in C# that performs basic and advanced arithmetic operations.",
            "lang": "C#",
            "url": "https://github.com/Ivann0730/InfoSys-Calculator"
        }
    ]

    cols = st.columns(2)
    for i, proj in enumerate(projects):
        with cols[i % 2]:
            st.subheader(proj['title'])
            st.write(proj['desc'])
            st.caption(f"Language: {proj['lang']}")
            st.markdown(f"[🔗 View on GitHub]({proj['url']})")

    st.markdown("---")

    # GitHub Stats and Trophies
    st.header("📊 GitHub Stats")
    st.image("https://github-readme-stats.vercel.app/api?username=Ivann0730&show_icons=true&theme=radical", use_container_width=True)

    st.header("🏆 GitHub Trophies")
    st.image("https://github-profile-trophy.vercel.app/?username=Ivann0730&theme=radical&margin-w=10&margin-h=10", use_container_width=True)

# ==============================
# ===== PAGE 2: GOALS =====
# ==============================
elif page == "Goals":
    st.markdown("<h1 style='text-align:center;'>🎯 My Goals</h1>", unsafe_allow_html=True)
    st.write("""
    As a **Computer Science student**, my goals are centered on continuous learning, technical growth, and personal development. 
    These objectives guide me toward becoming a skilled and responsible professional in the tech industry.
    """)

    st.subheader("🎓 Academic & Learning Goals")
    st.write("""
    - Strengthen my understanding of **data structures, algorithms, and software design principles**.  
    - Develop a solid grasp of **cybersecurity**, **artificial intelligence**, and **web development**.  
    - Consistently improve my problem-solving skills through **coding challenges** and **competitive programming**.  
    - Build a strong academic portfolio by completing impactful **capstone projects**.
    """)

    st.subheader("💻 Career & Technical Goals")
    st.write("""
    - Contribute to open-source projects and collaborate with developers worldwide.  
    - Create innovative applications that solve **real-world problems** using modern technologies.  
    - Gain experience in **backend and frontend development**, **database management**, and **cloud computing**.  
    - Prepare for certifications such as **AWS Certified Developer**, **Google IT Professional**, or **CompTIA Security+**.  
    - Build a personal brand as a versatile and reliable software developer.
    """)

    st.subheader("🌱 Personal Growth Goals")
    st.write("""
    - Maintain a balance between academics, work, and personal life.  
    - Continue exploring new places and meeting people who inspire creativity and growth.  
    - Mentor or help other students who are starting their journey in Computer Science.  
    - Keep learning every day — not just about technology, but about becoming a better version of myself.
    """)

    st.success("🚀 My ultimate goal is to become a skilled, well-rounded software developer who creates technology that makes people's lives better.")

# ==============================
# ===== PAGE 3: EDUCATION =====
# ==============================
elif page == "Education":
    st.markdown("<h1 style='text-align:center;'>🎓 Education</h1>", unsafe_allow_html=True)
    st.write("""
    My educational journey reflects my growth from childhood curiosity to a focused passion for computer science.
    Each stage has shaped not only my academic skills but also my discipline and motivation to improve continuously.
    """)

    st.subheader("🏫 Cebu Institute of Technology – University")
    st.write("**Bachelor of Science in Computer Science**  \n*Cebu City, Philippines | 2023 – Present*")

    st.subheader("🏫 Science and Technology Education Center (STEC)")
    st.write("**Senior High School – ABM Strand**  \n*With Honors – 92 GWA*  \n*Lapu-Lapu City, Philippines | 2021 – 2023*")

    st.subheader("🏫 Indiana Aerospace University")
    st.write("**Elementary (Grades 1–5)**  \n*Lapu-Lapu City, Philippines*")

    st.subheader("🏫 Marigondon Elementary School")
    st.write("**Elementary (Grade 6)**  \n*Lapu-Lapu City, Philippines*")

# ==============================
# ===== PAGE 4: SKILLS =====
# ==============================
elif page == "Skills":
    st.markdown("<h1 style='text-align:center;'>🧠 Skills</h1>", unsafe_allow_html=True)
    st.write("""
    - **Programming Languages:** Java, C, C#, C++, Python, PHP, HTML, CSS  
    - **Frameworks & Tools:** Django, Firebase, MySQL, Figma, Canva, Gimp, Aseprite  
    - **Soft Skills:** Leadership, teamwork, adaptability, creativity, and time management  
    - **Technical Interests:** Game development, cybersecurity, software engineering  
    """)

# ==============================
# ===== PAGE 5: CV =====
# ==============================
elif page == "CV":
    st.markdown("<h1 style='text-align:center;'>📄 Curriculum Vitae</h1>", unsafe_allow_html=True)
    st.write("Here’s a copy of my full CV. You can preview it below or download it:")

    cv_url = "https://raw.githubusercontent.com/Ivann0730/AutoBiographyStreamlit/main/Ivann_James_Paradero_CV.pdf"
    viewer_url = f"https://docs.google.com/gview?embedded=true&url={cv_url}"

    st.markdown(f"[📄 Open CV in a new tab (preview)]({viewer_url})")

    st.markdown(f"<iframe src='{viewer_url}' width='100%' height='800px' style='border:none; border-radius:10px;'></iframe>", unsafe_allow_html=True)

    if st.button("📥 Prepare Download"):
        try:
            resp = requests.get(cv_url, timeout=15)
            resp.raise_for_status()
            st.download_button(
                label="📥 Download CV (PDF)",
                data=resp.content,
                file_name="Ivann_James_Paradero_CV.pdf",
                mime="application/pdf"
            )
        except requests.RequestException:
            st.error("⚠️ Unable to fetch the CV from GitHub right now. Please try again later.")
