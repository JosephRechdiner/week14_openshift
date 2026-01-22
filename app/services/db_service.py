

class SQLService:
    @staticmethod
    def insert_to_db(data, cnx):
        query = """
                INSERT INTO weapons_table (weapon_id, weapon_name, weapon_type, range_km, weight_kg, manufacturer, origin_country, storage_location, year_estimated, risk_level)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
        try:
            with cnx.cursor() as cursor:
                for weapon in data:
                    cursor.execute(query, ( weapon.weapon_id,
                                            weapon.weapon_name,
                                            weapon.weapon_type,
                                            weapon.range_km,
                                            weapon.weight_kg,
                                            weapon.manufacturer,
                                            weapon.origin_country,
                                            weapon.storage_location,
                                            weapon.year_estimated,
                                            weapon.risk_level,
                                            ))
                cnx.commit()
                inserted_count = cursor.rowcount
                return inserted_count
        except Exception as e:
            raise Exception(f"could not insert data into db {str(e)}")