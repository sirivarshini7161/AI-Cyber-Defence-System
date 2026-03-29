import streamlit as st
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

from detector import detect_attack
from analyser import risk_score
from response_ai import generate_response

st.set_page_config(page_title="AI Cyber Defence System", layout="wide")

st.title("🛡️ AI Cyber Defence System (SOC Dashboard)")
st.write("Real-time attack detection, analysis, and AI response system")

# Session storage
if "history" not in st.session_state:
    st.session_state.history = []

# INPUT
user_input = st.text_area("Enter network activity / log / message")

if st.button("Analyze Threat"):

    if user_input.strip() == "":
        st.warning("Please enter a log first")

    else:
        log = {"event": user_input}

        # PROCESSING
        attack_type = detect_attack(log)
        score = risk_score(log)
        response = generate_response(attack_type, score)

        # RISK LEVEL
        if score >= 80:
            level = "🔴 CRITICAL"
        elif score >= 50:
            level = "🟡 MEDIUM"
        else:
            level = "🟢 LOW"

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # SAVE HISTORY
        st.session_state.history.append({
            "Time": time_now,
            "Input": user_input,
            "Attack": attack_type,
            "Score": score,
            "Level": level,
            "Response": response
        })

        # OUTPUT UI
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🔍 Detection")
            st.success(attack_type)

        with col2:
            st.subheader("📊 Risk Score")
            st.info(f"{score} ({level})")

        with col3:
            st.subheader("🤖 AI Response")
            st.warning(response)

# ================= HISTORY SECTION =================
st.markdown("---")
st.subheader("📁 Attack History Log")

if len(st.session_state.history) == 0:
    st.info("No attacks detected yet.")

else:
    df = pd.DataFrame(st.session_state.history)

    # TABLE VIEW
    st.dataframe(df)

    # ================= DOWNLOAD CSV =================
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Report (CSV)",
        csv,
        "cyber_attack_report.csv",
        "text/csv"
    )

    # ================= ATTACK FREQUENCY GRAPH =================
    st.subheader("📊 Attack Frequency Analysis")

    chart_data = df["Attack"].value_counts()

    fig, ax = plt.subplots()

    chart_data.plot(kind='bar', ax=ax)

    ax.set_title("Attack Frequency Analysis")
    ax.set_xlabel("Attack Type")
    ax.set_ylabel("Count")

    st.pyplot(fig)