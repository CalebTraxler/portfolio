#cd Portfolio

#streamlit run Portfolio.py

import streamlit as st
from PIL import Image
import base64
import os

def set_custom_style():
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            border-radius: 0.5rem;
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #0066CC;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
        h1, h2, h3 {
            color: #0066CC;
        }
        .highlight {
            background-color: #e9ecef;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            border-left: 4px solid #0066CC;
        }
        .publication-item {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #dee2e6;
        }
        .skill-category {
            background-color: #e3f2fd;
            padding: 0.75rem;
            border-radius: 0.3rem;
            margin-bottom: 0.75rem;
        }
        .metric-container {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            border: 1px solid #dee2e6;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Caleb Traxler's Portfolio", layout="wide", page_icon="🎓")
    set_custom_style()
    
    # Header Section
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            image = Image.open("output.png")
            st.image(image, width=275)
        except:
            st.info("Profile image not found. Please add 'output.png' to display your photo.")
    
    with col2:
        st.title("Caleb Traxler")
        st.subheader("Data Scientist | ML Engineer | Researcher | Entrepreneur | Investor")
        
        st.markdown("""
        **Contact Information:**
        - Email: [calebtraxler34@gmail.com](mailto:calebtraxler34@gmail.com)
        - Phone: (805) 377-8182
        - Academic: traxlerc@uci.edu
        
        **Professional Links:**
        - [LinkedIn](https://www.linkedin.com/in/calebtraxler) 
        - [GitHub](https://www.github.com/calebtraxler) 
        - [Traxler Technology](https://traxlertechnology.vercel.app)
        """)
    
    st.markdown("---")
    
    # Professional Summary
    with st.container():
        st.markdown("""
        <div class="highlight">
        <h3>Professional Summary</h3>
        <p>Data Science graduate student specializing in Machine Learning, Data Science and Computer Vision. Published 
        academic researcher with significant entrepreneurial experience developing scalable Artificial Intelligence systems. 
        Actively seeking PhD opportunities in computer science (start date: September 2026) and job opportunities in 
        the data science and machine learning space (start date: December 2025).</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Custom CSS for tabs
    st.markdown("""
    <style>
        .stTabs {
            background-color: #f0f2f6;
            padding: 6px 0px;
            border-radius: 6px;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            justify-content: space-evenly;
            flex-wrap: wrap;
        }
        .stTabs [data-baseweb="tab"] {
            height: auto;
            min-height: 40px;
            white-space: normal;
            background-color: transparent;
            border-radius: 8px;
            color: #31333F;
            font-size: 14px;
            font-weight: 600;
            align-items: center;
            justify-content: center;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            padding: 8px 12px;
            text-align: center;
        }
        .stTabs [aria-selected="true"] {
            background-color: #0066CC;
            color: white;
            border-color: #0066CC;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(0, 102, 204, 0.1);
            border-color: #0066CC;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "About Me", "Education", "Research", "Experience", "Projects", "Publications", "Investments"
    ])
    
    with tab1:
        st.header("About Me")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("""
            I'm Caleb Traxler, a passionate Data Science graduate student at UC Irvine with a strong 
            foundation in Machine Learning, Computer Vision, and AI research. As a published researcher and 
            entrepreneur, I'm dedicated to advancing the field of artificial intelligence and its applications.

            **Current Focus:**
            - Pursuing M.S. in Data Science at UC Irvine (GPA: 3.97)
            - Conducting cutting-edge research in variational inference and geospatial analysis
            - Leading Traxler Technology LLC, building multimodal AI systems
            - Active investor in real estate and securities markets

            **Career Goals:**
            - Seeking PhD opportunities in Computer Science (September 2026)
            - Open to data science and ML engineering roles (December 2025)

            **Personal Interests:**
            - Surfing and weight training
            - Traveling and exploring new cultures
            - Visiting amusement parks
            - Discovering amazing cuisines
            - Building full-stack applications
            - Exploring new ML architectures and contributing to open-source projects
            """)
        
        with col2:
            st.markdown("### Quick Stats")
            st.metric("Current GPA", "3.97", "UC Irvine")
            st.metric("Publications", "2", "arXiv papers")
            st.metric("GitHub Projects", "15+", "Public repos")
            st.metric("Research Areas", "3", "Active projects")
        
        # Download Resume Button
        st.markdown("### Download Resume")
        if st.button("Download Latest Resume", type="primary"):
            try:
                file_path = "ResumeFinalpro.docx (8).pdf"
                with open(file_path, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                
                st.download_button(
                    label="Click here to download",
                    data=PDFbyte,
                    file_name="CalebTraxler_Resume.pdf",
                    mime="application/pdf"
                )
            except FileNotFoundError:
                st.error("Resume file not found. Please check the file path.")
        
        # Personal photos section
        st.markdown("### Personal Interests")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Travel Adventures")
            try:
                st.image("travel/japan.png", caption="Exploring Japan", use_column_width=True)
                st.image("travel/japan2.png", caption="Cultural experiences", use_column_width=True)
            except:
                st.info("Travel photos coming soon!")
        
        with col2:
            st.subheader("Theme Parks")
            try:
                st.image("parks/universal.png", caption="Universal Studios", use_column_width=True)
                st.image("parks/stormtroopers.png", caption="Disneyland adventures", use_column_width=True)
            except:
                st.info("Theme park photos coming soon!")
        
        with col3:
            st.subheader("Culinary Experiences")
            try:
                st.image("food/crab.png", caption="Santa Barbara pier dining", use_column_width=True)
                st.image("food/omlet.png", caption="Tamagoyaki in Japan", use_column_width=True)
            except:
                st.info("Food photos coming soon!")
    
    with tab2:
        st.header("Education")
        
        # UC Irvine
        with st.expander("M.S. Data Science - UC Irvine (Current)", expanded=True):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Education/uci_image.png", width=100)
                except:
                    st.write("UC Irvine")
            with col2:
                st.subheader("University of California, Irvine")
                st.write("**Master of Science in Data Science** | GPA: 3.97")
                st.write("September 2024 - December 2025")
            
            st.markdown("""
            **Specializations:**
            - Artificial Intelligence
            - Generative Models  
            - Computer Vision
            - Geographic Information Systems (GIS)
            - Big Data Analytics
            
            **Key Achievements:**
            - UCI Master of Data Science Scholarship Recipient
            - Accelerated 15-month program
            - Maintaining 3.97 GPA
            """)
        
        # UCLA
        with st.expander("B.S. Mathematics & Computer Science - UCLA"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Education/ucla_image.png", width=100)
                except:
                    st.write("UCLA")
            with col2:
                st.subheader("University of California, Los Angeles")
                st.write("**Bachelor of Science in Mathematics & Computer Science** | GPA: 3.81")
                st.write("September 2022 - June 2024")
            
            st.markdown("""
            **Honors & Activities:**
            - Phi Theta Kappa Honors Society
            - AI Safety Fellowship
            - Undergraduate Mathematics Student Association (UMSA)
            - Undergraduate Mathematics Research (Prof. Shbia Biswal)
            
            **Concentrations:**
            - Applied Mathematics
            - Computer Science
            """)
        
        # Moorpark College
        with st.expander("A.S. Multiple Disciplines - Moorpark College"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Education/mpc_image.png", width=100)
                except:
                    st.write("Moorpark College")
            with col2:
                st.subheader("Moorpark College")
                st.write("**Associate of Science in Mathematics, Physics & Computer Science** | GPA: 4.00")
                st.write("August 2020 - June 2022")
            
            st.markdown("""
            **Achievements:**
            - Dean's List (2020-2022)
            - Honor Roll (2020-2022)
            - Phi Theta Kappa Honors Society
            - NASA Community College Aerospace Scholars Internship
            - Mathematics Tutor
            """)
    
    with tab3:
        st.header("Research Experience")
        
        # Current Research Positions
        st.subheader("Current Research Positions")
        
        with st.expander("Variational Inference Research - UC Irvine (Prof. Erik Sudderth)", expanded=True):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("**Research Focus**")
            with col2:
                st.write("**Graduate Research Assistant**")
                st.write("June 2025 - Present | Irvine, CA")
            
            st.markdown("""
            **Research Focus:**
            - Variational inference with Gauss-Markov distributions
            - Applying methods to Stochastic Differential Equation (SDE) time series models
            - Future project involving chemical data analysis
            - Advanced probabilistic modeling and inference techniques
            """)
        
        with st.expander("Geospatial Climate Research - UC Irvine (Prof. Jun Wu)"):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("**Satellite Data**")
            with col2:
                st.write("**Graduate Research Assistant**")
                st.write("June 2025 - Present | Irvine, CA")
            
            st.markdown("""
            **Research Focus:**
            - ECOSTRESS satellite data analysis
            - Extreme heat distribution mapping across California urban zones
            - Spatial data handling and GIS analysis
            - Python-based geospatial analysis and visualization
            """)
        
        # Previous Research
        st.subheader("Previous Research")
        
        with st.expander("COVID-19 Mathematical Modeling - UCLA (Prof. Shbia Biswal)"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Experience/ucla_math.png", width=80)
                except:
                    st.write("**Research**")
            with col2:
                st.write("**Undergraduate Researcher**")
                st.write("March 2023 - June 2023 | Los Angeles, CA")
            
            st.markdown("""
            **Research Achievements:**
            - Modeled COVID-19 dynamics using extended SIR/SEIR models
            - Analyzed Orange County COVID-19 data using Python and Jupyter notebooks
            - Developed innovative bifurcation diagrams for predictive modeling
            - **Published in arXiv**: [Analysis of COVID-19 Infection Dynamics](https://arxiv.org/abs/2505.13753)
            - Identified critical transcritical bifurcation thresholds for predictions
            """)
    
    with tab4:
        st.header("Professional Experience")
        
        # Current Positions
        with st.expander("Founder & CEO - Traxler Technology LLC", expanded=True):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Experience/the_x.png", width=100)
                except:
                    st.write("**CEO**")
            with col2:
                st.write("**Founder & CEO**")
                st.write("November 2024 - Present | Los Angeles, CA")
            
            st.markdown("""
            **Company Overview:**
            - AI-focused startup building multimodal intelligence systems
            - [Visit Traxler Technology](https://traxlertechnology.vercel.app/login)
            
            **Key Achievements:**
            - Designed and deployed scalable full-stack platforms
            - Tech Stack: React, Firebase, AWS EC2, Vercel, Auth0
            - Developing cross-platform mobile applications
            - Focus on vision-language models and AI-driven insights
            """)
        
        with st.expander("Program Ambassador - UC Irvine"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Education/uci_image.png", width=80)
                except:
                    st.write("**Ambassador**")
            with col2:
                st.write("**Master of Data Science Program Ambassador**")
                st.write("September 2024 - Present | Irvine, CA")
            
            st.markdown("""
            **Responsibilities:**
            - Ambassador for Masters of Data Science program (2024-2025 cohort)
            - Support creation and development of marketing campaigns
            - Student outreach and program promotion
            - [UCI Faculty Profile](https://ics.uci.edu/?people=caleb-traxler)
            """)
        
        # Previous Experience
        with st.expander("Data Scientist & ML Engineer Intern - Amgen"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Experience/amgen_img.png", width=120)
                except:
                    st.write("**Amgen**")
            with col2:
                st.write("**Data Scientist & ML Engineer Intern**")
                st.write("July 2024 - September 2024 | Remote")
            
            st.markdown("""
            **Key Achievements:**
            - Built rare disease prioritization model using generative AI
            - Reduced year-long process to minutes using GenAI pipeline
            - Developed Streamlit application for stakeholder data visualization
            - **Winner: Amgen AI Symposium 2024**
            - 96% accuracy in disease scoring automation
            """)
        
        with st.expander("AI Safety Fellowship - UCLA"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Experience/ai_safety.png", width=75)
                except:
                    st.write("**AI Safety**")
            with col2:
                st.write("**AI Safety Fellow**")
                st.write("January 2024 - March 2024 | Los Angeles, CA")
            
            st.markdown("""
            **Program Focus:**
            - Developed practical ML skills using PyTorch and micrograd
            - Explored AI safety and alignment challenges
            - Studied AI existential risks and impacts on humanity's future
            - Contributed to understanding AI system failure modes
            """)
        
        with st.expander("Engineering & Design Intern - NASA"):
            col1, col2 = st.columns([1, 4])
            with col1:
                try:
                    st.image("Experience/nasa.png", width=80)
                except:
                    st.write("**NASA**")
            with col2:
                st.write("**Engineering & Design Intern**")
                st.write("February 2022 - August 2022 | Remote")
            
            st.markdown("""
            **Project Achievements:**
            - Mars rover capstone project collaboration
            - Designed modern Mars rover blueprint with ML/AI systems
            - Built project hardware and software components
            - Enhanced NASA Mars rover functionality and adaptability
            - NASA Community College Aerospace Scholars Program
            """)
    
    with tab5:
        st.header("Technical Projects")
        
        # Featured Projects
        st.subheader("Featured Projects")
        
        with st.expander("AI Life Journal using VLMs and LangChain Memory", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown("""
                **Project Overview:**
                Cross-platform mobile application (Android & iOS) enabling users to capture, organize, and 
                reflect on daily experiences using Meta Ray-Ban AI glasses and other life-logging devices.
                
                **Technical Stack:**
                - Vision-Language Models (VLMs)
                - LangChain for memory-augmented AI
                - Cross-platform mobile development
                - Secure cloud storage and processing
                
                **Key Features:**
                - Media ingestion from wearable devices
                - AI-driven insights and summaries
                - Intelligent journaling features
                - End-to-end secure architecture
                """)
            with col2:
                st.markdown("**Status:** Active")
                st.markdown("**Period:** June 2025 - Present")
                st.markdown("[GitHub Repository](https://github.com/CalebTraxler/TraxlerTechnologyApp_)")
        
        with st.expander("Generative Route Prediction with HMMs and 3D Point Clouds"):
            st.markdown("""
            **Project Overview:**
            Developed discrete Hidden Markov Models (HMMs) to generate realistic driving routes from 
            KITTI-360 3D point cloud maps.
            
            **Technical Achievements:**
            - Advanced probabilistic modeling with HMMs
            - 3D point cloud data processing
            - Realistic driving route generation
            - Currently under review for publication
            
            **Timeline:** May 2025 - June 2025 | [GitHub Repository](https://github.com/CalebTraxler/HMM-3D-Routing)
            """)
        
        with st.expander("Multivariate Statistical Analysis of Exoplanet Habitability"):
            st.markdown("""
            **Project Overview:**
            Comprehensive analysis of 517 exoplanets from NASA Exoplanet Archive to identify potentially 
            habitable worlds and quantify detection bias.
            
            **Key Features:**
            - Multivariate statistical analysis
            - Habitability assessment algorithms
            - Interactive 3D visualization using Streamlit and PyDeck
            - **Published in arXiv**
            
            **Links:**
            - [Live Application](https://planet-habitability.streamlit.app/)
            - [arXiv Paper](https://arxiv.org/abs/2506.18200)
            
            **Timeline:** May 2025 - June 2025
            """)
        
        # Additional Projects
        st.subheader("Additional Projects")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.markdown("""
                **Autonomous Driving via CNN and Groq API**
                - Real-time lane detection using U-Net CNN
                - >95% accuracy, <50ms latency
                - Under review for publication
                - [GitHub Repository](https://github.com/CalebTraxler/Autonomous_Driving_CV)
                
                **Real Estate ROI Geo-Locator**
                - Interactive 3D visualization with Streamlit
                - Real-time ROI trend analysis
                - [Live Application](https://lnkd.in/g_NrKj-b)
                """)
        
        with col2:
            with st.container():
                st.markdown("""
                **Neural Network Classification**
                - Two-layer network for binary classification
                - 97.24% validation accuracy on MNIST
                - Implemented forward/backward propagation
                
                **K-means Clustering on CIFAR-10**
                - Applied to 60K labeled images
                - PCA dimensionality reduction
                - K=10 clustering with ground truth analysis
                """)
        
        # Legacy Projects
        with st.expander("Academic & Legacy Projects"):
            st.markdown("""
            **Bayesian Network and Causal Modeling**
            - Probabilistic reasoning system
            - SamIam inference tool implementation
            - What-if scenario analysis
            
            **Sokoban Game with Admissible Heuristic**
            - A* algorithm implementation
            - Solved 19 games under 4 seconds
            - Manhattan distance optimization
            
            **Mathematical Imaging Projects**
            - Histogram equalization for MRI enhancement
            - Image sharpening using Laplacian masks
            - Feature extraction via brightness adjustments
            """)
    
    with tab6:
        st.header("Publications")
        
        st.markdown("""
        <div style="background-color: #f0f8ff; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
        <h4>Publication Metrics</h4>
        <div style="display: flex; gap: 2rem;">
            <div><strong>Total Papers:</strong> 2</div>
            <div><strong>Platform:</strong> arXiv</div>
            <div><strong>Research Areas:</strong> AI, Statistics, Epidemiology</div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Publication 1
        with st.container():
            st.markdown("""
            <div class="publication-item">
            <h4>Multivariate Statistical Analysis of Exoplanet Habitability: Detection Bias and Earth Analog Identification</h4>
            <p><strong>Authors:</strong> <strong>Traxler, C.</strong>, et al.</p>
            <p><strong>Published:</strong> 2025 | <strong>arXiv:</strong> 2506.18200</p>
            <p><strong>Abstract:</strong> Comprehensive multivariate statistical analysis of 517 exoplanets from the NASA Exoplanet Archive to identify potentially habitable worlds and quantify detection bias in current surveys.</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.link_button("Read Paper", "https://arxiv.org/abs/2506.18200")
            with col2:
                st.link_button("Live Demo", "https://planet-habitability.streamlit.app/")
            with col3:
                st.link_button("GitHub", "https://github.com/CalebTraxler")
        
        # Publication 2  
        with st.container():
            st.markdown("""
            <div class="publication-item">
            <h4>Analysis of COVID-19 Infection Dynamics: Extended SIR Model Approach</h4>
            <p><strong>Authors:</strong> <strong>Traxler, C.</strong>, et al.</p>
            <p><strong>Published:</strong> 2025 | <strong>arXiv:</strong> 2505.13754</p>
            <p><strong>Abstract:</strong> Advanced mathematical modeling of COVID-19 dynamics using extended SIR/SEIR models with bifurcation analysis for predictive modeling of pandemic spread patterns.</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("Read Paper", "https://arxiv.org/abs/2505.13753")
            with col2:
                st.link_button("Research Details", "https://github.com/CalebTraxler")
        
        # Research Impact
        st.markdown("### Research Impact")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Citation Potential", "High", "Emerging research")
        with col2:
            st.metric("Research Areas", "3", "AI, Stats, Health")
        with col3:
            st.metric("Collaboration", "Multi-author", "Team research")
        
        # Future Publications
        st.markdown("### Upcoming Publications")
        st.info("""
        **In Review:**
        - Generative Route Prediction with HMMs and 3D Point Clouds
        - Autonomous Driving via CNN and Real-time Analysis
        
        **In Progress:**
        - Variational Inference Applications in Chemical Data Analysis
        - Geospatial Analysis of Urban Heat Islands using ECOSTRESS Data
        """)
    
    with tab7:
        st.header("Investment Portfolio")
        
        # Investment Philosophy
        st.markdown("""
        <div class="highlight">
        <h3>Investment Philosophy</h3>
        <p>Active investor in real estate and public markets with a focus on long-term value creation, 
        financial modeling, and portfolio diversification. Passionate about identifying emerging market 
        opportunities and applying data-driven analysis to investment decisions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Real Estate Portfolio
        st.subheader("Real Estate Investments")
        
        with st.expander("First Property Investment - Topeka, Kansas", expanded=True):
            st.markdown("""
            **Investment Details:**
            - **Achievement:** Purchased first property at age 22
            - **Location:** Topeka, Kansas
            - **Status:** Currently under renovation
            - **Strategy:** Fix, refinance, rent (BRRRR method)
            - **Goal:** Generate passive income and build equity
            """)
            
            # Property Images
            try:
                col1, col2, col3 = st.columns(3)
                with col1:
                    image1 = Image.open("Investments/1.jpg")
                    st.image(image1, caption="Property Exterior", use_column_width=True)
                with col2:
                    image2 = Image.open("Investments/2.png")
                    st.image(image2, caption="Interior View", use_column_width=True)
                with col3:
                    image3 = Image.open("Investments/3.png")
                    st.image(image3, caption="Renovation Progress", use_column_width=True)
            except:
                st.info("Property photos will be displayed here once available.")
        
        # Investment Strategy
        st.subheader("Investment Strategy")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Real Estate Focus:**
            - Target emerging neighborhoods with growth potential
            - Value-add opportunities through strategic renovation
            - Geographic diversification (Midwest expansion)
            - Focus on cash flow and appreciation
            - Building relationships with local investors
            """)
        
        with col2:
            st.markdown("""
            **Investment Principles:**
            - Data-driven market analysis
            - Long-term value creation
            - Risk management and diversification
            - Continuous market education
            - Leveraging technology for analysis
            """)
        
        # Future Investment Plans
        st.subheader("Future Investment Plans")
        
        with st.container():
            st.markdown("""
            **2025 Goals:**
            - Acquire second property in Texas by end of 2025
            - Research multi-family investment opportunities
            - Develop automated investment analysis tools
            - Join local real estate investment groups
            - Complete real estate education programs
            
            **Long-term Vision:**
            - Build diverse portfolio of residential properties
            - Explore commercial real estate opportunities  
            - Potential real estate syndication participation
            - Geographic expansion to high-growth markets
            - Integration of AI/ML in property analysis
            """)
        
        # Investment Performance Tracking
        st.subheader("Portfolio Tracking")
        
        # Create sample metrics (you can replace with real data)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Properties Owned", "1", "First acquisition")
        with col2:
            st.metric("Target ROI", "15%+", "Annual target")
        with col3:
            st.metric("Investment Timeline", "Long-term", "10+ years")
        with col4:
            st.metric("Next Purchase", "Q4 2025", "Texas market")
        
        # Investment Education
        st.markdown("### Continuous Learning")
        st.info("""
        **Investment Education Focus:**
        - Real estate market analysis and trends
        - Financial modeling and cash flow analysis
        - Tax strategies and legal structures
        - Networking with experienced investors
        - Technology tools for property evaluation
        """)
    
    # Technical Skills Section
    st.markdown("---")
    st.header("Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="skill-category">
        <h4>Languages & Cloud Platforms</h4>
        <p>Python • R • JavaScript (React) • SQL • MATLAB • Bash<br>
        AWS (EC2, S3) • Firebase • Vercel • Docker • Git/GitHub</p>
        </div>
        
        <div class="skill-category">
        <h4>Machine Learning & AI</h4>
        <p>Deep Learning • Generative AI • Vision-Language Models (VLMs)<br>
        Transformers • NLP • Reinforcement Learning • HMMs<br>
        Variational Inference • Bayesian Networks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="skill-category">
        <h4>Frameworks & Libraries</h4>
        <p>NumPy • Pandas • Scikit-learn • TensorFlow • PyTorch<br>
        Keras • OpenCV • Hugging Face • LangChain • Plotly</p>
        </div>
        
        <div class="skill-category">
        <h4>Development Tools</h4>
        <p>Jupyter • VSCode • REST APIs • Linux CLI<br>
        CI/CD (GitHub Actions) • Auth0 • Streamlit</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2025 Caleb Traxler. All rights reserved.</p>
        <p>Built with Streamlit • Last updated: January 2025</p>
        <p>
            <a href="mailto:calebtraxler34@gmail.com">Email</a> • 
            <a href="https://www.linkedin.com/in/calebtraxler">LinkedIn</a> • 
            <a href="https://github.com/calebtraxler">GitHub</a> • 
            <a href="https://traxlertechnology.vercel.app">Company</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
