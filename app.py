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
PAGE_TITLE = "Harshil Vyas | Digitial CV"
PAGE_ICON = ":wave:"
PHONE_NUM = "+1 (669) 210-3246"
DESCRIPTION = """
 Innovative Software Engineer Specializing in Cloud Computing and Mobile Solutions | AI/ML & LLM Enthusiast
"""
EMAIL = "hvyas330@outlook.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://linkedin.com/in/harshil-vyas/",
    "GitHub" : "https://github.com/Harshil-V/",
}
PROJECTS = {
    "👩🏻‍💻 Pneumonia Classification Application" : "",
    "👩🏻‍💻 TravelEase" : "https://github.com/Harshil-V/CMPE281-Cloud-Project-2",
    "👩🏻‍💻 Cloud Storage Management" : "https://github.com/Harshil-V/CMPE281-Cloud-Project-1",
    "👩🏻‍💻 Academics Without Borders (AWB) - Computational-Science Platform " : "https://github.com/University-of-Eswatini/Eswatini-Project",
}

AWARDS = {
    # "🏆 Pneumonia Classification Application" : "",
    # "🏆 TravelEase" : "https://github.com/Harshil-V/CMPE281-Cloud-Project-2",
    # "🏆 Cloud Storage Management" : "https://github.com/Harshil-V/CMPE281-Cloud-Project-1",
    # "🏆 Academics Without Borders (AWB) - Computational-Science Platform " : "https://github.com/University-of-Eswatini/Eswatini-Project"

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
- ✔️ Strong hands on experience and knowldge in Python, Java, Andriod Developement 
- ✔️ Good understand of Cloud Technologies (AWS / GCP) in building scaleable apps
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Strong background in software design patterns/principles, ensuring maintainable & efficient code.
- ✔️ Proficient in Agile methodologies, facilitating rapid development cycles and adaptive planning.
- ✔️ Proficient in implementing RESTful APIs and microservices architecture, enhancing system integration and scalability.
- ✔️ Excellent communication skills, capable of conveying complex technical ideas to non-technical stakeholders.
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write("---")
st.write(
"""
- 👩‍💻 __Programming__: Python, Java, Javascript, NodeJS, Kotlin, C, Andriod Development
- 📊 __Frameworks__: ReactJS, ViteJS, Express.js, Flask, Django, Streamlit
- ☁️ __Cloud Services__: AWS, GCP, Azure
- 🗄️ __Databases__: Postgres, MongoDB, MySQL, Firebase
- 💻 __Other Technologies__: CI/CD, Ansible, Docker, Datadog, Terraform
- 💿 __Operating Systems__: Linux/Unix, Windows, MacOS 
- 📖 __Currently Learning__: Tensorflow, OpenCV, Working toward AWS Certification
- ✨ __AI/ML__ - CNN, Reinforment Learning, Retrieval-Augmented Generation (RAG)
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
- • Redesigned the company's internal website on AWS, enhancing system architecture by upgrading from legacy code, which
resulted in a 45% improvement in system performance and a 35% increase in scalability.

- • Implemented a CI/CD pipeline using Bitbucket and AWS for software releases, reducing deployment time by 60% and
increasing team productivity by 40%, facilitating faster and more efficient release cycles.

- • Led the development of an Android application for warehouse/inventory management, integrating API calls to an ERP
system, which streamlined inventory tracking processes, enhancing operational efficiency by 30%.

"""
)

# --- JOB 2
st.write('#')
st.markdown("🚧 **Software Developer Intern | INVIDI Technologies**")
st.markdown("May 2021 – Aug 2021")
st.write(
"""
- • Enhanced feature deployment with CRUD operations for Web API to database, boosting data processing efficiency by 25%
and user experience.
- • Ensured highest data security by leading testing and debugging during deployment, reducing security vulnerabilities by 30%.
- • Contributed to ideas and suggestions and provided updates on deadlines, designs, and enhancements in team meetings.
"""
)

# --- Projects & Accomplishments ---
st.write('#')
st.subheader("Projects & Accomplishments")
st.write("---")
if PROJECTS:
    st.markdown("##### Projects")

    for project, link in PROJECTS.items():
        if link or (link != ""):
            st.write(f"[{project}]({link})")
        else:
            st.write(f"{project}")

if AWARDS:
    st.markdown("##### Awards / Accomplishments")