from fastapi import FastAPI, UploadFile, File
import fitz  # PyMuPDF

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    return {"text": text}
