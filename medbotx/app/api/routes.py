from fastapi import APIRouter, UploadFile, File
from app.models.patient import PatientInput
from app.services.diagnosis import suggest_diagnosis
from app.services.prescription import generate_prescription
from app.services.ocr import extract_text

router = APIRouter()

@router.post("/analyze/")
def analyze(data: PatientInput):
    diagnosis = suggest_diagnosis(data.symptoms)
    prescription = generate_prescription(data.name, data.age, data.symptoms, diagnosis)
    return {"diagnosis": diagnosis, "prescription": prescription}

@router.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    text = extract_text(await file.read())
    return {"text": text}
