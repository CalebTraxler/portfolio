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
            padding: 5rem;
            border-radius: 3rem;
            margin-bottom: 3rem;
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Caleb Traxler's Portfolio", layout="wide")
    set_custom_style()
    
    col1, col2 = st.columns([1, 2])
    
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
    
   # Custom CSS to style the tabs
    st.markdown("""
    <style>
        .stTabs {
            background-color: #f0f2f6;
            padding: 6px 0px;
            border-radius: 6px;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            justify-content: space-evenly;
            flex-wrap: wrap;
        }
        .stTabs [data-baseweb="tab"] {
            height: auto;
            min-height: 28px;
            white-space: normal;
            background-color: transparent;
            border-radius: 4px 4px 0 0;
            color: #31333F;
            font-size: 10px;
            font-weight: 500;
            align-items: center;
            justify-content: center;
            border: none;
            transition: all 0.2s ease;
            border-bottom: 1px solid transparent;
            margin: 2px;
            padding: 4px 8px;
            text-align: center;
            word-break: keep-all;
            overflow-wrap: anywhere;
        }
        .stTabs [aria-selected="true"] {
            background-color: white;
            color: #4CAF50;
            font-weight: 700;
            border-bottom-color: #4CAF50;
        }
        .stTabs [data-baseweb="tab"]:hover {
            color: #4CAF50;
            background-color: rgba(255, 255, 255, 0.5);
        }
        @media (max-width: 600px) {
            .stTabs [data-baseweb="tab"] {
                flex: 1 1 auto;
                font-size: 9px;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # Create the tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "About Me", "Education", "Experience", "Projects", "Investments"
    ])
    
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
        where we're working on deriving insights from data to make a positive and lasting impression on humanity though many different avenues. 
        
    
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
            col1, col2 = st.columns([1, 8])
            with col1:
                st.image("Experience/the_x.png", width=100)
            with col2:
                st.write(" ")
                st.subheader("Traxler Technology, Irvine, CA")
            st.write("June 2024 - Present")
            st.write("• Founded a company focused on advancing Mars exploration and colonization")
            st.write("• Developing interactive tools and simulations for Mars-related research")
            st.write("At Traxler Technology, our mission is to advance humanity's reach into the cosmos by exploring innovative solutions for Mars exploration and colonization. We believe in a future where humans live and thrive on multiple planets. Explore our interactive tools and simulations to learn more about the Red Planet and how we plan to establish a sustainable human presence on Mars.")
            st.write("• [Visit Traxler Technology](https://traxler.streamlit.app)")
    
        with st.expander("Data Science and ML Engineer Internship- Amgen"):
            col1, col2 = st.columns([1, 5])
            with col1:
                st.image("Experience/amgen_img.png", width=150)
            with col2:
                st.subheader("Amgen, Thousand Oaks, CA")
            st.write("June 2024 - September 2024")
            st.write("• Built a rare disease prioritization model using Python and generative AI, achieving 96% accuracy")
            st.write("• Accelerated a year-long scoring process to just a few days")
            st.write("Joined the Technology and Innovation Lab at Amgen for a 10-week data science and machine learning role, focused on accelerating research and development using machine learning, AI and digital technologies. Used python to build a rare disease prioritization model able to automate a rare disease scoring process with generative artificial intelligence, yielding an accuracy of 96%. Accelerated a year-long scoring process into a few days.")
    
        with st.expander("AI-Safety Fellowship - UCLA"):
            col1, col2 = st.columns([1, 8])
            with col1:
                st.image("Experience/ai_safety.png", width=75)
            with col2:
                st.write(" ")
                st.subheader("UCLA AI Safety, Los Angeles, CA")
            st.write("January 2024 - March 2024")
            st.write("• Developed practical skills in ML, including neural networks using PyTorch and micrograd")
            st.write("• Explored AI safety and alignment challenges")
            st.write("Worked alongside fellow machine learning students at UCLA and gained insights about AI existential risks and the impacts of AI advancements on humanity's future. Developed practical stills in ML, including neural networks by using tools like PyTorch and micrograd. Explored AI safety and alignment challenges, contributing to understanding and mitigating potential failure modes in AI systems.")
    
        with st.expander("Undergraduate Mathematics Researcher - UCLA"):
            col1, col2 = st.columns([1, 8])
            with col1:
                st.image("Experience/ucla_math.png", width=100)
            with col2:
                st.write(" ")
                st.subheader("UCLA Mathematics Department, Los Angeles, CA")
            st.write("March 2023 - June 2023")
            st.write("• Led a COVID-19 research project, analyzing data using Python and Jupyter notebooks")
            st.write("• Developed innovative bifurcation diagrams for predictive modeling")
            st.write("Led a COVID-19 research project at UCLA Mathematics Department in Junior year, under Professor Shiba Biswals supervision. Analyzed Orange County COVID-19 data using Jupyter notebooks and python; focused on data processing an in-depth analysis in python. Implemented error analysis methods using Matlab, enhancing accuracy. Utilized SIR and SEIR differential equations and nonlinear equations to develop an innovative bifurcatin diagram, hence identifying a critical transcritical bifurcation threshold used for predictions.")
    
        with st.expander("Engineering and Design Internship - NASA"):
            col1, col2 = st.columns([1, 8])
            with col1:
                st.image("Experience/nasa.png", width=100)
            with col2:
                st.write(" ")
                st.subheader("NASA (Remote)")
            st.write("February 2022 - August 2022")
            st.write("• Collaborated on a Mars rover capstone project")
            st.write("• Designed a modern Mars rover blueprint, introducing ML and AI systems")
            st.write("Collaborated in a NASA National Community College Aerospace Scholars program and completed a mission capstone project; addressing complications with today's Mars rovers. Designed a modern Mars rover blueprint; the project served as an introduction to machine learning and AI systems. I was further able to build this project's hardware and software as a personal project. Improved NASA's Mars rover functionality and adaptability with this design.")
    
    with tab4:
        st.header("Projects")

        # Function to display images with customizable width
        def display_image(path, caption, width=400):
            st.image(path, caption=caption, width=width)

        # Function to display two images side-by-side
        def display_images_side_by_side(image1, caption1, image2, caption2, width1=300, width2=300):
            col1, col2 = st.columns(2)
            with col1:
                st.image(image1, caption=caption1, width=width1)
            with col2:
                st.image(image2, caption=caption2, width=width2)

        with st.expander("UCLA Modeling COVID-19 Research"):
            st.subheader("Modeling and Data Analysis")
            st.write("• Conducted research on modeling COVID-19 spread and impact")
            st.write("• Analyzed and visualized complex datasets related to the pandemic")
            display_images_side_by_side(
                "Projects/Modeling/data.png", "COVID-19 Data Visualization",
                "Projects/Modeling/bifurcation.png", "Bifurcation Diagram",
                width1=600, width2=600
            )

        with st.expander("Machine Learning Projects"):
            st.subheader("Two Layer Neural Network for Binary Classification (Even or Odd)")
            st.write("• Implemented a neural network for classifying numbers as even or odd")
            st.write("• Achieved high accuracy in binary classification tasks")
            display_image("Projects/ML/ml1.png", "Neural Network Performance", width=300)

            st.subheader("K-means Clustering")
            st.write("• Developed a K-means clustering algorithm for data segmentation")
            st.write("• Applied the algorithm to various datasets to identify patterns")
            display_images_side_by_side(
                "Projects/ML/clustering1.png", "K-means Clustering Result 1",
                "Projects/ML/clustering2.png", "K-means Clustering Result 2",
                width1=500, width2=500
            )

        with st.expander("AI Projects"):
            st.subheader("Bayesian Network")
            st.write("• Created a Bayesian network for probabilistic reasoning")
            st.write("• Applied the network to solve complex inference problems")
            display_image("Projects/AI/bayesian.png", "Bayesian Network Structure", width=600)

            st.subheader("Sokoban Game with Admissible Heuristic")
            st.write("• Implemented the Sokoban puzzle game with an AI solver")
            st.write("• Developed an admissible heuristic for efficient pathfinding")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("Projects/AI/sako1.png", caption="Sokoban Game State 1", width=200)
            with col2:
                st.image("Projects/AI/sako2.png", caption="Sokoban Game State 2", width=215)
            with col3:
                st.image("Projects/AI/sako3.png", caption="Sokoban Game State 3", width=400)

        with st.expander("Math Imaging Projects"):
            st.subheader("Feature Enhancement via Brightness Adjustments")
            st.write("• Developed algorithms for feature extraction using brightness adjustments")
            st.write("• Enhanced image features for improved analysis and recognition")
            display_images_side_by_side(
                "Projects/Imaging/dark.png", "Dark Image",
                "Projects/Imaging/light.png", "Light Image",
                width1=500, width2=500
            )

            st.subheader("Image Sharpening")
            st.write("• Implemented image sharpening techniques to enhance details")
            st.write("• Compared various sharpening algorithms and their effects")
            display_image("Projects/Imaging/sharpening.png", "Image Sharpening Result", width=450)

            st.subheader("Notch Filter using Fourier Transforms")
            st.write("• Applied Fourier transforms to implement a notch filter")
            st.write("• Removed specific frequency components to reduce image noise")
            display_image("Projects/Imaging/notch.png", "Notch Filter Application", width=450)
    
    with tab5:
        st.header("Real Estate Investments")
    
        st.markdown("""
        
        <h4>First Property Investment - Topeka, Kansas</h4>
        • Purchased first real estate property at 22 years old<br>
        • Currently renovating the property<br>
        • Plans to refinance and rent out for passive income<br>
        • Actively seeking next property investment in Texas by end of 2025

        """, unsafe_allow_html=True)

        st.write(" ")
    
        st.write("I've just purchased my first real estate property in Topeka, Kansas at 22 years old! This home is definitely a fixer upper, however I am ready to take on the challenge. With some hard work and dedication, I plan to transform it, refinance, and rent it out and make this investment worthwhile. This is just the beginning of my real estate journey. I am already looking ahead to purchase my next property in Texas before the end of 2025. Stay tuned for more updates as I continue to grow my real estate portfolio!")
    
        # Display images in a row
        col1, col2, col3 = st.columns(3)
    
        with col1:
            image1 = Image.open("Investments/1.jpg")
            st.image(image1, caption="Property View 1", use_column_width=True)
    
        with col2:
            image2 = Image.open("Investments/2.png")
            st.image(image2, caption="Property View 2", use_column_width=True)
    
        with col3:
            image3 = Image.open("Investments/3.png")
            st.image(image3, caption="Property View 3", use_column_width=True)
    
        st.markdown("""
        <h4>Investment Strategy</h4>
        • Focus on up-and-coming neighborhoods with growth potential<br>
        • Target properties with value-add opportunities through renovation<br>
        • Aim to build a diverse portfolio of residential and potentially commercial properties
        """, unsafe_allow_html=True)

        st.write(" ")
    
        st.markdown("""
        <h4>Future Plans</h4>
        • Research multi-family properties in emerging markets<br>
        • Network with local real estate investors and join investment groups<br>
        • Continuously educate myself on real estate market trends and investment strategies
        """, unsafe_allow_html=True)
    
        st.info("My goal is to build a robust real estate portfolio that generates passive income and appreciates in value over time. I'm committed to learning and growing as a real estate investor.")

    st.markdown("---")
    st.write("© 2024 Caleb Traxler. All rights reserved.")


if __name__ == "__main__":
    main()
