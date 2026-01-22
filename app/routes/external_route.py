from io import BytesIO
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
import pandas as pd
from db.connector import SQLManager
from services.data_service import DataAnalizer
from services.db_service import SQLService
from models.schemas import Weapon

external_router = APIRouter()
manager = SQLManager()

# DEPENDENCIES
def get_cnx():
    return manager.get_cnx()


@external_router.post("/upload")
def upload_file(file: UploadFile = File(...), cnx = Depends(get_cnx)):
    # INIT DB
    try:
        manager.init_db()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Could not init db: {str(e)}")

    # CONVERT FILE TO DF
    try:
        contents = file.file.read()
        data = BytesIO(contents)
        df = pd.read_csv(data)
        data.close()
        file.file.close()
    except Exception as e:
        raise HTTPException(status_code=402, detail=f"Could not read csv file: {str(e)}")

    # ANALIZING DF
    df = DataAnalizer.remove_null(df)
    df = DataAnalizer.claculate_risk_level(df)

    # CONVERT DF TO PYTHON LIST OF DICTS
    data = df.to_dict('records')

    # VALIDATE PYDANTIC TYPES
    valid_weapons = []
    for weapon in data:
        new_weapon = Weapon(
                weapon_id=weapon["weapon_id"],
                weapon_name=weapon["weapon_name"],
                weapon_type=weapon["weapon_type"],
                range_km=weapon["range_km"],
                weight_kg=weapon["weight_kg"],
                manufacturer=weapon["manufacturer"],
                origin_country=weapon["origin_country"],
                storage_location=weapon["storage_location"],
                year_estimated=weapon["year_estimated"],
                risk_level=weapon["risk_level"]
        )
        valid_weapons.append(new_weapon)

    # INSERTING TO DB
    try:
        inserted_count = SQLService.insert_to_db(valid_weapons, cnx)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"Could not insert to db: {str(e)}")

    return {
        "status": "succes",
        "inserted_records": inserted_count
        }