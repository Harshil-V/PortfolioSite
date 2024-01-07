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
PAGE_TITLE = "DIGITAL RESUME | {NAME}"
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

st.title("Hello!!")

