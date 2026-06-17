from flask import Flask, render_template, request
import pickle
import re
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "phishing.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

scan_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = ""
    prediction_class = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        cleaned_url = re.sub(r'^https?://(www\.)?', '', url)

        vector = vectorizer.transform([cleaned_url])
        prediction = model.predict(vector)[0]

        if prediction == "bad":
            prediction_text = "Phishing Threat Detected"
            prediction_class = "phishing"
            label = "Phishing"
        else:
            prediction_text = "Legitimate Website Verified"
            prediction_class = "legit"
            label = "Legitimate"

        scan_history.insert(0, {"url": url, "result": label})

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        prediction_class=prediction_class,
        history=scan_history[:21]
    )

if __name__ == "__main__":
    app.run(debug=True)
