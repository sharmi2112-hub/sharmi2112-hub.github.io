"""
Sharmi Thakor - Data Analyst & Machine Learning Portfolio
Streamlit Web Application
"""

import streamlit as st
from PIL import Image
import os

# Page Configuration
st.set_page_config(
    page_title="Sharmi Thakor | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #0b0f17;
        color: #f8fafc;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }
    .highlight {
        color: #38bdf8;
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        background: rgba(56, 189, 248, 0.1);
        border: 1px solid rgba(56, 189, 248, 0.25);
        color: #38bdf8;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
    }
    .metric-val {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38bdf8;
    }
    .metric-lbl {
        font-size: 0.85rem;
        color: #94a3b8;
    }
    .project-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 6px;
        background: #1f2937;
        color: #cbd5e1;
        font-size: 0.75rem;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="badge">Data Analyst & Machine Learning Specialist • London, UK</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Turning Complex Data into <span class="highlight">Strategic Insights</span> & Applied AI.</div>', unsafe_allow_html=True)
st.write(
    "MSc Data Science graduate based in London specializing in SQL relational modeling, statistical testing, "
    "machine learning pipelines, and executive Power BI dashboards. Experienced in translating raw commercial and public "
    "datasets into reproducible, decision-grade analytics."
)

st.write("---")

# Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-val">50k+</div><div class="metric-lbl">Evaluated Records</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-val">3</div><div class="metric-lbl">Production Systems</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-val">100%</div><div class="metric-lbl">Reproducible Code</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-val">London</div><div class="metric-lbl">Immediate Availability</div></div>', unsafe_allow_html=True)

st.write("---")

# Projects Section
st.subheader("Featured Analytical Ventures")

tab1, tab2, tab3 = st.tabs([
    "Conduct Risk Analytics",
    "People Analytics & Benchmarks",
    "Deepfake Detection AI"
])

# Project 1: Conduct Risk
with tab1:
    col_a, col_b = st.columns([1.2, 1])
    with col_a:
        st.markdown("### Conduct Risk & Customer Outcome Monitoring")
        st.caption("Regulatory Risk Analytics • UK Financial Conduct Authority (FCA PS22/9)")
        st.write(
            "Monitoring and governance reporting suite engineered to satisfy UK Financial Conduct Authority (FCA) "
            "Consumer Duty requirements. Audits 50,000 policy sales and 10,000 complaints against published FCA Value Measures "
            "benchmarks, tracking fair value claims ratios, operational support SLAs, and vulnerable customer disparities."
        )
        st.markdown("**Key Capabilities:**")
        st.markdown("- Multi-dimensional vulnerability matrix categorizing health, resilience, and life-event risk triggers.")
        st.markdown("- Claims ratio and fair value diagnostic flagging products below published FCA benchmark thresholds.")
        st.markdown("- 4-page interactive Power BI suite backed by a Star Schema SQLite database.")
        st.markdown(
            "**Stack:** `Power BI` `SQL (SQLite)` `Python` `Star Schema` `FCA Benchmarks` `Conduct Risk`"
        )
        st.link_button("View Repository on GitHub", "https://github.com/sharmi2112-hub/conduct-risk-customer-outcomes")

    with col_b:
        img_path = os.path.join("assets", "images", "consumer-duty-p1.jpg")
        if os.path.exists(img_path):
            st.image(img_path, caption="Executive Outcomes Overview", use_container_width=True)

# Project 2: People Analytics
with tab2:
    col_c, col_d = st.columns([1.2, 1])
    with col_c:
        st.markdown("### Workforce Planning & Labour Market Benchmarks")
        st.caption("People Analytics • Dimensional Star Schema SQL • ONS ASHE")
        st.write(
            "Interactive reporting suite harmonizing organizational human capital data with official UK benchmarks "
            "(ONS ASHE salary figures and real-time Adzuna vacancy demand) to pinpoint salary compression, critical skills shortages, "
            "and 5-year succession and retirement risk."
        )
        st.markdown("**Key Capabilities:**")
        st.markdown("- Dimensional star schema with fact and dimension tables optimized for Power BI DAX calculations.")
        st.markdown("- Automated Python ETL pipelines ingesting and standardizing Nomis regional wage indexes and Adzuna API feeds.")
        st.markdown("- Succession pipeline readiness scoring identifying critical operational single-point-of-failure roles.")
        st.markdown(
            "**Stack:** `Python` `SQL (SQLite)` `Power BI` `DAX` `ONS ASHE Data` `People Analytics`"
        )
        st.link_button("View Repository on GitHub", "https://github.com/sharmi2112-hub/people-analytics-market-benchmarks")

    with col_d:
        img_path = os.path.join("assets", "images", "workforce-p1.jpg")
        if os.path.exists(img_path):
            st.image(img_path, caption="Workforce Planning Executive Overview", use_container_width=True)

# Project 3: Deepfake Detection AI
with tab3:
    col_e, col_f = st.columns([1.2, 1])
    with col_e:
        st.markdown("### Deepfake Face Detection AI Engine & Web App")
        st.caption("Computer Vision • Deep Learning • Streamlit")
        st.write(
            "Computer vision classification pipeline developed from scratch for binary detection of real versus deepfake facial media. "
            "Evaluates three custom Convolutional Neural Network (CNN) architectures across 8,400 balanced facial images and deploys "
            "a real-time interactive Streamlit web application."
        )
        st.markdown("**Key Capabilities:**")
        st.markdown("- Benchmarked Baseline CNN, Deep CNN with Batch Normalization, and Wide CNN using TensorFlow and Keras.")
        st.markdown("- Achieved 74.50% test accuracy and 0.834 ROC-AUC on 64x64 facial crops with data augmentation.")
        st.markdown("- Integrated live Streamlit web interface allowing real-time image uploads and instant probability score visualization.")
        st.markdown(
            "**Stack:** `Python` `TensorFlow` `Keras` `CNNs` `Streamlit` `Computer Vision`"
        )
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.link_button("View Repository on GitHub", "https://github.com/sharmi2112-hub/DEEPFAKE-face-Detaction-using-Deep-learning")
        with col_btn2:
            st.link_button("Launch Live Streamlit App", "https://deepfake-face-detaction-using-deep-learning-kz5ysgjthhxgv2y9hn.streamlit.app/")

    with col_f:
        img_path = os.path.join("assets", "images", "deepfake-p1.jpg")
        if os.path.exists(img_path):
            st.image(img_path, caption="Deepfake Detection Web Architecture", use_container_width=True)

st.write("---")

# Skills Matrix
st.subheader("Technical Competencies & Stack Matrix")

scol1, scol2, scol3 = st.columns(3)

with scol1:
    st.markdown("#### Languages & Querying")
    st.markdown("- **Python** (Pandas, NumPy, Scikit-learn, TF)")
    st.markdown("- **SQL** (SQLite, PostgreSQL, Window Functions)")
    st.markdown("- **R Language** (ggplot2, Statistical Tests)")
    st.markdown("- **JavaScript, HTML5 & CSS3**")

with scol2:
    st.markdown("#### BI & Visualization")
    st.markdown("- **Power BI Desktop & Service**")
    st.markdown("- **DAX Modeling & Calculated Measures**")
    st.markdown("- **Tableau**")
    st.markdown("- **Matplotlib, Seaborn, ggplot2**")

with scol3:
    st.markdown("#### Machine Learning & Data Eng")
    st.markdown("- **Supervised & Unsupervised Learning**")
    st.markdown("- **Convolutional Neural Networks (CNN)**")
    st.markdown("- **Star Schema Relational Design**")
    st.markdown("- **ETL Pipelines & Automated Testing (pytest)**")

st.write("---")

# Education Section
st.subheader("Academic Qualifications")
ecol1, ecol2 = st.columns(2)

with ecol1:
    st.markdown("### Master of Science (MSc) in Data Science")
    st.markdown("**Coventry University** • London, United Kingdom (2025 – 2026)")
    st.write(
        "Advanced curriculum in statistical analysis, machine learning algorithms, big data technologies, "
        "and predictive visualization applied to real-world datasets."
    )

with ecol2:
    st.markdown("### Bachelor of Engineering (B.E.) in Information Technology")
    st.markdown("**Parul Institute of Engineering & Technology** • Gujarat, India (2019 – 2023)")
    st.write(
        "Rigorous foundation in computer science, relational databases, data structures, algorithms, "
        "and software engineering principles."
    )

st.write("---")

# Contact Section
st.subheader("Contact & Location")
st.write("Available for full-time Data Analyst, BI Analyst, and Data Science roles in London and remote UK.")
st.markdown("- **Location:** London, United Kingdom")
st.markdown("- **Email:** [sharmithakor2112@gmail.com](mailto:sharmithakor2112@gmail.com)")
st.markdown("- **GitHub:** [github.com/sharmi2112-hub](https://github.com/sharmi2112-hub)")
st.caption("© 2026 Sharmi Thakor. All rights reserved.")
