import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Valuation",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Styling and layout
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global Typography */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #292524;
    }
    
    /* Background styling */
    .stApp {
        background: linear-gradient(180deg, rgba(28, 25, 23, 0.45) 0%, rgba(20, 18, 16, 0.65) 100%),
                    url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=2000&q=80') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }

    /* Transparent Headers */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    footer {
        visibility: hidden !important;
    }

    /* Main Container */
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1260px !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(253, 252, 250, 0.95) !important;
        backdrop-filter: blur(25px) !important;
        border-right: 1.5px solid #E7E2DA !important;
    }

    section[data-testid="stSidebar"] * {
        color: #292524 !important;
    }

    /* Hero Section */
    .hero-container {
        text-align: center;
        margin-bottom: 28px;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(253, 252, 250, 0.22);
        border: 1px solid rgba(253, 252, 250, 0.45);
        color: #FAF8F5;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        padding: 6px 18px;
        border-radius: 50px;
        margin-bottom: 12px;
        backdrop-filter: blur(10px);
    }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #FAF8F5 !important;
        letter-spacing: -0.025em;
        margin: 0;
        line-height: 1.15;
        text-shadow: 0 4px 16px rgba(15, 12, 10, 0.65);
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #E7E2DA !important;
        font-weight: 400;
        margin-top: 8px;
        text-shadow: 0 2px 8px rgba(15, 12, 10, 0.55);
    }

    /* Search Bar Panel */
    div[data-testid="stHorizontalBlock"] {
        background: rgba(253, 252, 250, 0.96) !important;
        backdrop-filter: blur(25px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(25px) saturate(180%) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.95) !important;
        border-radius: 20px !important;
        box-shadow: 0 20px 45px -10px rgba(28, 25, 23, 0.35) !important;
        padding: 18px 24px 14px 24px !important;
        align-items: flex-end !important;
    }

    /* Form Labels */
    label[data-testid="stWidgetLabel"] p, 
    .stSelectbox label, 
    .stNumberInput label {
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.06em !important;
        color: #57534E !important;
        text-transform: uppercase !important;
        margin-bottom: 4px !important;
    }

    /* Form Inputs */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] {
        background-color: #F8F6F2 !important;
        background: #F8F6F2 !important;
        border: 1.5px solid #E2DCD5 !important;
        border-radius: 12px !important;
        box-shadow: none !important;
    }

    div[data-baseweb="select"] span, 
    div[data-baseweb="select"] div {
        color: #292524 !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
    }

    div[data-baseweb="select"] svg {
        fill: #78716C !important;
    }

    div[data-baseweb="input"] input {
        background-color: #F8F6F2 !important;
        color: #292524 !important;
        font-weight: 800 !important;
        font-size: 0.95rem !important;
    }

    div[data-baseweb="input"] button {
        background: #ECE7DF !important;
        color: #292524 !important;
    }

    /* Dropdown Popover */
    div[data-baseweb="popover"], 
    div[data-baseweb="popover"] ul, 
    div[data-baseweb="popover"] li {
        background-color: #FDFBF7 !important;
        color: #292524 !important;
        font-weight: 600 !important;
    }
    
    div[data-baseweb="popover"] li:hover,
    div[data-baseweb="popover"] li[aria-selected="true"] {
        background-color: #F2ECE4 !important;
        color: #A84E34 !important;
    }

    /* Action Button */
    div.stButton > button {
        background: linear-gradient(135deg, #C2654A 0%, #A84E34 100%) !important;
        color: #FAF8F5 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.4rem !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.04em !important;
        box-shadow: 0 8px 22px -4px rgba(168, 78, 52, 0.45) !important;
        transition: all 0.25s ease !important;
        height: 44px !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #A84E34 0%, #8C3E26 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 28px -4px rgba(140, 62, 38, 0.55) !important;
        color: #FFFFFF !important;
    }

    /* Valuation Result Card */
    .val-result-card {
        background: rgba(253, 252, 250, 0.96);
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        border: 1.5px solid rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 20px 45px -10px rgba(28, 25, 23, 0.35);
        padding: 22px 32px;
        margin-top: 22px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 24px;
        flex-wrap: wrap;
        animation: slideDown 0.35s ease-out;
    }

    .val-hero {
        display: flex;
        flex-direction: column;
    }

    .val-tag {
        display: inline-block;
        background: #F4EBE6;
        border: 1.5px solid #E5D5CD;
        color: #8F432D;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 3px 12px;
        border-radius: 50px;
        width: fit-content;
        margin-bottom: 4px;
    }

    .val-price {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1C1917;
        letter-spacing: -0.03em;
        line-height: 1.1;
    }

    .val-stats-group {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }

    .val-stat-pill {
        background: #F5F2EB;
        border: 1.5px solid #E5DFD5;
        border-radius: 12px;
        padding: 10px 16px;
        text-align: center;
        min-width: 120px;
    }

    .val-stat-lbl {
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #78716C;
        margin-bottom: 2px;
    }

    .val-stat-num {
        font-size: 1.1rem;
        font-weight: 800;
        color: #1C1917;
    }

    .val-desc-badge {
        background: #F5F2EB;
        border-radius: 12px;
        padding: 12px 18px;
        color: #44403C;
        font-size: 0.9rem;
        font-weight: 600;
        max-width: 320px;
        line-height: 1.45;
        border: 1.5px solid #E5DFD5;
    }

    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Load cached model and metadata
@st.cache_resource
def load_model():
    data = joblib.load("model.pkl")
    return data["pipeline"], data["localities"], data["flat_types"], data["statuses"]

pipeline, localities, flat_types, statuses = load_model()

# Hero Header
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">🏡 Gurgaon Real Estate Valuation</div>
    <h1 class="hero-title">Find Your Property's Fair Value</h1>
    <p class="hero-subtitle">Accurate price estimation across 107 verified Gurgaon sectors with 89% accuracy</p>
</div>
""", unsafe_allow_html=True)

# Sidebar: Model Architecture
with st.sidebar:
    st.markdown('<div style="font-size:0.75rem; font-weight:700; color:#78716C; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:8px;">Model Architecture</div>', unsafe_allow_html=True)
    sidebar_card = (
        '<div style="background: #F8F6F2; padding: 18px; border-radius: 16px; border: 1.5px solid #E2DCD5; margin-bottom: 16px; box-shadow: 0 4px 12px rgba(28,25,23,0.03);">'
        '<div style="font-size:0.75rem; color:#78716C; text-transform:uppercase; letter-spacing:0.06em; font-weight:700;">Algorithm</div>'
        '<div style="font-size:1.15rem; font-weight:800; color:#1C1917; margin-bottom:12px;">Random Forest Regressor</div>'
        '<div style="display:flex; justify-content:space-between; margin-bottom:8px; border-top: 1.5px solid #E2DCD5; padding-top:10px;">'
        '<span style="font-size:0.85rem; color:#78716C; font-weight:600;">R² Score</span>'
        '<span style="font-size:0.95rem; font-weight:800; color:#1C1917;">~89%</span>'
        '</div>'
        '<div style="display:flex; justify-content:space-between; margin-bottom:8px;">'
        '<span style="font-size:0.85rem; color:#78716C; font-weight:600;">MAE (Accuracy)</span>'
        '<span style="font-size:0.95rem; font-weight:800; color:#A84E34;">± ₹0.48 Cr</span>'
        '</div>'
        '<div style="display:flex; justify-content:space-between;">'
        '<span style="font-size:0.85rem; color:#78716C; font-weight:600;">Training Set</span>'
        '<span style="font-size:0.95rem; font-weight:800; color:#1C1917;">17,800+ homes</span>'
        '</div>'
        '</div>'
    )
    st.markdown(sidebar_card, unsafe_allow_html=True)
    st.caption("Trained on 17,800+ real estate transactions across Gurgaon.")

# Horizontal input bar
c_loc, c_type, c_bhk, c_area, c_status, c_btn = st.columns([1.5, 1.1, 0.8, 0.9, 1.0, 1.1], gap="small")

with c_loc:
    default_locality_idx = localities.index("Sector 65") if "Sector 65" in localities else 0
    locality = st.selectbox(
        "Location / Sector",
        options=localities,
        index=default_locality_idx,
        help="Select Gurgaon Sector"
    )

with c_type:
    flat_type = st.selectbox(
        "Property Type",
        options=flat_types,
        help="Apartment, Floor, Plot"
    )

with c_bhk:
    bhk = st.selectbox(
        "Bedrooms",
        options=[1, 2, 3, 4, 5, 6],
        index=2,
        format_func=lambda x: f"{x} BHK",
        help="Number of bedrooms"
    )

with c_area:
    area = st.number_input(
        "Area (sq.ft.)",
        min_value=300,
        max_value=10000,
        value=1800,
        step=50,
        help="Built-up Area in sq.ft."
    )

with c_status:
    status = st.selectbox(
        "Status",
        options=statuses,
        help="Construction status"
    )

with c_btn:
    st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
    predict_btn = st.button("Estimate Price", use_container_width=True)

# Display valuation output
if predict_btn:
    input_data = pd.DataFrame(
        [[locality, bhk, area, flat_type, status]],
        columns=["Locality", "BHK_Count", "Area", "Flat Type", "Status"]
    )
    
    try:
        predicted_cr = float(pipeline.predict(input_data)[0])
        predicted_cr = max(0.15, round(predicted_cr, 2))
        
        # Financial metrics
        total_inr = predicted_cr * 10000000
        predicted_lakhs = round(total_inr / 100000)
        rate_per_sqft = round(total_inr / area)
        
        lower_bound = max(0.15, round(predicted_cr - 0.48, 2))
        upper_bound = round(predicted_cr + 0.48, 2)
        
        # Result card HTML
        result_html = (
            '<div class="val-result-card">'
            '<div class="val-hero">'
            '<span class="val-tag">Estimated Fair Value</span>'
            f'<div class="val-price">₹{predicted_cr:.2f} Cr</div>'
            '</div>'
            '<div class="val-stats-group">'
            '<div class="val-stat-pill">'
            '<div class="val-stat-lbl">In Lakhs</div>'
            f'<div class="val-stat-num">₹{predicted_lakhs:,} L</div>'
            '</div>'
            '<div class="val-stat-pill">'
            '<div class="val-stat-lbl">Rate / Sq. Ft.</div>'
            f'<div class="val-stat-num">₹{rate_per_sqft:,}</div>'
            '</div>'
            '<div class="val-stat-pill">'
            '<div class="val-stat-lbl">Market Band (±MAE)</div>'
            f'<div class="val-stat-num">₹{lower_bound:.2f} - ₹{upper_bound:.2f} Cr</div>'
            '</div>'
            '</div>'
            '<div class="val-desc-badge">'
            f'Fair valuation for a <strong>{bhk} BHK {flat_type}</strong> ({area:,} sq.ft.) in <strong>{locality}</strong> ({status}).'
            '</div>'
            '</div>'
        )
        st.markdown(result_html, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error calculating valuation: {e}")
