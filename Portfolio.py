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
            padding: 2rem;
            font-family: 'Inter', sans-serif;
        }
        
        /* Color Variables */
        :root {
            --primary-blue: #0066CC;
            --secondary-blue: #4A90E2;
            --accent-green: #28A745;
            --accent-purple: #6F42C1;
            --accent-orange: #FD7E14;
            --light-gray: #F8F9FA;
            --medium-gray: #E9ECEF;
            --dark-gray: #6C757D;
            --success-green: #20C997;
            --warning-yellow: #FFC107;
        }
        
        /* Header Styles */
        .header-container {
            background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0, 102, 204, 0.2);
        }
        
        .header-title {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .header-subtitle {
            font-size: 1.3rem;
            font-weight: 400;
            opacity: 0.95;
            margin-bottom: 1rem;
        }
        
        /* Professional Summary Card */
        .summary-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid var(--accent-green);
            margin-bottom: 2rem;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        
        .summary-title {
            color: var(--primary-blue);
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        /* Tab Styling */
        .stTabs {
            background: white;
            padding: 0.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
            justify-content: space-evenly;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 10px;
            color: var(--dark-gray);
            font-size: 14px;
            font-weight: 600;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            margin: 0.25rem;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 102, 204, 0.3);
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: linear-gradient(135deg, var(--secondary-blue) 0%, var(--primary-blue) 100%);
            color: white;
            transform: translateY(-1px);
        }
        
        /* Card Styles */
        .info-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            border-top: 4px solid var(--secondary-blue);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .education-card {
            border-top-color: var(--accent-green);
        }
        
        .research-card {
            border-top-color: var(--accent-purple);
        }
        
        .experience-card {
            border-top-color: var(--accent-orange);
        }
        
        .project-card {
            border-top-color: var(--success-green);
        }
        
        .publication-card {
            background: linear-gradient(135deg, #fff8e1 0%, #fff3c4 100%);
            border: 1px solid var(--warning-yellow);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 15px rgba(255, 193, 7, 0.2);
        }
        
        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, white 0%, #f8f9fa 100%);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-top: 4px solid var(--accent-green);
            margin-bottom: 1rem;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary-blue);
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            color: var(--dark-gray);
            font-weight: 500;
        }
        
        /* Skill Categories */
        .skill-category {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            padding: 1.25rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border-left: 4px solid var(--primary-blue);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .skill-category h4 {
            color: var(--primary-blue);
            margin-bottom: 0.75rem;
            font-weight: 600;
        }
        
        /* Status Badges */
        .status-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        
        .status-active {
            background: var(--success-green);
            color: white;
        }
        
        .status-completed {
            background: var(--primary-blue);
            color: white;
        }
        
        .status-in-review {
            background: var(--warning-yellow);
            color: #333;
        }
        
        /* Button Styles */
        .stButton>button {
            background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
            color: white;
            font-weight: 600;
            border-radius: 8px;
            border: none;
            padding: 0.75rem 1.5rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 102, 204, 0.4);
        }
        
        /* Link Buttons */
        .custom-link-button {
            display: inline-block;
            background: linear-gradient(135deg, var(--accent-green) 0%, #20c997 100%);
            color: white;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-weight: 500;
            margin: 0.25rem;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(40, 167, 69, 0.3);
        }
        
        .custom-link-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(40, 167, 69, 0.4);
            text-decoration: none;
            color: white;
        }
        
        /* Section Headers */
        .section-header {
            color: var(--primary-blue);
            font-size: 1.75rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid var(--medium-gray);
        }
        
        /* Footer */
        .footer {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            text-align: center;
            padding: 2rem;
            border-radius: 12px;
            margin-top: 3rem;
        }
        
        .footer a {
            color: #74b9ff;
            text-decoration: none;
            margin: 0 0.5rem;
            transition: color 0.3s ease;
        }
        
        .footer a:hover {
            color: #0984e3;
        }
        
        /* Contact Grid */
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-bottom: 1rem;
        }
        
        .contact-item {
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            border-radius: 8px;
            backdrop-filter: blur(10px);
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .header-title {
                font-size: 2rem;
            }
            
            .header-subtitle {
                font-size: 1rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                font-size: 12px;
                padding: 0.5rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Caleb Traxler's Portfolio", layout="wide", page_icon="🎓")
    set_custom_style()
    
    # Header Section
    st.markdown("""
    <div class="header-container">
        <div style="display: flex; align-items: center; gap: 2rem;">
            <div style="flex: 1;">
                <h1 class="header-title">Caleb Traxler</h1>
                <p class="header-subtitle">Data Scientist | ML Engineer | Researcher | Entrepreneur | Investor</p>
                <div class="contact-grid">
                    <div class="contact-item">
                        <strong>📧 Email:</strong><br>
                        <a href="mailto:calebtraxler34@gmail.com" style="color: white;">calebtraxler34@gmail.com</a>
                    </div>
                    <div class="contact-item">
                        <strong>📞 Phone:</strong><br>
                        (805) 377-8182
                    </div>
                    <div class="contact-item">
                        <strong>🎓 Academic:</strong><br>
                        <a href="mailto:traxlerc@uci.edu" style="color: white;">traxlerc@uci.edu</a>
                    </div>
                    <div class="contact-item">
                        <strong>🔗 Links:</strong><br>
                        <a href="https://www.linkedin.com/in/calebtraxler" style="color: white;">LinkedIn</a> | 
                        <a href="https://github.com/calebtraxler" style="color: white;">GitHub</a> | 
                        <a href="https://traxlertechnology.vercel.app" style="color: white;">Company</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Summary
    st.markdown("""
    <div class="summary-card">
        <h3 class="summary-title">Professional Summary</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; color: #495057;">
            Data Science graduate student specializing in Machine Learning, Data Science and Computer Vision. Published 
            academic researcher with significant entrepreneurial experience developing scalable Artificial Intelligence systems. 
            Actively seeking PhD opportunities in computer science (start date: September 2026) and job opportunities in 
            the data science and machine learning space (start date: December 2025).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "About Me", "Education", "Research", "Experience", "Projects", "Publications", "Investments"
    ])
    
    with tab1:
        st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <p style="font-size: 1.1rem; line-height: 1.7;">
                    I'm Caleb Traxler, a passionate Data Science graduate student at UC Irvine with a strong 
                    foundation in Machine Learning, Computer Vision, and AI research. As a published researcher and 
                    entrepreneur, I'm dedicated to advancing the field of artificial intelligence and its applications.
                </p>
                
                <h4 style="color: var(--primary-blue); margin-top: 1.5rem;">Current Focus</h4>
                <ul style="line-height: 1.6;">
                    <li>Pursuing M.S. in Data Science at UC Irvine (GPA: 3.97)</li>
                    <li>Conducting cutting-edge research in variational inference and geospatial analysis</li>
                    <li>Leading Traxler Technology LLC, building multimodal AI systems</li>
                    <li>Active investor in real estate and securities markets</li>
                </ul>
                
                <h4 style="color: var(--primary-blue); margin-top: 1.5rem;">Career Goals</h4>
                <ul style="line-height: 1.6;">
                    <li>Seeking PhD opportunities in Computer Science (September 2026)</li>
                    <li>Open to data science and ML engineering roles (December 2025)</li>
                </ul>
                
                <h4 style="color: var(--primary-blue); margin-top: 1.5rem;">Personal Interests</h4>
                <ul style="line-height: 1.6;">
                    <li>Surfing and weight training</li>
                    <li>Traveling and exploring new cultures</li>
                    <li>Visiting amusement parks</li>
                    <li>Discovering amazing cuisines</li>
                    <li>Building full-stack applications</li>
                    <li>Exploring new ML architectures and contributing to open-source projects</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Quick Stats")
            
            # Metrics with custom styling
            metrics_html = """
            <div class="metric-card">
                <div class="metric-value">3.97</div>
                <div class="metric-label">Current GPA<br>UC Irvine</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">2</div>
                <div class="metric-label">Publications<br>arXiv papers</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">15+</div>
                <div class="metric-label">GitHub Projects<br>Public repos</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">3</div>
                <div class="metric-label">Research Areas<br>Active projects</div>
            </div>
            """
            st.markdown(metrics_html, unsafe_allow_html=True)
        
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
            st.markdown("""
            <div class="info-card">
                <h4 style="color: var(--primary-blue);">Travel Adventures</h4>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.image("travel/japan.png", caption="Exploring Japan", use_column_width=True)
                st.image("travel/japan2.png", caption="Cultural experiences", use_column_width=True)
            except:
                st.info("Travel photos coming soon!")
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4 style="color: var(--accent-green);">Theme Parks</h4>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.image("parks/universal.png", caption="Universal Studios", use_column_width=True)
                st.image("parks/stormtroopers.png", caption="Disneyland adventures", use_column_width=True)
            except:
                st.info("Theme park photos coming soon!")
        
        with col3:
            st.markdown("""
            <div class="info-card">
                <h4 style="color: var(--accent-orange);">Culinary Experiences</h4>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.image("food/crab.png", caption="Santa Barbara pier dining", use_column_width=True)
                st.image("food/omlet.png", caption="Tamagoyaki in Japan", use_column_width=True)
            except:
                st.info("Food photos coming soon!")
    
    with tab2:
        st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
        
        # UC Irvine
        st.markdown("""
        <div class="info-card education-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="margin-right: 1rem;">
                    <span style="background: var(--accent-green); color: white; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">Current</span>
                </div>
                <h3 style="color: var(--primary-blue); margin: 0;">University of California, Irvine</h3>
            </div>
            <p style="font-size: 1.1rem; font-weight: 600; color: #495057;">Master of Science in Data Science | GPA: 3.97</p>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">September 2024 - December 2025</p>
            
            <h4 style="color: var(--accent-green); margin-bottom: 0.5rem;">Specializations</h4>
            <ul style="columns: 2; column-gap: 2rem;">
                <li>Artificial Intelligence</li>
                <li>Generative Models</li>
                <li>Computer Vision</li>
                <li>Geographic Information Systems (GIS)</li>
                <li>Big Data Analytics</li>
            </ul>
            
            <h4 style="color: var(--accent-green); margin-bottom: 0.5rem;">Key Achievements</h4>
            <ul>
                <li>UCI Master of Data Science Scholarship Recipient</li>
                <li>Accelerated 15-month program</li>
                <li>Maintaining 3.97 GPA</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # UCLA
        st.markdown("""
        <div class="info-card education-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="margin-right: 1rem;">
                    <span style="background: var(--primary-blue); color: white; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">Completed</span>
                </div>
                <h3 style="color: var(--primary-blue); margin: 0;">University of California, Los Angeles</h3>
            </div>
            <p style="font-size: 1.1rem; font-weight: 600; color: #495057;">Bachelor of Science in Mathematics & Computer Science | GPA: 3.81</p>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">September 2022 - June 2024</p>
            
            <h4 style="color: var(--accent-green); margin-bottom: 0.5rem;">Honors & Activities</h4>
            <ul style="columns: 2; column-gap: 2rem;">
                <li>Phi Theta Kappa Honors Society</li>
                <li>AI Safety Fellowship</li>
                <li>Undergraduate Mathematics Student Association (UMSA)</li>
                <li>Undergraduate Mathematics Research (Prof. Shbia Biswal)</li>
            </ul>
            
            <h4 style="color: var(--accent-green); margin-bottom: 0.5rem;">Concentrations</h4>
            <ul>
                <li>Applied Mathematics</li>
                <li>Computer Science</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Moorpark College
        st.markdown("""
        <div class="info-card education-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="margin-right: 1rem;">
                    <span style="background: var(--primary-blue); color: white; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">Completed</span>
                </div>
                <h3 style="color: var(--primary-blue); margin: 0;">Moorpark College</h3>
            </div>
            <p style="font-size: 1.1rem; font-weight: 600; color: #495057;">Associate of Science in Mathematics, Physics & Computer Science | GPA: 4.00</p>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">August 2020 - June 2022</p>
            
            <h4 style="color: var(--accent-green); margin-bottom: 0.5rem;">Achievements</h4>
            <ul style="columns: 2; column-gap: 2rem;">
                <li>Dean's List (2020-2022)</li>
                <li>Honor Roll (2020-2022)</li>
                <li>Phi Theta Kappa Honors Society</li>
                <li>NASA Community College Aerospace Scholars Internship</li>
                <li>Mathematics Tutor</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<h2 class="section-header">Research Experience</h2>', unsafe_allow_html=True)
        
        # Current Research Positions
        st.subheader("Current Research Positions")
        
        st.markdown("""
        <div class="info-card research-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--accent-purple); margin: 0;">Variational Inference Research</h3>
                <span class="status-badge status-active">Active</span>
            </div>
            <p style="font-weight: 600; color: #495057;">Graduate Research Assistant - UC Irvine (Prof. Erik Sudderth)</p>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">June 2025 - Present | Irvine, CA</p>
            
            <h4 style="color: var(--accent-purple); margin-bottom: 0.5rem;">Research Focus</h4>
            <ul>
                <li>Variational inference with Gauss-Markov distributions</li>
                <li>Applying methods to Stochastic Differential Equation (SDE) time series models</li>
                <li>Future project involving chemical data analysis</li>
                <li>Advanced probabilistic modeling and inference techniques</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card research-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--accent-purple); margin: 0;">Geospatial Climate Research</h3>
                <span class="status-badge status-active">Active</span>
            </div>
            <p style="font-weight: 600; color: #495057;">Graduate Research Assistant - UC Irvine (Prof. Jun Wu)</p>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">June 2025 - Present | Irvine, CA</p>
            
            <h4 style="color: var(--accent-purple); margin-bottom: 0.5rem;">Research Focus</h4>
            <ul>
                <li>ECOSTRESS satellite data analysis</li>
                <li>Extreme heat distribution mapping across California urban zones</li>
                <li>Spatial data handling and GIS analysis</li>
                <li>Python-based geospatial analysis and visualization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Previous Research
        st.subheader("Previous Research")
        
        st.markdown("""
        <div class="info-card research-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--accent-purple); margin: 0;">COVID-19 Mathematical Modeling</h3>
                <span class="status-badge status-completed">Published</span>
            </div>
            <p style="font-weight: 600; color: #495057;">Undergraduate Researcher - UCLA (Prof. Shbia Biswal)</p>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">March 2023 - June 2023 | Los Angeles, CA</p>
            
            <h4 style="color: var(--accent-purple); margin-bottom: 0.5rem;">Research Achievements</h4>
            <ul>
                <li>Modeled COVID-19 dynamics using extended SIR/SEIR models</li>
                <li>Analyzed Orange County COVID-19 data using Python and Jupyter notebooks</li>
                <li>Developed innovative bifurcation diagrams for predictive modeling</li>
                <li><strong>Published in arXiv:</strong> <a href="https://arxiv.org/abs/2505.13753" class="custom-link-button" target="_blank">View Publication</a></li>
                <li>Identified critical transcritical bifurcation thresholds for predictions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
        
        # Current Positions
        st.markdown("""
        <div class="info-card experience-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--accent-orange); margin: 0;">Founder & CEO - Traxler Technology LLC</h3>
                <span class="status-badge status-active">Active</span>
            </div>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">November 2024 - Present | Los Angeles, CA</p>
            
            <h4 style="color: var(--accent-orange); margin-bottom: 0.5rem;">Company Overview</h4>
            <ul>
                <li>AI-focused startup building multimodal intelligence systems</li>
                <li><a href="https://traxlertechnology.vercel.app/login" class="custom-link-button" target="_blank">Visit Traxler Technology</a></li>
            </ul>
            
            <h4 style="color: var(--accent-orange); margin-bottom: 0.5rem;">Key Achievements</h4>
            <ul>
                <li>Designed and deployed scalable full-stack platforms</li>
                <li>Tech Stack: React, Firebase, AWS EC2, Vercel, Auth0</li>
                <li>Developing cross-platform mobile applications</li>
                <li>Focus on vision-language models and AI-driven insights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card experience-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--accent-orange); margin: 0;">Program Ambassador - UC Irvine</h3>
                <span class="status-badge status-active">Active</span>
            </div>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">September 2024 - Present | Irvine, CA</p>
            
            <h4 style="color: var(--accent-orange); margin-bottom: 0.5rem;">Responsibilities</h4>
            <ul>
                <li>Ambassador for Masters of Data Science program (2024-2025 cohort)</li>
                <li>Support creation and development of marketing campaigns</li>
                <li>Student outreach and program promotion</li>
                <li><a href="https://ics.uci.edu/?people=caleb-traxler" class="custom-link-button" target="_blank">UCI Faculty Profile</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Previous Experience
        st.markdown("""
        <div class="info-card experience-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--accent-orange); margin: 0;">Data Scientist & ML Engineer Intern - Amgen</h3>
                <span style="background: var(--warning-yellow); color: #333; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">Award Winner</span>
            </div>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">July 2024 - September 2024 | Remote</p>
            
            <h4 style="color: var(--accent-orange); margin-bottom: 0.5rem;">Key Achievements</h4>
            <ul>
                <li>Built rare disease prioritization model using generative AI</li>
                <li>Reduced year-long process to minutes using GenAI pipeline</li>
                <li>Developed Streamlit application for stakeholder data visualization</li>
                <li><strong>Winner: Amgen AI Symposium 2024</strong></li>
                <li>96% accuracy in disease scoring automation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional experiences in a more compact format
        experiences = [
            {
                "title": "AI Safety Fellowship - UCLA",
                "period": "January 2024 - March 2024",
                "points": [
                    "Developed practical ML skills using PyTorch and micrograd",
                    "Explored AI safety and alignment challenges",
                    "Studied AI existential risks and impacts on humanity's future"
                ]
            },
            {
                "title": "Engineering & Design Intern - NASA",
                "period": "February 2022 - August 2022",
                "points": [
                    "Mars rover capstone project collaboration",
                    "Designed modern Mars rover blueprint with ML/AI systems",
                    "NASA Community College Aerospace Scholars Program"
                ]
            }
        ]
        
        for exp in experiences:
            st.markdown(f"""
            <div class="info-card experience-card">
                <h4 style="color: var(--accent-orange); margin-bottom: 0.5rem;">{exp['title']}</h4>
                <p style="color: var(--dark-gray); margin-bottom: 0.75rem;">{exp['period']}</p>
                <ul>
                    {''.join([f'<li>{point}</li>' for point in exp['points']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown('<h2 class="section-header">Technical Projects</h2>', unsafe_allow_html=True)
        
        # Featured Projects
        st.subheader("Featured Projects")
        
        st.markdown("""
        <div class="info-card project-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: var(--success-green); margin: 0;">AI Life Journal using VLMs and LangChain Memory</h3>
                <span class="status-badge status-active">Active</span>
            </div>
            <p style="color: var(--dark-gray); margin-bottom: 1rem;">June 2025 - Present</p>
            
            <p style="margin-bottom: 1rem;">Cross-platform mobile application (Android & iOS) enabling users to capture, organize, and 
            reflect on daily experiences using Meta Ray-Ban AI glasses and other life-logging devices.</p>
            
            <h4 style="color: var(--success-green); margin-bottom: 0.5rem;">Technical Stack</h4>
            <ul style="columns: 2; column-gap: 2rem; margin-bottom: 1rem;">
                <li>Vision-Language Models (VLMs)</li>
                <li>LangChain for memory-augmented AI</li>
                <li>Cross-platform mobile development</li>
                <li>Secure cloud storage and processing</li>
            </ul>
            
            <a href="https://github.com/CalebTraxler/TraxlerTechnologyApp_" class="custom-link-button" target="_blank">GitHub Repository</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Project grid for remaining projects
        projects = [
            {
                "title": "Generative Route Prediction with HMMs and 3D Point Clouds",
                "status": "In Review",
                "period": "May 2025 - June 2025",
                "description": "Developed discrete Hidden Markov Models (HMMs) to generate realistic driving routes from KITTI-360 3D point cloud maps.",
                "link": "https://github.com/CalebTraxler/HMM-3D-Routing",
                "status_class": "status-in-review"
            },
            {
                "title": "Multivariate Statistical Analysis of Exoplanet Habitability",
                "status": "Published",
                "period": "May 2025 - June 2025",
                "description": "Comprehensive analysis of 517 exoplanets from NASA Exoplanet Archive to identify potentially habitable worlds.",
                "link": "https://planet-habitability.streamlit.app/",
                "status_class": "status-completed"
            },
            {
                "title": "Autonomous Driving via CNN and Groq API",
                "status": "In Review",
                "period": "Sep 2024 - March 2025",
                "description": "Real-time lane detection using U-Net CNN with >95% accuracy and <50ms latency.",
                "link": "https://github.com/CalebTraxler/Autonomous_Driving_CV",
                "status_class": "status-in-review"
            },
            {
                "title": "Real Estate ROI Geo-Locator",
                "status": "Completed",
                "period": "Jan 2025 - March 2025",
                "description": "Interactive 3D visualization using Streamlit and PyDeck to analyze real-time ROI trends.",
                "link": "https://lnkd.in/g_NrKj-b",
                "status_class": "status-completed"
            }
        ]
        
        col1, col2 = st.columns(2)
        for i, project in enumerate(projects):
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"""
                <div class="info-card project-card">
                    <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 0.75rem;">
                        <h4 style="color: var(--success-green); margin: 0; font-size: 1.1rem;">{project['title']}</h4>
                        <span class="status-badge {project['status_class']}">{project['status']}</span>
                    </div>
                    <p style="color: var(--dark-gray); font-size: 0.9rem; margin-bottom: 0.75rem;">{project['period']}</p>
                    <p style="margin-bottom: 1rem; font-size: 0.95rem;">{project['description']}</p>
                    <a href="{project['link']}" class="custom-link-button" target="_blank">View Project</a>
                </div>
                """, unsafe_allow_html=True)
    
    with tab6:
        st.markdown('<h2 class="section-header">Publications</h2>', unsafe_allow_html=True)
        
        # Publication Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">2</div>
                <div class="metric-label">Total Papers</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">arXiv</div>
                <div class="metric-label">Platform</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">3</div>
                <div class="metric-label">Research Areas</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Publications
        st.markdown("""
        <div class="publication-card">
            <h4 style="color: var(--primary-blue); margin-bottom: 0.75rem;">Multivariate Statistical Analysis of Exoplanet Habitability: Detection Bias and Earth Analog Identification</h4>
            <p><strong>Authors:</strong> <strong>Traxler, C.</strong>, et al.</p>
            <p><strong>Published:</strong> 2025 | <strong>arXiv:</strong> 2506.18200</p>
            <p style="margin-bottom: 1rem;"><strong>Abstract:</strong> Comprehensive multivariate statistical analysis of 517 exoplanets from the NASA Exoplanet Archive to identify potentially habitable worlds and quantify detection bias in current surveys.</p>
            <div>
                <a href="https://arxiv.org/abs/2506.18200" class="custom-link-button" target="_blank">Read Paper</a>
                <a href="https://planet-habitability.streamlit.app/" class="custom-link-button" target="_blank">Live Demo</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="publication-card">
            <h4 style="color: var(--primary-blue); margin-bottom: 0.75rem;">Analysis of COVID-19 Infection Dynamics: Extended SIR Model Approach</h4>
            <p><strong>Authors:</strong> <strong>Traxler, C.</strong>, et al.</p>
            <p><strong>Published:</strong> 2025 | <strong>arXiv:</strong> 2505.13754</p>
            <p style="margin-bottom: 1rem;"><strong>Abstract:</strong> Advanced mathematical modeling of COVID-19 dynamics using extended SIR/SEIR models with bifurcation analysis for predictive modeling of pandemic spread patterns.</p>
            <div>
                <a href="https://arxiv.org/abs/2505.13753" class="custom-link-button" target="_blank">Read Paper</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
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
        st.markdown('<h2 class="section-header">Investment Portfolio</h2>', unsafe_allow_html=True)
        
        # Investment Philosophy
        st.markdown("""
        <div class="summary-card">
            <h3 class="summary-title">Investment Philosophy</h3>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                Active investor in real estate and public markets with a focus on long-term value creation, 
                financial modeling, and portfolio diversification. Passionate about identifying emerging market 
                opportunities and applying data-driven analysis to investment decisions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Portfolio Metrics
        col1, col2, col3, col4 = st.columns(4)
        metrics = [
            ("1", "Properties Owned", "First acquisition"),
            ("15%+", "Target ROI", "Annual target"),
            ("Long-term", "Investment Timeline", "10+ years"),
            ("Q4 2025", "Next Purchase", "Texas market")
        ]
        
        for i, (value, label, sublabel) in enumerate(metrics):
            with [col1, col2, col3, col4][i]:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}<br><small>{sublabel}</small></div>
                </div>
                """, unsafe_allow_html=True)
        
        # Real Estate Investment
        st.markdown("""
        <div class="info-card">
            <h3 style="color: var(--primary-blue); margin-bottom: 1rem;">First Property Investment - Topeka, Kansas</h3>
            
            <h4 style="color: var(--accent-green); margin-bottom: 0.5rem;">Investment Details</h4>
            <ul>
                <li><strong>Achievement:</strong> Purchased first property at age 22</li>
                <li><strong>Location:</strong> Topeka, Kansas</li>
                <li><strong>Status:</strong> Currently under renovation</li>
                <li><strong>Strategy:</strong> Fix, refinance, rent (BRRRR method)</li>
                <li><strong>Goal:</strong> Generate passive income and build equity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
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
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4 style="color: var(--primary-blue);">Real Estate Focus</h4>
                <ul>
                    <li>Target emerging neighborhoods with growth potential</li>
                    <li>Value-add opportunities through strategic renovation</li>
                    <li>Geographic diversification (Midwest expansion)</li>
                    <li>Focus on cash flow and appreciation</li>
                    <li>Building relationships with local investors</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4 style="color: var(--primary-blue);">Investment Principles</h4>
                <ul>
                    <li>Data-driven market analysis</li>
                    <li>Long-term value creation</li>
                    <li>Risk management and diversification</li>
                    <li>Continuous market education</li>
                    <li>Leveraging technology for analysis</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Technical Skills Section
    st.markdown("---")
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
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
    st.markdown("""
    <div class="footer">
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">© 2025 Caleb Traxler. All rights reserved.</p>
        <p style="margin-bottom: 1rem;">Built with Streamlit • Last updated: January 2025</p>
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
