from fastapi import UploadFile
from .ImageSaver import ImageSaver


ImageSaver.ensureFolder()


# TODO:send image to frontend
def get_products(db):
    cursor = db.cursor()
    cursor.execute(
        """SELECT
        p.Product_ID,
        p.Name,
        p.Price,
        p.Stock,
        p.Category_ID,
        c.Category_Name
        FROM product p
        JOIN category c
        ON p.Category_ID = c.Category_ID"""
    )
    rows = cursor.fetchall()
    cursor.close()

    return [
        {"Product_ID": row[0],
         "Name": row[1],
         "Price": float(row[2]),
         "Stock": row[3],
         "Category_ID": row[4],
         "Category_Name": row[5]}
        for row in rows]


def get_product(product_id, db):
    cursor = db.cursor()
    sql = "SELECT * FROM Product WHERE Product_ID = %s"
    values = (product_id,)
    cursor.execute(sql, values)

    row = cursor.fetchone()
    cursor.close()
    return [
        {
            "Product_ID": row[0],
            "Name": row[1],
            "Price": float(row[2]),
            "Stock": row[3]
        }
    ]


def create_product(product: dict, db):
    cursor = db.cursor()
    sql = "INSERT INTO product(Name, Price, Stock) VALUES (%s, %s, %s)"
    values = (product["Name"], product["Price"], product["Stock"])

    cursor.execute(sql, values)
    db.commit()

    return {"message": "Success",
            "product": product}


def update_product(product_id: int, product: dict, image: UploadFile, db):
    cursor = db.cursor()
    imageUrl = ImageSaver.saveImage(image.filename, image.file.read())
    sql = """UPDATE product
                SET Name=%s,
                    Price=%s,
                    Stock=%s,
                    Category_ID=%s,
                    image_url=%s
            WHERE Product_ID = %s"""
    values = (
        product["Name"],
        product["Price"],
        product["Stock"],
        product["Category_ID"],
        imageUrl, product_id)

    cursor.execute(sql, values)
    db.commit()

    return {
        "message": "Success",
        "Product": product
           }


def delete_product(product_id: int):
    pass
