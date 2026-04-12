from fastapi import UploadFile
from schema.product import ProductBase, ProductResponse
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


def update_product(product_id: int,
                   product: ProductBase,
                   image: UploadFile, db):

    image_url = "Null"
    cursor = db.cursor()
    if image and image.filename:
        content = image.file.read()
        if content:
            image_url = ImageSaver.saveImage(image.filename, content)

    sql = """UPDATE product
                SET Name=%s,
                    Price=%s,
                    Stock=%s,
                    Category_ID=%s,
                    image_url=%s
            WHERE Product_ID = %s"""

    values = (
        product.name,
        product.price,
        product.stock,
        product.category_id,
        image_url,
        product_id)

    cursor.execute(sql, values)
    db.commit()

    return {
        "message": "Success",
        "Product": ProductResponse(product_id=product_id, **product.model_dump(), image_url=image_url)
           }


def delete_product(product_id: int):
    pass
