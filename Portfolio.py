#cd Portfolio

#streamlit run Portfolio.py

import streamlit as st
from PIL import Image
import base64

def set_custom_style():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            border-radius: 0.5rem;
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        h1, h2, h3 {
            color: #2C3E50;
        }
        .highlight {
            background-color: #e9ecef;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Caleb Traxler's Portfolio", layout="wide")
    set_custom_style()
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Replace with your actual image path
        image = Image.open("output.png")
        st.image(image, width=275)
    
    with col2:
        st.title("Caleb Traxler")
        st.subheader("Data Scientist, ML Engineer, Entrepreneur, and Investor")
        st.write("Contact Me : (805) 377-8182 | calebtraxler34@gmail.com | traxlerc@uci.edu")
        st.write("Visit Websites : [LinkedIn](https://www.linkedin.com/in/calebtraxler) | [GitHub](https://www.github.com/calebtraxler) | [Traxler Technology](https://traxler.streamlit.app)")
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["About Me", "Education", "Experience", "Projects", "Entrepreneurship", "Investments"])
    
    with tab1:
        st.header("About Me")
        st.write("""
        Hello, my name is Caleb Traxler. 
    
        I'm a data scientist, machine learning engineer, investor and an aspiring entrepreneur with a passion for innovation and space exploration. 
        As a UCLA Mathematics and Computer Science Alumni (Class of 2024) and current graduate student at UC Irvine, 
        I bring a strong technical foundation to my work. My experience as an Ex-Data Scientist and ML Engineer at Amgen has honed my 
        skills in applying cutting-edge technologies to real-world problems.
    
        Beyond my technical pursuits, I'm an active investor in both real estate and securities markets, always looking for new 
        opportunities to grow and diversify my portfolio. My entrepreneurial spirit has led me to found Traxler Technology, 
        where we're working on advancing humanity's reach into the cosmos through innovative Mars exploration and colonization solutions.
        
    
        In my free time, I enjoy:
        - Traveling to new places
        - Visiting amusement parks
        - Eating amazing foods
        """)

        def get_binary_file_downloader_html(bin_file, file_label='File'):
            with open(bin_file, 'rb') as f:
                data = f.read()
            bin_str = base64.b64encode(data).decode()
            href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
            return href

        if st.button("Download Resume"):
            file_path = "ResumeFinalpro.docx (8).pdf"
    
            try:
                with open(file_path, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
        
                st.download_button(
                    label="Click here to download",
                    data=PDFbyte,
                    file_name="CalebTraxler_Resume.pdf",
                    mime="application/octet-stream"
                )
            except FileNotFoundError:
                st.error("Resume file not found. Please check the file path.")
    
        # Display personal interest photos
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.subheader("Traveling - Japan")
            st.image("travel/japan.png", caption="My latest travel adventure")

            st.image("travel/japan2.png", caption="My latest travel adventure")
            # Replace the placeholder with your actual travel photo:
            # st.image("path_to_your_travel_photo.jpg", caption="My latest travel adventure")
    
        with col2:
            st.subheader("Amusement Parks")
            st.image("parks/universal.png", caption="Fun at the Universal Studios amusement park")

            st.image("parks/stormtroopers.png", caption="Fun at the Disneyland amusement park")
            # Replace the placeholder with your actual amusement park photo:
            # st.image("path_to_your_amusement_park_photo.jpg", caption="Fun at the amusement park")
    
        with col3:
            st.subheader("Food")
            st.image("food/crab.png", caption="Eating crab on the Santa Barbra pier")

            st.image("food/omlet.png", caption="Eating tamagoyaki in Japan.")
            # Replace the placeholder with your actual gym photo:
            # st.image("path_to_your_gym_photo.jpg", caption="Staying fit at the gym")
    
    with tab2:
        st.header("Education")

        with st.expander("M.S. Data Science - UC Irvine"):
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                st.image("Education/uci_image.png", width=100)
            with col2:
                st.write(" ")
                st.subheader("University of California Irvine (UCI)")
            st.write("September 2024 - Expected December 2025")
            st.write("I am pursuing a Master of Science in Data Science at UCI with a focus in machine learning and artificial intelligence at the UCI School of Information and Computer Sciences.")
            st.write("• Concentrations in Machine Learning, Computer Vision and Artificial Intelligence")
            st.write("• UCI Master of Data Science Scholarship Recipient")
            st.write("• Accelerated Masters in Data Science Program (~15 months)")

        with st.expander("B.S. Mathematics and Computer Science - UCLA"):
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                st.image("Education/ucla_image.png", width=100)
            with col2:
                st.write(" ")
                st.subheader("University of California Los Angeles (UCLA)")
            st.write("September 2022 - June 2024")
            st.write(" Graduated from UCLA with a Bachelor Degree in Mathematics and Computer Science. I was involved in many activities and societies: Undergraduate Mathematics Student Association (UMSA), AI Safety Fellowship. Phi Theta Kappa Honors Society. Undergraduate Mathematics Research under the supervision of Professor Shiba Biswal.")
            st.write("• Joint Degree with Concentrations in Applied Mathematics and Computer Science")
            st.write("• GPA: 3.81/4.00")
            st.write("• UCLA Mathematics and Computer Science Alumni, Class of 2024")

        with st.expander("A.S. Mathematics, Physics and Computer Science - Moorpark College"):
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                st.image("Education/mpc_image.png", width=100)
            with col2:
                st.write(" ")
                st.subheader("Moorpark College")
            st.write("August 2020 - June 2022")
            st.write("I graduated from Moorpark College in 2022 and transferred to UCLA. At Moorpark College I studied Mathematics, Physics and Computer Science. I was also an active partcipant of many activities and societies: Deans List (2020-2022), Honor Roll (2020 - 2022), Phi Theta Kappa Honors Society 2020-present, Nasa Community College Aerospace Scholars Internship, and I was a Mathematics tutor ")
            st.write("• GPA: 4.00/4.00")
    
    with tab3:
        st.header("Experience")
        
        with st.expander("Founder and CEO - Traxler Technology"):
            st.subheader("Traxler Technology, Irvine, CA")
            st.write("June 2024 - Present")
            st.write("• Founded a company focused on advancing Mars exploration and colonization")
            st.write("• Developing interactive tools and simulations for Mars-related research")
            st.write(" At Traxler Technology, our mission is to advance humanity's reach into the cosmos by exploring innovative solutions for Mars exploration and colonization. We believe in a future where humans live and thrive on multiple planets. Explore our interactive tools and simulations to learn more about the Red Planet and how we plan to establish a sustainable human presence on Mars.")
            st.write("• [Visit Traxler Technology](https://traxler.streamlit.app)")
        
        with st.expander("Data Science and ML Engineer - Amgen"):
            st.subheader("Amgen, Thousand Oaks, CA")
            st.write("June 2024 - September 2024")
            st.write("• Built a rare disease prioritization model using Python and generative AI, achieving 96% accuracy")
            st.write("• Accelerated a year-long scoring process to just a few days")
            st.write("I joined the Technology and Innovation Lab team at Amgen for a 10-week internship focusing on accelerating R&D through AI and digital technologies, involving project-based and experiential learning. Focused on applying machine learning and data science for predictive and prescriptive model development.")
        
        with st.expander("AI-Safety Fellowship - UCLA"):
            st.subheader("UCLA AI Safety Fellowship, Los Angeles, CA")
            st.write("January 2024 - March 2024")
            st.write("• Developed practical skills in ML, including neural networks using PyTorch and micrograd")
            st.write("• Explored AI safety and alignment challenges")
            st.write(" I joined UCLA's AI Safety team, I was engaged in advanced computer vision projects, developed models to enhance image recognition and analysis. I also learned about the risk associated with the rapid development of artificial intelligence.")
        
        with st.expander("Undergraduate Mathematics Researcher - UCLA"):
            st.subheader("UCLA, Los Angeles, CA")
            st.write("March 2023 - June 2023")
            st.write("• Led a COVID-19 research project, analyzing data using Python and Jupyter notebooks")
            st.write("• Developed innovative bifurcation diagrams for predictive modeling")
        
        with st.expander("Engineering and Design Internship - NASA"):
            st.subheader("NASA (Remote)")
            st.write("February 2022 - August 2022")
            st.write("• Collaborated on a Mars rover capstone project")
            st.write("• Designed a modern Mars rover blueprint, introducing ML and AI systems")
    
    with tab4:
        st.header("Projects")
        
        with st.expander("Numerical Image Recognition"):
            st.subheader("September 2023 - December 2023")
            st.write("• Developed a two-layer CNN for number classification, achieving 94% accuracy")
            st.write("• Enhanced model performance through hyperparameter tuning")
        
        with st.expander("Image Degradation and Restoration"):
            st.subheader("September 2023 - December 2023")
            st.write("• Constructed a MATLAB project on image degradation and restoration")
            st.write("• Implemented an embedded notch filter to eliminate noise frequencies")
    
    with tab5:
        st.header("Entrepreneurship")
        st.subheader("Traxler Technology")
        st.write("""
        As the Founder and CEO of Traxler Technology, I'm leading our mission to advance humanity's reach into the cosmos. 
        We're exploring innovative solutions for Mars exploration and colonization, believing in a future where humans 
        live and thrive on multiple planets.
        """)
        st.write("Key Focus Areas:")
        st.write("• Developing interactive tools and simulations for Mars research")
        st.write("• Exploring sustainable technologies for Mars colonization")
        st.write("• Collaborating with space agencies and private space companies")
        st.markdown("[Explore Traxler Technology](https://traxler.streamlit.app)")
    
    with tab6:
        st.header("Investments")
        st.subheader("Real Estate")
        st.markdown("""
        <div class="highlight">
        <h4>First Property Investment - Topeka, Kansas</h4>
        • Purchased first real estate property at 22 years old<br>
        • Currently renovating the property<br>
        • Plans to refinance and rent out for passive income<br>
        • Actively seeking next property investment in Texas by end of 2025
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Securities")
        st.write("Active investor in the stock market and other securities")
        st.write("• Diversified portfolio across various sectors")
        st.write("• Focus on long-term growth and value investing")
    
    st.markdown("---")
    st.write("© 2024 Caleb Traxler. All rights reserved.")

if __name__ == "__main__":
    main()
