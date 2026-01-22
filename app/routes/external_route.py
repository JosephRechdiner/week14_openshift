from io import BytesIO
from fastapi import APIRouter, Depends, File, UploadFile
import pandas as pd
from db.connector import SQLManager
from services.data_service import DataAnalizer
from services.db_service import SQLService

external_router = APIRouter()
manager = SQLManager()

# DEPENDENCIES
def get_cnx():
    return manager.get_cnx()


@external_router.post("/upload")
def upload_file(file: UploadFile = File(...), cnx = Depends(get_cnx)):
    # INIT DB
    manager.init_db()

    # CONVERT FILE TO DF
    contents = file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)
    data.close()
    file.file.close()

    # ANALIZING DF
    df = DataAnalizer.remove_null(df)
    df = DataAnalizer.claculate_risk_level(df)

    # CONVERT DF TO PYTHON LIST OF DICTS
    data = df.to_dict()

    # INSERTING TO DB
    inserted_count = SQLService.insert_to_db(data)

    return {
        "status": "succes",
        "inserted_records": inserted_count
        }