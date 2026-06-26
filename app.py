import os
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
model = joblib.load(MODEL_PATH)


HOME_OWNERSHIP_OPTIONS = ["RENT", "MORTGAGE", "OWN", "OTHER"]
LOAN_INTENT_OPTIONS = ["EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"]
LOAN_GRADE_OPTIONS = ["A", "B", "C", "D", "E", "F", "G"]
DEFAULT_ON_FILE_OPTIONS = ["N", "Y"]

REQUIRED_FIELDS = [
    "person_age",
    "person_income",
    "person_home_ownership",
    "person_emp_length",
    "loan_intent",
    "loan_grade",
    "loan_amnt",
    "loan_int_rate",
    "cb_person_default_on_file",
    "cb_person_cred_hist_length",
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        home_ownership_options=HOME_OWNERSHIP_OPTIONS,
        loan_intent_options=LOAN_INTENT_OPTIONS,
        loan_grade_options=LOAN_GRADE_OPTIONS,
        default_options=DEFAULT_ON_FILE_OPTIONS,
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(silent=True) or {}

    missing = [f for f in REQUIRED_FIELDS if payload.get(f) in (None, "")]
    if missing:
        return jsonify({"error": f"Missing field(s): {', '.join(missing)}"}), 400

    try:
        person_age = float(payload["person_age"])
        person_income = float(payload["person_income"])
        person_home_ownership = str(payload["person_home_ownership"]).upper()
        person_emp_length = float(payload["person_emp_length"])
        loan_intent = str(payload["loan_intent"]).upper()
        loan_grade = str(payload["loan_grade"]).upper()
        loan_amnt = float(payload["loan_amnt"])
        loan_int_rate = float(payload["loan_int_rate"])
        cb_person_default_on_file = str(payload["cb_person_default_on_file"]).upper()
        cb_person_cred_hist_length = float(payload["cb_person_cred_hist_length"])
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter valid numeric values."}), 400

    if person_income <= 0 or loan_amnt <= 0:
        return jsonify({"error": "Income and loan amount must be greater than zero."}), 400

    if person_home_ownership not in HOME_OWNERSHIP_OPTIONS:
        return jsonify({"error": "Invalid home ownership value."}), 400
    if loan_intent not in LOAN_INTENT_OPTIONS:
        return jsonify({"error": "Invalid loan intent value."}), 400
    if loan_grade not in LOAN_GRADE_OPTIONS:
        return jsonify({"error": "Invalid loan grade value."}), 400
    if cb_person_default_on_file not in DEFAULT_ON_FILE_OPTIONS:
        return jsonify({"error": "Invalid default-on-file value."}), 400

    loan_percent_income = loan_amnt / person_income
    income_to_loan = person_income / loan_amnt
    employment_category = "Experienced" if person_emp_length >= 5 else "New"

    row = pd.DataFrame([{
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length,
        "income_to_loan": income_to_loan,
        "employment_category": employment_category,
    }])

    try:
        prediction = int(model.predict(row)[0])
        probabilities = model.predict_proba(row)[0]
    except Exception:
        return jsonify({"error": "The model could not score this application."}), 500

    good_probability = float(probabilities[0]) * 100
    risk_probability = float(probabilities[1]) * 100

    return jsonify({
        "prediction": prediction,
        "label": "Good Credit Risk" if prediction == 0 else "Bad Credit Risk",
        "risk_probability": round(risk_probability, 2),
        "good_probability": round(good_probability, 2),
        "loan_percent_income": round(loan_percent_income * 100, 2),
        "employment_category": employment_category,
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)