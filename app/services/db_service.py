

class SQLService:
    @staticmethod
    def insert_to_db(data, cnx):
        query = """
                INSERT INTO table_name (weapon_id, weapon_name, weapon_type, range_km, weight_kg, manufacturer, origin_country, storage_location, year_estimated, level_risk)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
        try:
            cursor = cnx.cursor()
            cursor.execute(query, ( data["weapon_id"],
                                    data["weapon_name"],
                                    data["weapon_type"],
                                    data["range_km"],
                                    data["weight_kg"],
                                    data["manufacturer"],
                                    data["origin_country"],
                                    data["storage_location"],
                                    data["year_estimated"],
                                    data["level_risk"],
                                    ))
            cnx.commit()
        except Exception as e:
            raise Exception(f"could not insert data into db {str(e)}")