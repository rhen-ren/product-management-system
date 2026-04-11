import mysql.connector


# connect to db
def get_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@zer02woKun",
        database="ecommerce_db")

    try:
        yield db
    finally:
        db.close()
