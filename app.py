from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-img.png"

# --- General Setting ---
NAME = "Harshil Vyas"
PAGE_TITLE = "DIGITAL RESUME | Harshil Vyas"
PAGE_ICON = ":wave:"
DESCRIPTION = """
 Innovative Software Engineer Specializing in Cloud Computing and Mobile Solutions 
"""
EMAIL = "hvyas330@outlook.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://linkedin.com/in/harshil-vyas/",
    "GitHub" : "https://github.com/Harshil-V/",
}
PROJECTS = {
    "🏆 Pneumonia Classification Application" : "",
    "🏆 CMPE 281 Cloud Computing Project - TravelEase" : "https://github.com/Harshil-V/CMPE281-Cloud-Project-2",
    "🏆 CMPE 281 Cloud Computing Project - CLoud Storage Management" : "https://github.com/Harshil-V/CMPE281-Cloud-Project-1",
    "🏆 Academics Without Borders (AWB) - Computational-Science Platform " : "https://github.com/University-of-Eswatini/Eswatini-Project"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load CSS, PDF, & PROFILE PIC --- 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True) 

with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ---  HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume.name,
        mime="application/octet-stream", 
    )
    st.write("📧", EMAIL)

    # --- SOCILA LINKS ---
    cols = st.columns(len(SOCIAL_MEDIA)+2)

    for index, (plateform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{plateform}]({link})")

# --- Experience & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
"""
- ✔ Strong hands on experience and knowldge in Python, Java, Andriod Developement 
- ✔ Good understand of Cloud Technologies (AWS / GCP) in building scaleable applications
- ✔ Excellent team-player and displaying strong sense of initiative on tasks
- ✔ Strong background in software design patterns/principles, ensuring maintainable & efficient code.
- ✔ Proficient in Agile methodologies, facilitating rapid development cycles and adaptive planning.
- ✔ Proficient in implementing RESTful APIs and microservices architecture, enhancing system integration and scalability.
- ✔ Excellent communication skills, capable of conveying complex technical ideas to non-technical stakeholders.
"""
)


