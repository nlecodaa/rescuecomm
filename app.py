from flask import Flask, request, render_template_string
import joblib
import sqlite3
from risk_engine import compute_risk

app = Flask(__name__)

model = joblib.load("rescuecomm_clf.pkl")

conn = sqlite3.connect('rescuecomm.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS alerts
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                category TEXT,
                risk_score INTEGER,
                priority TEXT)''')
conn.commit()
conn.close()

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚨 RescueComm AI Alert System</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 font-sans">
    <div class="max-w-3xl mx-auto mt-12 bg-white shadow-2xl rounded-3xl p-8">
        <h1 class="text-4xl font-extrabold text-center text-red-600 mb-3">🚨 RescueComm</h1>
        <p class="text-center text-gray-600 mb-8">AI-powered Emergency Classification & Prioritization</p>

        <!-- Quick Category Buttons -->
        <div class="grid grid-cols-3 sm:grid-cols-6 gap-4 mb-8 text-white text-sm font-semibold text-center">
            <button onclick="insertText('Fire at location, need fire brigade!')" class="bg-red-600 hover:bg-red-700 rounded-xl p-3">🔥 Fire</button>
            <button onclick="insertText('Robbery in progress near the market!')" class="bg-blue-600 hover:bg-blue-700 rounded-xl p-3">🕵️‍♂️ Robbery</button>
            <button onclick="insertText('Road accident with injuries!')" class="bg-yellow-500 hover:bg-yellow-600 rounded-xl p-3">🚑 Accident</button>
            <button onclick="insertText('Medical emergency, person unconscious!')" class="bg-green-600 hover:bg-green-700 rounded-xl p-3">💉 Medical</button>
            <button onclick="insertText('Flood situation developing in the area!')" class="bg-purple-600 hover:bg-purple-700 rounded-xl p-3">🌊 Disaster</button>
            <button onclick="insertText('Suspicious activity observed!')" class="bg-gray-700 hover:bg-gray-800 rounded-xl p-3">⚙️ Other</button>
        </div>

        <form method="POST" class="space-y-6">
            <textarea id="message" name="message" rows="4"
                      class="w-full p-4 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-red-400"
                      placeholder="Type or select a message describing the emergency..."></textarea>

            <button type="submit"
                    class="w-full bg-red-600 hover:bg-red-700 text-white py-3 rounded-xl font-semibold text-lg shadow-md">
                🚨 Classify & Prioritize
            </button>
        </form>

        {% if result %}
        <div class="mt-10 p-6 bg-green-50 border border-green-300 rounded-2xl text-center shadow">
            <h2 class="text-2xl font-bold text-green-700 mb-3">✅ Alert Processed</h2>
            <p class="text-gray-700"><b>Category:</b> {{result['category']}}</p>
            <p class="text-gray-700"><b>Priority:</b> {{result['priority']}}</p>
            <p class="text-gray-700"><b>Risk Score:</b> {{result['risk_score']}}</p>
            <p class="text-sm text-gray-500 mt-2 italic">Simulated dispatch sent to {{result['category']}} Department</p>
        </div>
        {% endif %}
    </div>

    <script>
        function insertText(example) {
            document.getElementById('message').value = example;
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["message"]
        category = model.predict([text])[0]
        risk_score, priority = compute_risk(text)

        conn = sqlite3.connect('rescuecomm.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO alerts (text, category, risk_score, priority) VALUES (?,?,?,?)",
                    (text, category, risk_score, priority))
        conn.commit()
        conn.close()

        result = {"category": category, "priority": priority, "risk_score": risk_score}

    return render_template_string(TEMPLATE, result=result)


if __name__ == "__main__":
    app.run(debug=True)
