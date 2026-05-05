import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vanshika Choudhary | Portfolio", layout="wide")

# --- CUSTOM CSS FOR MODERN LOOK ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stHeader { color: #1E3A8A; }
    .skill-tag {
        background-color: #f0f2f6;
        padding: 5px 12px;
        border-radius: 15px;
        margin-right: 5px;
        display: inline-block;
        margin-bottom: 8px;
        font-size: 14px;
        font-weight: 500;
    }
    hr { margin-top: 2rem; margin-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("Vanshika Choudhary")
st.markdown("#### **Fraud Strategy & Risk Analytics Professional**")
st.write("📍 United States | ✉️ vanshikachoudhary0394@gmail.com | 📞 (469) 744-7863")

col_links = st.columns([1, 1, 1, 6])
with col_links[0]: st.markdown("[LinkedIn](#)")
with col_links[1]: st.markdown("[GitHub](#)")
with col_links[2]: st.markdown("[Impact](#impact)")

st.divider()

# --- PROFESSIONAL SUMMARY ---
st.header("Professional Summary")
st.write("""
Strategy & Risk Analytics professional with 5+ years of experience supporting first-party fraud prevention, 
credit risk decisioning, and fraud lifecycle strategy execution across high-volume consumer transaction environments. 
Advanced proficiency in SQL, Python, and machine learning techniques with a strong background in governance 
and decision engine optimization.
""")

# --- TECHNICAL SKILLS ---
st.header("Technical Skills")
sk1, sk2, sk3, sk4 = st.columns(4)

with sk1:
    st.subheader("Data & Analytics")
    st.markdown('<div class="skill-tag">SQL (BigQuery/Oracle)</div><div class="skill-tag">Python</div><div class="skill-tag">SAS</div><div class="skill-tag">Excel</div>', unsafe_allow_html=True)
with sk2:
    st.subheader("Machine Learning")
    st.markdown('<div class="skill-tag">XGBoost</div><div class="skill-tag">Random Forests</div><div class="skill-tag">A/B Testing</div><div class="skill-tag">Predictive Modeling</div>', unsafe_allow_html=True)
with sk3:
    st.subheader("BI & Visualization")
    st.markdown('<div class="skill-tag">Tableau</div><div class="skill-tag">Power BI</div><div class="skill-tag">Looker</div><div class="skill-tag">Splunk</div>', unsafe_allow_html=True)
with sk4:
    st.subheader("Cloud & Certs")
    st.markdown('<div class="skill-tag">GCP</div><div class="skill-tag">AWS</div><div class="skill-tag">ECBA®</div><div class="skill-tag">Azure Fundamentals</div>', unsafe_allow_html=True)

st.divider()

# --- CAREER JOURNEY ---
st.header("Career Journey")
st.info("Explore my professional journey by clicking on each role to see key achievements.")

with st.expander("Data Analyst — Fraud Strategy & Risk Operations | Walmart (Oct 2025 – Present)"):
    st.write("• Led fraud analytics across **5M+ weekly e-commerce transactions**.")
    st.write("• Designed **reflector ID-based entity aggregation framework** for $10M+ monthly exposure.")
    st.write("• Optimized 400+ fraud rules, contributing to a **20% reduction in rule overlap**.")
    st.write("• Developed standardized fraud classification logic for chargebacks and return abuse.")

with st.expander("Data Analyst — Metaverse Technology | Accenture (May 2022 – Aug 2023)"):
    st.write("• Analyzed 1M+ XR interaction events to map user journeys.")
    st.write("• Built churn-prediction models (Gradient Boosting, Random Forests) to identify high-risk segments.")
    st.write("• Automated workflows in Python/SQL, reducing manual reporting by **8+ hours weekly**.")

with st.expander("Data Scientist | Zeta (Fintech) (May 2020 – April 2022)"):
    st.write("• Mapped end-to-end payment lifecycle (Auth, Capture, Settlement) to identify failure points.")
    st.write("• Built PySpark-based pipelines for millions of transactions.")
    st.write("• Reduced operational and fraud-related anomaly detection latency by **40%**.")

with st.expander("Business Insights Analyst | Byjus (EdTech) (Aug 2016 – May 2020)"):
    st.write("• Identified onboarding drop-off trends for 100K+ users.")
    st.write("• Reduced activation failures by **30%** via SQL validation checks.")
    st.write("• Drove a **10–12% lift** in feature adoption through A/B testing on 10K+ user cohorts.")

st.divider()

# --- DATA-DRIVEN IMPACT ---
st.header("Data-Driven Impact", anchor="impact")
st.write("Quantitative achievements across fraud prevention and operational efficiency.")
impact_data = {
    'Metric': ['Manual Review Target', 'Activation Success', 'Rule Overlap Red.', 'Reporting Efficiency'],
    'Improvement (%)': [50, 30, 20, 40]
}
st.bar_chart(data=impact_data, x='Metric', y='Improvement (%)')

st.divider()

# --- EDUCATION ---
st.header("Education")
st.write("**Clark University** — Master of Science in Information Technology (Data & Project Management)")
st.write("**Kurukshetra University** — Bachelor of Technology (B.Tech)")

st.divider()

# --- FOOTER ---
st.markdown("<h3 style='text-align: center;'>Get In Touch</h3>", unsafe_allow_html=True)
st.columns(3)[1].button("Email Me", use_container_width=True)

st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 Vanshika Choudhary. All Rights Reserved.</p>", unsafe_allow_html=True)
