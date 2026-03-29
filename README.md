# 🛡️ AI Cyber Defense System (Prototype)

## 📌 Project Description
This project is a simple AI-powered cybersecurity prototype that detects possible cyber attacks like brute force, SQL injection, and DDoS attacks. It then generates an automated response using a rule-based AI system.

##  🏗️ System Architecture

User Input (Logs)
        ↓
Attack Detection Module (detector.py)
        ↓
AI Response Engine (ai_engine.py)
        ↓
Streamlit UI (app.py)
        ↓
Threat Alert & Response
---

## 🚀 Features
- Detects cyber attacks from input logs
- Identifies attack type (Brute Force, SQL Injection, DDoS)
- Generates AI-based response actions
- Simple and interactive Streamlit UI

---

## 🧠 Tech Stack
- Python
- Streamlit
- Rule-based AI logic

---

## 📂 Project Structure
CyberDefensePrototype/
│
├── app.py              # Main Streamlit UI
├── detector.py         # Attack detection logic
├── ai_engine.py        # AI response system
├── requirements.txt    # Dependencies
└── README.md           # Project info

---

## ▶️ How to Run

### Step 1: Install dependencies
            ->pip install -r requirements.txt
### Step 2: Run the Streamlit app
            ->streamlit run app.py
### Step 3: Input logs and see AI responses
            ->Enter log data in the text area and click "Detect Attack"

## 🧪 Example

### Input:
Failed login attempts from IP 192.168.1.1 multiple times

### Output:
Attack Type: Brute Force  
Response: Block IP and alert admin

## 🔮 Future Improvements
- Integrate Machine Learning models
- Real-time network traffic monitoring
- Cloud deployment
- Advanced threat intelligence

## 🌍 Impact
- Helps detect cyber attacks early
- Reduces manual monitoring effort
- Can be extended to enterprise-level systems
