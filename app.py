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
PHONE_NUM = "+16692103246"
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

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

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

    st.write("📱", PHONE_NUM)

    # --- SOCILA LINKS ---
    cols = st.columns(len(SOCIAL_MEDIA)+2)

    for index, (plateform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{plateform}]({link})")

# --- Experience & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
"""
- ✔  Strong hands on experience and knowldge in Python, Java, Andriod Developement 
- ✔  Good understand of Cloud Technologies (AWS / GCP) in building scaleable apps
- ✔  Excellent team-player and displaying strong sense of initiative on tasks
- ✔  Strong background in software design patterns/principles, ensuring maintainable & efficient code.
- ✔  Proficient in Agile methodologies, facilitating rapid development cycles and adaptive planning.
- ✔  Proficient in implementing RESTful APIs and microservices architecture, enhancing system integration and scalability.
- ✔  Excellent communication skills, capable of conveying complex technical ideas to non-technical stakeholders.
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write("---")
st.write(
"""
- 👩‍💻 Programming: Python, Java, Javascript, Kotlin, C, Andriod Development
- 📊 Frameworks: ReactJS, ViteJS, Django, Streamlit
- ☁️ Cloud Services: AWS, GCP
- 🗄️ Databases: Postgres, MongoDB, MySQL, Firebase
- 📚 Currently Learning: Tensorflow, OpenCV, Working toward AWS Certification
"""
)

# --- Education Section ---
st.write("#")
st.subheader("Education")
st.write("---")
# San Jose State University
st.markdown("#### San Jose State University, San Jose, CA")
st.markdown("*Master of Science in Software Engineering*")
st.markdown("Aug 2023 - Current (Expected May 2025)")
st.markdown("Cumulative GPA: 3.8/4.0")
st.markdown("Relevant Coursework: Virtual Technologies, Cloud Technologies, Enterprise Software Solutions")

# University of Alberta
st.markdown("#### University of Alberta, Alberta, CA")
st.markdown("*Bachelor of Science in Computer Science with Distinctions*")
st.markdown("Aug 2018 - April 2022")
st.markdown("Cumulative GPA: 3.7/4.0; Dean’s List & First Class Standing: 2020-21, 2021-22")
st.markdown("Relevant Coursework: Software Engineering, Operating Systems, Algorithms & Data Structures, Artificial Intelligence")

# --- WORK HISTORY ---
st.write('#')
st.subheader("Work History")
st.write("---")
# --- JOB 1
st.write("🚧", "**Software Developer | Hi-Tech Seals Inc.**")
st.markdown("May 2022 – Aug 2023")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('#')
st.markdown("🚧 **Software Developer Intern | INVIDI Technologies**")
st.markdown("May 2021 – Aug 2021")
st.write(
"""
- ► Implemented, tested, and deployed CRUD for Web API requests to a database for a new feature.
- ► Helped with deployment by testing, debugging, and resolving issues to ensure the highest level of data security.
- ► Contributed to ideas and suggestions and provided updates on deadlines, designs, and enhancements in team meetings.
"""
)

# --- Projects & Accomplishments ---
st.write('#')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    if link or (link != ""):
        st.write(f"[{project}]({link})")
    else:
        st.write(f"{project}")