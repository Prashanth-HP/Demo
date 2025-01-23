import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # Add a title
    st.title("Hari Prashanth Ravichandran")

    # Add a brief introduction
    st.write("Ex-Intern@ Edunet Foundation,Infosys SpringBoard, Aspiring Data Science Student")


    # Sidebar with icons
    st.sidebar.markdown(
        """
        <style>
        .menu-icon {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .menu-icon img {
            width: 25px;
            height: 25px;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    menu = [
        ("Home", "🏠"),
        ("Education", "🎓"),
        ("Experience","🏢"),
        ("Projects", "📂"),
        ("Contact", "📞"),
    ]

    # Render menu with icons
    choice = st.sidebar.radio(
        "Navigation",
        [item[0] for item in menu],
        format_func=lambda name: f"{dict(menu).get(name)} {name}",
    )

    if choice == "Home":
        home()
    elif choice == "Education":
        education()
    elif choice == "Experience":
        experience ()
    elif choice == "Projects":
        projects()
    elif choice == "Contact":
        contact()

#--------------------------------------------------------Home-----------------------------------------------------------------------------------------------------------------------------------------
def home():
    st.header("Welcome to My Portfolio")
    st.write("Here, you'll find information about my skills, projects, education, and how to contact me.")

#-----------------------------------------------------------Projects----------------------------------------------------------------------------------------------------------------------------------
def projects():
    st.header("My Self-Projects")
    st.write("Here are some of the projects I've worked on:")

    # Example of a project
    st.write("### Project 1: Air Quality Water Pollution")
    st.write("Description:  Coded a tool to analyze and visualize air and water pollution data across the globe.")
    st.write("Technologies: Python,  Pandas, Matplotlib.")
    st.write("Key Features:\n 1. Processed and analyzed pollution datasets \n 2. Developed bar and line chart visualizations \n 3. Highlighted top 20 countries affected by air and water pollution.")
    st.write("GitHub: [Project Link](https://github.com/Prashanth-HP/Data_Analysis/tree/main/Air%20Quality%20Water%20population)")

    
    st.write("### Project 2: Facebook EDA")
    st.write("Description:  Analyzed Facebook data to explore user counts, gender differences in post interactions, and trends using various visualizations")
    st.write("Technologies: Python, Pandas,NUmpy, Matplotlib")
    st.write("Key Features:\n 1. Analyzed user counts and gender-based post interactions. \n 2. Visualized insights with bar, line, and clustered line charts.")
    st.write("GitHub: [Project Link](https://github.com/Prashanth-HP/Data_Analysis/tree/main/Facebook%20Data)")

    st.write("### Project 3: Netflix EDA")
    st.write("Description:  Explored Netflix data to analyze content trends and user preferences in 2021")
    st.write("Technologies: Python, Pandas")
    st.write("Key Features:\n 1. Analyzed data for content type, release year, and genre trends. \n 2. Visualized findings using bar charts, line graphs")
    st.write("GitHub: [Project Link](https://github.com/Prashanth-HP/Data_Analysis/tree/main/Netflex%20Anlaysis)")



#-----------------------------------------------------Education----------------------------------------------------------------------------------------------------------------------------------------
def education():
    st.header("My Education")
    st.write("Here is a brief overview of my academic background:")

    st.write("### Bachelor of Technology in Artificial Intelligence & Machine Learning")
    st.write("Institution: K RAMAKRISHNAN COLLEGE OF ENGINEERING")
    st.write("Duration: 2022 - Present")
    st.write("Key Subjects: Machine Learning, Data Analysis, Data Visualization")

    st.write("### 12th Grade")
    st.write("Institution: Sacred Heart Higher Secondary School")
    st.write("Duration: 2021 - 2022")
    st.write("Key Subjects:Physics, Chemistry, Mathematics, Computer Science")

    st.write("### 10th Grade")
    st.write("Institution: St Arnold's Matriculation School")
    st.write("Duration: 2019 - 2020")
    st.write("Key Subjects: Mathematics, Science")

#---------------------------------------------------------Experience----------------------------------------------------
def experience():
    st.header("Intership Experience")
    st.write("## Data Visualization Internship(Remote) at Infosys SpringBoard")
    st.write("Duration: October-December'24")
    st.write("Task: \n 1. Data Collection, Preprocessing, Transformation \n 2. Creating Powerbi through Cleaned Dataset \n 3. Integrated Streamlit with Functional PowerBI Dashboard")
    st.write("Tools: Python, Pandas , Streamlit, Bcrypt, FPDF, PowerBI")
    st.write("[Certificate](https://drive.google.com/drive/u/0/folders/1kVNGoaFBu3P7IlKDzPDpuT-V0AZsVJ8D)")


#---------------------------------------------------------Contact page content-------------------------------------------
def contact():
    st.header("Contact Me")
    st.write("You can reach me via email: gowthamhari2103@gmail.com")
    st.write("Or connect with me on LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/hariprashanth--r/)")
    # Resume download button
    st.write("Click below to download my resume:")
    with open("Hari_Prashanth_Resume .pdf", "rb") as resume_file:
        st.download_button(
            label="Download Resume",
            data=resume_file,
            file_name="Hari_Prashanth_Resume .pdf",
            mime="application/pdf"
        )

import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # Add a title
    st.title("Hari Prashanth Ravichandran")

    # Add a brief introduction
    st.write("Artificial Intelligence Intern @ Edunet Foundation, Aspiring Data Science Student and Ex-Intern @ Infosys SpringBoard.")


    # Sidebar with icons
    st.sidebar.markdown(
        """
        <style>
        .menu-icon {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .menu-icon img {
            width: 25px;
            height: 25px;
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    menu = [
        ("Home", "🏠"),
        ("Education", "🎓"),
        ("Experience","🏢"),
        ("Projects", "📂"),
        ("Contact", "📞"),
    ]

    # Render menu with icons
    choice = st.sidebar.radio(
        "Navigation",
        [item[0] for item in menu],
        format_func=lambda name: f"{dict(menu).get(name)} {name}",
    )

    if choice == "Home":
        home()
    elif choice == "Education":
        education()
    elif choice == "Experience":
        experience ()
    elif choice == "Projects":
        projects()
    elif choice == "Contact":
        contact()

#--------------------------------------------------------Home-----------------------------------------------------------------------------------------------------------------------------------------
def home():
    st.subheader("Welcome to My Portfolio")
    st.image("My photo.jpg", caption=None, width=None)
    st.write("Here, you'll find information about my skills, projects, education, and how to contact me.")

#-----------------------------------------------------------Projects----------------------------------------------------------------------------------------------------------------------------------
def projects():
    st.header("My Self-Projects")
    st.write("Here are some of the projects I've worked on:")

    # Example of a project
    st.write("### Project 1: Air Quality Water Pollution")
    st.write("Description:  Coded a tool to analyze and visualize air and water pollution data across the globe.")
    st.write("Technologies: Python,  Pandas, Matplotlib.")
    st.write("Key Features:\n 1. Processed and analyzed pollution datasets \n 2. Developed bar and line chart visualizations \n 3. Highlighted top 20 countries affected by air and water pollution.")
    st.write("GitHub: [Project Link](https://github.com/Prashanth-HP/Data_Analysis/tree/main/Air%20Quality%20Water%20population)")

    
    st.write("### Project 2: Facebook EDA")
    st.write("Description:  Analyzed Facebook data to explore user counts, gender differences in post interactions, and trends using various visualizations")
    st.write("Technologies: Python, Pandas,NUmpy, Matplotlib")
    st.write("Key Features:\n 1. Analyzed user counts and gender-based post interactions. \n 2. Visualized insights with bar, line, and clustered line charts.")
    st.write("GitHub: [Project Link](https://github.com/Prashanth-HP/Data_Analysis/tree/main/Facebook%20Data)")

    st.write("### Project 3: Netflix EDA")
    st.write("Description:  Explored Netflix data to analyze content trends and user preferences in 2021")
    st.write("Technologies: Python, Pandas")
    st.write("Key Features:\n 1. Analyzed data for content type, release year, and genre trends. \n 2. Visualized findings using bar charts, line graphs")
    st.write("GitHub: [Project Link](https://github.com/Prashanth-HP/Data_Analysis/tree/main/Netflex%20Anlaysis)")



#-----------------------------------------------------Education----------------------------------------------------------------------------------------------------------------------------------------
def education():
    st.subheader("My Education")
    st.write("Here is a brief overview of my academic background:")

    st.write("### Bachelor of Technology in Artificial Intelligence & Machine Learning")
    st.write("Institution: K RAMAKRISHNAN COLLEGE OF ENGINEERING")
    st.write("Duration: 2022 - Present")
    st.write("Key Subjects: Machine Learning, Data Analysis, Data Visualization")

    st.write("### 12th Grade")
    st.write("Institution: Sacred Heart Higher Secondary School")
    st.write("Duration: 2021 - 2022")
    st.write("Key Subjects:Physics, Chemistry, Mathematics, Computer Science")

    st.write("### 10th Grade")
    st.write("Institution: St Arnold's Matriculation School")
    st.write("Duration: 2019 - 2020")
    st.write("Key Subjects: Mathematics, Science")

#---------------------------------------------------------Experience----------------------------------------------------
def experience():
    st.subheader("Intership Experience")
    st.write("## Data Visualization Internship(Remote) at Infosys SpringBoard")
    st.write("Duration: October-December'24")
    st.write("Task: \n 1. Data Collection, Preprocessing, Transformation \n 2. Creating Powerbi through Cleaned Dataset \n 3. Integrated Streamlit with Functional PowerBI Dashboard")
    st.write("Tools: Python, Pandas , Streamlit, Bcrypt, FPDF, PowerBI")
    st.write("[Certificate](https://drive.google.com/drive/u/0/folders/1kVNGoaFBu3P7IlKDzPDpuT-V0AZsVJ8D)")


#---------------------------------------------------------Contact page content-------------------------------------------
def contact():
    st.subheader("Contact Me")
    st.write("You can reach me via email: gowthamhari2103@gmail.com")
    st.write("Or connect with me on LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/hariprashanth--r/)")
    # Resume download button
    st.write("Click below to download my resume:")
    with open("Hari_Prashanth_Resume .pdf", "rb") as resume_file:
        st.download_button(
            label="Download Resume",
            data=resume_file,
            file_name="Hari_Prashanth_Resume .pdf",
            mime="application/pdf"
        )
