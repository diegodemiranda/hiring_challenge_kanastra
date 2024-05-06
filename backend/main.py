import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

load_dotenv()

app = FastAPI()

# Configuração do CORS para esse domínio
origins = [
    os.getenv("FRONTEND_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="frontend/build", html=True))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <h1>Hello, Kanastra!</h1>
    <form action="/charges" method="post">
      <label for="name">Name:</label><br>
      <input type="text" id="name" name="name"><br>
      <label for="governmentId">Government ID:</label><br>
      <input type="text" id="governmentId" name="governmentId"><br>
      <label for="email">Email:</label><br>
      <input type="text" id="email" name="email"><br>
      <label for="debtAmount">Debt Amount:</label><br>
      <input type="text" id="debtAmount" name="debtAmount"><br>
      <label for="debtDueDate">Debt Due Date:</label><br>
      <input type="text" id="debtDueDate" name="debtDueDate"><br>
      <input type="submit" value="Create a Charge" />
    </form>
    """
    return HTMLResponse(content=html_content)


@app.post("/charges")
def create_charge(name: str = Form(...), governmentId: str = Form(...), email: str = Form(...), debtAmount:
float = Form(...), debtDueDate: str = Form(...), db: Session = Depends(get_db)):
    try:
        debtDueDate = datetime.strptime(debtDueDate, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid date format. Expected format: YYYY-MM-DD")
    charge = schemas.ChargeCreate(name=name, governmentId=governmentId, email=email, debtAmount=debtAmount,
                                  debtDueDate=debtDueDate)
    print(f"Received charge data: {charge.dict()}")
    db_charge = crud.create_charge(db, charge)
    return jsonable_encoder(db_charge)


# Executa a API com Uvicorn.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
