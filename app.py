from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# ==========================================================
# 📊 DATA, MODEL & METRICS LOGIC
# ==========================================================
model_metrics = {"accuracy": "N/A"}

try:
    # 1. Load Data
    df = pd.read_excel("marketing_campaign.xlsx").dropna()
    features = ['Income', 'Recency', 'NumWebPurchases', 'NumCatalogPurchases', 
                'NumStorePurchases', 'NumWebVisitsMonth', 'MntWines', 'MntMeatProducts']
    
    X = df[features]
    y = df['Response']

    # 2. Split Data (80% Train / 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Train the Random Forest Algorithm
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    # 4. Calculate Accuracy
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    model_metrics["accuracy"] = f"{acc * 100:.2f}%"
    
    # --- THIS IS THE BOX THAT WILL POP UP IN CMD ---
    print("\n" + "="*40)
    print("🚀 SYSTEM METRICS LOADED SUCCESSFULLY")
    print(f"📊 MODEL ACCURACY: {model_metrics['accuracy']}")
    print("="*40 + "\n")

except Exception as e:
    print(f"\n❌ ERROR LOADING MODEL: {e}\n")
    model = None

# --- Logic Functions ---
def email_to_features(text):
    return {
        'Income': 50000, 'Recency': len(text) % 100,
        'NumWebPurchases': len(re.findall(r'http', text)),
        'NumCatalogPurchases': text.lower().count("offer"),
        'NumStorePurchases': text.lower().count("buy"),
        'NumWebVisitsMonth': len(text.split()) // 10,
        'MntWines': text.lower().count("premium") * 50,
        'MntMeatProducts': text.lower().count("discount") * 40
    }

def decision_engine(text):
    text = text.lower()
    if "hours" in text and "subject" in text: return "Strategy: Allocate 50% difficult, 30% medium, 20% easy."
    elif "exam" in text and "project" in text: return "Priority: Focus on exam preparation first, then the project."
    elif "ai" in text and "web" in text: return "Growth: Choose AI for long-term depth, Web for immediate income."
    return "Framework: Apply a weighted decision matrix to evaluate this specific goal."

# ==========================================================
# 🌐 WEB ROUTES
# ==========================================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    mode = data.get('mode', '')
    img_count = data.get('images', 0)

    if "Organisation" in mode and model:
        f_dict = email_to_features(text)
        pred = model.predict(pd.DataFrame([f_dict]))[0]
        status = "High Engagement Expected" if pred == 1 else "Low Engagement Expected"
        
        suggestions = []
        if f_dict['NumWebPurchases'] < 2: suggestions.append("Increase URL/Link density.")
        if int(img_count) == 0: suggestions.append("Add visual assets to improve CTR.")
        
        return jsonify({
            "status": status,
            "suggestions": suggestions,
            "chart_data": f_dict,
            "accuracy": model_metrics["accuracy"]
        })
    else:
        result = decision_engine(text)
        return jsonify({"decision": result})

if __name__ == '__main__':
    app.run(debug=True)
