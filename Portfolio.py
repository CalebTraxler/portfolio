#cd Portfolio

#streamlit run Portfolio.py

import streamlit as st
from PIL import Image
import base64
import os

def set_custom_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .main {
            padding: 0.5rem 2rem;
            font-family: 'Inter', sans-serif;
        }
        
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
            border-radius: 8px;
            border: none;
            padding: 0.5rem 1.5rem;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        }
        
        h1 {
            color: #2D3748;
            font-weight: 700;
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        
        h2 {
            color: #4A5568;
            font-weight: 600;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
            margin: 2rem 0 1rem 0;
        }
        
        h3 {
            color: #2D3748;
            font-weight: 600;
        }
        
        .header-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 1rem;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        }
        
        .summary-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 0.5rem 0;
            box-shadow: 0 4px 16px rgba(240, 147, 251, 0.3);
        }
        
        .education-card {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 4px 16px rgba(79, 172, 254, 0.3);
        }
        
        .experience-card {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 4px 16px rgba(67, 233, 123, 0.3);
        }
        
        .project-card {
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 4px 16px rgba(250, 112, 154, 0.3);
        }
        
        .publication-card {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            color: #2D3748;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 4px 16px rgba(168, 237, 234, 0.3);
        }
        
        .investment-card {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            color: #2D3748;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 4px 16px rgba(255, 236, 210, 0.3);
        }
        
        .skill-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            text-align: center;
        }
        
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            border-left: 4px solid #667eea;
        }
        
        .info-box {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            margin: 1rem 0;
        }
        
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .contact-item {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .contact-item:hover {
            transform: translateY(-3px);
        }
        
        .section-divider {
            height: 3px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 2px;
            margin: 2rem 0;
        }
        
        .tab-content {
            padding: 1.5rem 0;
            min-height: 400px;
        }
        
        .achievement-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 25px;
            font-size: 0.85rem;
            font-weight: 500;
            margin: 0.3rem 0.2rem;
            display: inline-block;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Caleb Traxler - Portfolio", 
        layout="wide", 
        page_icon="🎓",
        initial_sidebar_state="collapsed"
    )
    set_custom_style()
    
    # Header Section with gradient background
    st.markdown("""
    <div class="header-card">
        <h1 style="color: white; margin-bottom: 0.5rem;">Caleb Traxler</h1>
        <h3 style="color: rgba(255,255,255,0.9); font-weight: 400; margin-bottom: 1.5rem;">
            Data Scientist | ML Engineer | Researcher | Entrepreneur | Investor
        </h3>
        <div class="contact-grid">
            <div class="contact-item">
                <strong>📧 Email</strong><br>
                <a href="mailto:calebtraxler34@gmail.com" style="color: #667eea;">calebtraxler34@gmail.com</a>
            </div>
            <div class="contact-item">
                <strong>📞 Phone</strong><br>
                <span style="color: #2D3748;">(805) 377-8182</span>
            </div>
            <div class="contact-item">
                <strong>🎓 Academic</strong><br>
                <a href="mailto:traxlerc@uci.edu" style="color: #667eea;">traxlerc@uci.edu</a>
            </div>
            <div class="contact-item">
                <strong>💼 LinkedIn</strong><br>
                <a href="https://www.linkedin.com/in/calebtraxler" style="color: #667eea;">LinkedIn Profile</a>
            </div>
            <div class="contact-item">
                <strong>💻 GitHub</strong><br>
                <a href="https://www.github.com/calebtraxler" style="color: #667eea;">GitHub Profile</a>
            </div>
            <div class="contact-item">
                <strong>🌐 Company</strong><br>
                <a href="https://traxlertechnology.vercel.app" style="color: #667eea;">Traxler Technology</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Summary with gradient card
    st.markdown("""
    <div class="summary-card">
        <h3 style="color: white; margin-bottom: 1rem;">🎯 Professional Summary</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Data Science graduate student specializing in Machine Learning, Data Science and Computer Vision. 
            Published academic researcher with significant entrepreneurial experience developing scalable 
            Artificial Intelligence systems. Actively seeking PhD opportunities in computer science 
            (start date: September 2026) and job opportunities in the data science and machine learning 
            space (start date: December 2025).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats Section
    st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin: 0; font-size: 2rem;">3.97</h3>
            <p style="margin: 0.5rem 0 0 0; color: #4A5568; font-weight: 500;">Current GPA</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin: 0; font-size: 2rem;">2</h3>
            <p style="margin: 0.5rem 0 0 0; color: #4A5568; font-weight: 500;">Publications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin: 0; font-size: 2rem;">15+</h3>
            <p style="margin: 0.5rem 0 0 0; color: #4A5568; font-weight: 500;">GitHub Projects</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin: 0; font-size: 2rem;">3</h3>
            <p style="margin: 0.5rem 0 0 0; color: #4A5568; font-weight: 500;">Research Areas</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Custom CSS for enhanced tabs
    st.markdown("""
    <style>
        .stTabs {
            background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
            padding: 0.75rem;
            border-radius: 15px;
            margin: 1rem 0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.75rem;
            justify-content: space-evenly;
            flex-wrap: wrap;
            padding: 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            background: white;
            border-radius: 10px;
            color: #4A5568;
            font-size: 14px;
            font-weight: 600;
            padding: 12px 20px;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
        }
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
    </style>
    """, unsafe_allow_html=True)

    # Create enhanced tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "About Me", "Education", "Research", "Experience", "Projects", "Publications", "Investments"
    ])
    
    with tab1:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## About Me
            
            I'm Caleb Traxler, a passionate Data Science graduate student at UC Irvine with a strong 
            foundation in Machine Learning, Computer Vision, and AI research. As a published researcher and 
            entrepreneur, I'm dedicated to advancing the field of artificial intelligence and its applications.
            """)
            
            st.markdown("""
            <div class="info-box">
                <h4>🎯 Current Focus</h4>
                <ul>
                    <li>Pursuing M.S. in Data Science at UC Irvine (GPA: 3.97)</li>
                    <li>Conducting research in variational inference and geospatial analysis</li>
                    <li>Leading Traxler Technology LLC, building multimodal AI systems</li>
                    <li>Active investor in real estate and securities markets</li>
                    <li>Published academic researcher with 2 arXiv publications</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-box">
                <h4>🚀 Career Goals</h4>
                <ul>
                    <li>Seeking PhD opportunities in Computer Science (September 2026)</li>
                    <li>Open to data science and ML engineering roles (December 2025)</li>
                    <li>Advancing Mars exploration and space technology applications</li>
                    <li>Contributing to AI safety and alignment research</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-box">
                <h4>🔬 Research Interests</h4>
                <ul>
                    <li>Variational inference and probabilistic modeling</li>
                    <li>Computer vision and vision-language models</li>
                    <li>Geospatial analysis and climate data</li>
                    <li>Augmented reality and wearable computing</li>
                    <li>Human cognition and AI intersection</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            try:
                image = Image.open("output.png")
                st.image(image, width=275, caption="Caleb Traxler")
            except:
                st.info("Profile image will appear here")
            
            # Download Resume Button
            if st.button("📄 Download Latest Resume", type="primary"):
                try:
                    file_path = "ResumeFinalpro.docx (8).pdf"
                    with open(file_path, "rb") as pdf_file:
                        PDFbyte = pdf_file.read()
                    
                    st.download_button(
                        label="📄 Click here to download",
                        data=PDFbyte,
                        file_name="CalebTraxler_Resume.pdf",
                        mime="application/pdf"
                    )
                except FileNotFoundError:
                    st.error("Resume file not found. Please check the file path.")
        
        # Personal Interests Section
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        st.markdown("## Personal Interests")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h4>✈️ Travel Adventures</h4>
                <p>Exploring different cultures and cuisines around the world</p>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.image("travel/japan.png", caption="Exploring Japan", use_container_width=True)
            except:
                st.info("Travel photos coming soon!")
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h4>🎢 Theme Parks</h4>
                <p>Enjoying thrilling rides and magical experiences</p>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.image("parks/universal.png", caption="Universal Studios", use_container_width=True)
            except:
                st.info("Theme park photos coming soon!")
        
        with col3:
            st.markdown("""
            <div class="info-box">
                <h4>🏄‍♂️ Active Lifestyle</h4>
                <p>Surfing, weight training, and outdoor adventures. Passionate about maintaining physical fitness and exploring nature.</p>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.image("food/crab.png", caption="Santa Barbara dining", use_container_width=True)
            except:
                st.info("Lifestyle photos coming soon!")
        
        # Additional interests
        st.markdown("### Professional Interests")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h4>💻 Technical Pursuits</h4>
                <ul>
                    <li>Programming full-stack applications</li>
                    <li>Exploring new machine learning architectures</li>
                    <li>Contributing to open-source projects</li>
                    <li>Building innovative AI solutions</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h4>📊 Investment & Finance</h4>
                <ul>
                    <li>Financial modeling and portfolio strategy</li>
                    <li>Real estate market analysis</li>
                    <li>Data-driven investment decisions</li>
                    <li>Long-term wealth building strategies</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown("## Education")
        
        # UC Irvine
        st.markdown("""
        <div class="education-card">
            <h3 style="color: white;">🎓 Master of Science in Data Science</h3>
            <h4 style="color: rgba(255,255,255,0.9);">University of California, Irvine</h4>
            <p><strong>GPA: 3.97</strong> | September 2024 - December 2025</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                st.image("Education/uci_image.png", width=120)
            except:
                st.write("UC Irvine Logo")
        
        with col2:
            st.markdown("**Specializations:**")
            specializations = ["Artificial Intelligence", "Generative Models", "Computer Vision", "Geographic Information Systems", "Big Data Analytics"]
            for spec in specializations:
                st.markdown(f'<span class="achievement-badge">{spec}</span>', unsafe_allow_html=True)
            
            st.markdown("**Achievements:**")
            achievements = ["UCI Scholarship Recipient", "3.97 GPA", "15-month Accelerated Program"]
            for achievement in achievements:
                st.markdown(f'<span class="achievement-badge">{achievement}</span>', unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # UCLA
        st.markdown("""
        <div class="education-card">
            <h3 style="color: white;">🎓 Bachelor of Science in Mathematics & Computer Science</h3>
            <h4 style="color: rgba(255,255,255,0.9);">University of California, Los Angeles</h4>
            <p><strong>GPA: 3.81</strong> | September 2022 - June 2024</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                st.image("Education/ucla_image.png", width=120)
            except:
                st.write("UCLA Logo")
        
        with col2:
            ucla_honors = ["Phi Theta Kappa", "AI Safety Fellowship", "UMSA Member", "Undergraduate Research"]
            for honor in ucla_honors:
                st.markdown(f'<span class="achievement-badge">{honor}</span>', unsafe_allow_html=True)
        
        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
        
        # Moorpark College
        st.markdown("""
        <div class="education-card">
            <h3 style="color: white;">🎓 Associate of Science in Mathematics, Physics & Computer Science</h3>
            <h4 style="color: rgba(255,255,255,0.9);">Moorpark College</h4>
            <p><strong>GPA: 4.00</strong> | August 2020 - June 2022</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 3])
        with col1:
            try:
                st.image("Education/mpc_image.png", width=120)
            except:
                st.write("Moorpark College Logo")
        
        with col2:
            moorpark_achievements = ["Dean's List (2020-2022)", "Honor Roll (2020-2022)", "Phi Theta Kappa", "NASA Aerospace Scholars", "Mathematics Tutor"]
            for achievement in moorpark_achievements:
                st.markdown(f'<span class="achievement-badge">{achievement}</span>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown("## Research Experience")
        
        st.markdown("### Current Research Positions")
        
        # Research Position 1
        st.markdown("""
        <div class="experience-card">
            <h4 style="color: white;">🧠 Variational Inference Research</h4>
            <p style="color: rgba(255,255,255,0.9);"><strong>Graduate Research Assistant</strong> | Prof. Erik Sudderth</p>
            <p style="color: rgba(255,255,255,0.8);">June 2025 - Present | UC Irvine</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Research Focus:</strong>
            <ul>
                <li>Variational inference with Gauss-Markov distributions</li>
                <li>SDE time series models application</li>
                <li>Chemical data analysis projects</li>
                <li>Advanced probabilistic modeling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Research Position 2
        st.markdown("""
        <div class="experience-card">
            <h4 style="color: white;">🌡️ Geospatial Climate Research</h4>
            <p style="color: rgba(255,255,255,0.9);"><strong>Graduate Research Assistant</strong> | Prof. Jun Wu</p>
            <p style="color: rgba(255,255,255,0.8);">June 2025 - Present | UC Irvine</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Research Focus:</strong>
            <ul>
                <li>ECOSTRESS satellite data analysis</li>
                <li>Urban heat distribution mapping in California</li>
                <li>Python-based geospatial analysis</li>
                <li>GIS and spatial data visualization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Previous Research")
        
        # Previous Research
        st.markdown("""
        <div class="publication-card">
            <h4>🦠 COVID-19 Mathematical Modeling</h4>
            <p><strong>Undergraduate Researcher</strong> | Prof. Shbia Biswal</p>
            <p>March 2023 - June 2023 | UCLA Mathematics</p>
            <p><strong>Published:</strong> <a href="https://arxiv.org/abs/2505.13753">arXiv:2505.13753</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown("## Professional Experience")
        
        # Current CEO Position
        st.markdown("""
        <div class="experience-card">
            <h3 style="color: white;">🚀 Founder & CEO - Traxler Technology LLC</h3>
            <p style="color: rgba(255,255,255,0.9);">November 2024 - Present | Los Angeles, CA</p>
            <p style="color: rgba(255,255,255,0.8);"><a href="https://traxlertechnology.vercel.app/login" style="color: rgba(255,255,255,0.9);">Visit Company Website</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Key Achievements:</strong>
            <ul>
                <li>Building multimodal intelligence systems</li>
                <li>Full-stack platform development (React, Firebase, AWS EC2)</li>
                <li>Cross-platform mobile applications</li>
                <li>Vision-language models integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Amgen Internship
        st.markdown("""
        <div class="experience-card">
            <h3 style="color: white;">🧬 Data Scientist & ML Engineer - Amgen</h3>
            <p style="color: rgba(255,255,255,0.9);">July 2024 - September 2024 | Remote</p>
            <p style="color: rgba(255,255,255,0.8);"><strong>Winner: Amgen AI Symposium 2024</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Major Accomplishments:</strong>
            <ul>
                <li>96% accuracy in rare disease prioritization using GenAI</li>
                <li>Reduced year-long process to minutes</li>
                <li>Built Streamlit data visualization applications</li>
                <li>Won company-wide AI Symposium competition</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Program Ambassador
        st.markdown("""
        <div class="experience-card">
            <h3 style="color: white;">🎓 Program Ambassador - UC Irvine</h3>
            <p style="color: rgba(255,255,255,0.9);">September 2024 - Present | Irvine, CA</p>
            <p style="color: rgba(255,255,255,0.8);"><a href="https://ics.uci.edu/?people=caleb-traxler" style="color: rgba(255,255,255,0.9);">UCI Faculty Profile</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Responsibilities:</strong>
            <ul>
                <li>Ambassador for Masters of Data Science program (2024-2025 cohort)</li>
                <li>Support creation and development of marketing campaigns</li>
                <li>Student outreach and program promotion</li>
                <li>Represent program at university events and initiatives</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Safety Fellowship
        st.markdown("""
        <div class="experience-card">
            <h3 style="color: white;">🛡️ AI Safety Fellowship - UCLA</h3>
            <p style="color: rgba(255,255,255,0.9);">January 2024 - March 2024 | Los Angeles, CA</p>
            <p style="color: rgba(255,255,255,0.8);">Exploring AI safety and alignment challenges</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Program Focus:</strong>
            <ul>
                <li>Developed practical ML skills using PyTorch and micrograd</li>
                <li>Explored AI safety and alignment challenges</li>
                <li>Studied AI existential risks and impacts on humanity's future</li>
                <li>Contributed to understanding AI system failure modes</li>
                <li>Worked alongside fellow ML students at UCLA</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # NASA Internship
        st.markdown("""
        <div class="experience-card">
            <h3 style="color: white;">🚀 Engineering & Design Intern - NASA</h3>
            <p style="color: rgba(255,255,255,0.9);">February 2022 - August 2022 | Remote</p>
            <p style="color: rgba(255,255,255,0.8);">Community College Aerospace Scholars Program</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <strong>Project Achievements:</strong>
            <ul>
                <li>Collaborated on Mars rover capstone project</li>
                <li>Designed modern Mars rover blueprint with ML/AI systems</li>
                <li>Built project hardware and software components</li>
                <li>Enhanced NASA Mars rover functionality and adaptability</li>
                <li>Addressed complications with current Mars rover technology</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown("## Technical Projects")
        
        # Featured Project 1
        st.markdown("""
        <div class="project-card">
            <h3 style="color: white;">📱 AI Life Journal using VLMs and LangChain</h3>
            <p style="color: rgba(255,255,255,0.9);">June 2025 - Present</p>
            <p style="color: rgba(255,255,255,0.8);"><a href="https://github.com/CalebTraxler/TraxlerTechnologyApp_" style="color: rgba(255,255,255,0.9);">View on GitHub</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            Cross-platform mobile application enabling users to capture and reflect on daily experiences 
            using Meta Ray-Ban AI glasses. Features vision-language models, LangChain memory, and secure 
            AI-driven insights architecture.
        </div>
        """, unsafe_allow_html=True)
        
        # Featured Project 2
        st.markdown("""
        <div class="project-card">
            <h3 style="color: white;">🗺️ Generative Route Prediction with HMMs</h3>
            <p style="color: rgba(255,255,255,0.9);">May 2025 - June 2025</p>
            <p style="color: rgba(255,255,255,0.8);"><a href="https://github.com/CalebTraxler/HMM-3D-Routing" style="color: rgba(255,255,255,0.9);">View on GitHub</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            Developed discrete Hidden Markov Models to generate realistic driving routes from KITTI-360 
            3D point cloud maps. Under review for publication.
        </div>
        """, unsafe_allow_html=True)
        
        # Featured Project 3
        st.markdown("""
        <div class="project-card">
            <h3 style="color: white;">🪐 Exoplanet Habitability Analysis</h3>
            <p style="color: rgba(255,255,255,0.9);">May 2025 - June 2025</p>
            <p style="color: rgba(255,255,255,0.8);">
                <a href="https://planet-habitability.streamlit.app/" style="color: rgba(255,255,255,0.9);">Live App</a> | 
                <a href="https://arxiv.org/abs/2506.18200" style="color: rgba(255,255,255,0.9);">arXiv Paper</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            Comprehensive multivariate statistical analysis of 517 exoplanets with interactive 3D visualization. 
            Published in arXiv with live Streamlit application.
        </div>
        """, unsafe_allow_html=True)
        
        # Additional Projects Grid
        st.markdown("### Additional Projects")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="project-card">
                <h4 style="color: white;">🚗 Autonomous Driving via CNN and Groq API</h4>
                <p style="color: rgba(255,255,255,0.9);">September 2024 - March 2025</p>
                <p style="color: rgba(255,255,255,0.8);">Real-time lane detection using U-Net CNN with >95% accuracy and <50ms latency. Currently under review for publication.</p>
                <p style="color: rgba(255,255,255,0.8);"><a href="https://github.com/CalebTraxler/Autonomous_Driving_CV" style="color: rgba(255,255,255,0.9);">GitHub Repository</a></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="project-card">
                <h4 style="color: white;">🏠 Real Estate ROI Geo-Locator</h4>
                <p style="color: rgba(255,255,255,0.9);">January 2025 - March 2025</p>
                <p style="color: rgba(255,255,255,0.8);">Interactive 3D visualization using Streamlit and PyDeck to analyze real-time ROI trends across different markets.</p>
                <p style="color: rgba(255,255,255,0.8);"><a href="https://lnkd.in/g_NrKj-b" style="color: rgba(255,255,255,0.9);">Live Application</a></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="project-card">
                <h4 style="color: white;">🧠 Neural Network Binary Classification</h4>
                <p style="color: rgba(255,255,255,0.9);">Academic Project</p>
                <p style="color: rgba(255,255,255,0.8);">Two-layer neural network for classifying numbers as even or odd. Achieved 97.24% validation accuracy on MNIST dataset with L2 regularization.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="project-card">
                <h4 style="color: white;">🎯 K-means Clustering on CIFAR-10</h4>
                <p style="color: rgba(255,255,255,0.9);">Academic Project</p>
                <p style="color: rgba(255,255,255,0.8);">Applied K-means clustering to 60K labeled images with PCA dimensionality reduction and k=10 clustering analysis.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab6:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown("## Publications")
        
        # Publication Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">2</h4><p>Total Papers</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">arXiv</h4><p>Platform</p></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">3</h4><p>Research Areas</p></div>', unsafe_allow_html=True)
        
        # Publication 1
        st.markdown("""
        <div class="publication-card">
            <h4>🪐 Multivariate Statistical Analysis of Exoplanet Habitability</h4>
            <p><strong>Authors:</strong> <strong>Traxler, C.</strong>, et al. (2025)</p>
            <p><strong>arXiv:</strong> 2506.18200</p>
            <p>Comprehensive analysis of 517 exoplanets from NASA Exoplanet Archive to identify 
            potentially habitable worlds and quantify detection bias.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.link_button("📄 Read Paper", "https://arxiv.org/abs/2506.18200")
        with col2:
            st.link_button("🌐 Live Demo", "https://planet-habitability.streamlit.app/")
        with col3:
            st.link_button("💻 GitHub", "https://github.com/CalebTraxler")
        
        # Publication 2
        st.markdown("""
        <div class="publication-card">
            <h4>🦠 Analysis of COVID-19 Infection Dynamics</h4>
            <p><strong>Authors:</strong> <strong>Traxler, C.</strong>, et al. (2025)</p>
            <p><strong>arXiv:</strong> 2505.13754</p>
            <p>Advanced mathematical modeling using extended SIR/SEIR models with bifurcation analysis 
            for predictive modeling of pandemic spread patterns.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("📄 Read Paper", "https://arxiv.org/abs/2505.13753")
        with col2:
            st.link_button("🔬 Research Details", "https://github.com/CalebTraxler")
        
        # Future Publications
        st.markdown("""
        <div class="info-box">
            <h4>🔮 Upcoming Publications</h4>
            <ul>
                <li><strong>In Review:</strong> Generative Route Prediction with HMMs and 3D Point Clouds</li>
                <li><strong>In Review:</strong> Autonomous Driving via CNN and Real-time Analysis</li>
                <li><strong>In Progress:</strong> Variational Inference in Chemical Data Analysis</li>
                <li><strong>In Progress:</strong> Urban Heat Islands using ECOSTRESS Data</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab7:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.markdown("## Investment Portfolio")
        
        # Investment Philosophy
        st.markdown("""
        <div class="investment-card">
            <h3>💡 Investment Philosophy</h3>
            <p>Active investor in real estate and public markets with a focus on long-term value creation, 
            financial modeling, and portfolio diversification. Passionate about identifying emerging market 
            opportunities and applying data-driven analysis to investment decisions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Current Investment
        st.markdown("""
        <div class="investment-card">
            <h3>🏡 First Property Investment - Topeka, Kansas</h3>
            <p><strong>Achievement:</strong> Purchased first property at age 22</p>
            <p><strong>Strategy:</strong> BRRRR Method (Buy, Rehab, Rent, Refinance, Repeat)</p>
            <p><strong>Status:</strong> Currently under renovation</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Property Images
        try:
            col1, col2, col3 = st.columns(3)
            with col1:
                image1 = Image.open("Investments/1.jpg")
                st.image(image1, caption="Property Exterior", use_container_width=True)
            with col2:
                image2 = Image.open("Investments/2.png")
                st.image(image2, caption="Interior View", use_container_width=True)
            with col3:
                image3 = Image.open("Investments/3.png")
                st.image(image3, caption="Renovation Progress", use_container_width=True)
        except:
            st.info("Property photos will be displayed here once available.")
        
        # Investment Goals
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h4>📈 2025 Goals</h4>
                <ul>
                    <li>Acquire second property in Texas</li>
                    <li>Research multi-family opportunities</li>
                    <li>Develop automated analysis tools</li>
                    <li>Join investment groups</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h4>🎯 Long-term Vision</h4>
                <ul>
                    <li>Diverse residential portfolio</li>
                    <li>Commercial real estate exploration</li>
                    <li>Geographic expansion</li>
                    <li>AI/ML integration in analysis</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Portfolio Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">1</h4><p>Properties Owned</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">15%+</h4><p>Target ROI</p></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">10+</h4><p>Year Timeline</p></div>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="metric-card"><h4 style="color: #667eea;">Q4 2025</h4><p>Next Purchase</p></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Technical Skills Section with enhanced design
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("## 🛠️ Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="skill-card">
            <h4>💻 Languages & Platforms</h4>
            <p>Python • R • JavaScript • SQL • MATLAB • Bash<br>
            AWS • Firebase • Vercel • Docker • Git</p>
        </div>
        
        <div class="skill-card">
            <h4>🤖 Machine Learning & AI</h4>
            <p>Deep Learning • Generative AI • VLMs<br>
            Transformers • NLP • Reinforcement Learning<br>
            HMMs • Variational Inference • Bayesian Networks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="skill-card">
            <h4>📚 Frameworks & Libraries</h4>
            <p>NumPy • Pandas • Scikit-learn • TensorFlow<br>
            PyTorch • Keras • OpenCV • Hugging Face<br>
            LangChain • Plotly • Streamlit</p>
        </div>
        
        <div class="skill-card">
            <h4>🔧 Development Tools</h4>
            <p>Jupyter • VSCode • REST APIs • Linux<br>
            CI/CD • Auth0 • Big Data Tools<br>
            GIS • Scientific Computing</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced Footer
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #4A5568; padding: 2rem; background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); border-radius: 15px; margin-top: 2rem;">
        <h4 style="color: #2D3748; margin-bottom: 1rem;">Connect With Me</h4>
        <p style="margin-bottom: 1rem;">
            <a href="mailto:calebtraxler34@gmail.com" style="color: #667eea; margin: 0 1rem;">📧 Email</a> •
            <a href="https://www.linkedin.com/in/calebtraxler" style="color: #667eea; margin: 0 1rem;">💼 LinkedIn</a> •
            <a href="https://github.com/calebtraxler" style="color: #667eea; margin: 0 1rem;">💻 GitHub</a> •
            <a href="https://traxlertechnology.vercel.app" style="color: #667eea; margin: 0 1rem;">🌐 Company</a>
        </p>
        <p style="font-size: 0.9rem; color: #718096;">
            © 2025 Caleb Traxler. Built with Streamlit • Last updated: January 2025
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
