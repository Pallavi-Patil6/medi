def suggest_diagnosis(symptoms):
    symptom_db = {
        "fever": "Likely Flu or Viral Infection",
        "cough": "Could be Common Cold or Bronchitis",
        "headache": "Possible Migraine or Stress",
        "fatigue": "Could be Anemia or Thyroid issue"
    }
    diagnosis = []
    for symptom in symptoms:
        for key, value in symptom_db.items():
            if key.lower() in symptom.lower():
                diagnosis.append(value)
    return ', '.join(set(diagnosis)) or "Consult a medical professional"
