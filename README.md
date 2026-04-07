# Desicion-Support-System

A professional web-based dashboard that leverages Machine Learning (Random Forest) to provide real-time decision support for organizational marketing and personal productivity.

🚀 Overview
This project bridges the gap between complex data analysis and actionable insights. It features a dual-mode intelligence engine:

Organisation Mode: Uses a Random Forest Classifier trained on consumer behavior data to predict customer engagement and suggest content optimizations.

Personal Mode: A rule-based decision engine designed to help users prioritize tasks, schedule study hours, and evaluate long-term career paths.

🛠️ Technical Stack
Backend: Python / Flask

Machine Learning: Scikit-Learn (Random Forest Classifier)

Data Handling: Pandas / OpenPyXL

Frontend: HTML5 / Tailwind CSS (Modern Dark UI)

Visualizations: Chart.js (Real-time Feature Distribution)

📊 Model & Performance
The system uses an ensemble learning approach to ensure high prediction stability.

Algorithm: Random Forest Classifier (200 Estimators)

Validation Method: 80/20 Train-Test Split

Key Features: Income, Recency, Web Purchases, Catalog Purchases, Store Purchases, and Web Visits.


Shutterstock
📋 Requirements
Ensure you have Python 3.x installed along with the following libraries:

Bash
pip install flask pandas openpyxl scikit-learn
🏃 Quick Start
Place the marketing_campaign.xlsx dataset in the root directory.

Run the Flask server:

Bash
python app.py
Open your browser and navigate to:

Plaintext
http://127.0.0.1:5000
📂 Project Structure
Plaintext
decision_app/
├── app.py              # Flask Backend & ML Logic
├── marketing_campaign.xlsx # Dataset
├── README.md           # Documentation
└── templates/
    └── index.html      # Frontend Dashboard
📉 Visuals & Metrics
The application provides real-time bar charts showing the "Feature Impact" of the input provided. By analyzing keyword density and historical data, the model determines the likelihood of successful customer response.

🎯 Conclusion
The Nexus Intelligence system demonstrates how Machine Learning can be integrated into a user-friendly web interface to solve real-world problems in marketing efficiency and personal time management.
