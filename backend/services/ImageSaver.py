import os


class ImageSaver():
    folder = "backend/ProductImages"

    @staticmethod
    def ensureFolder():
        os.makedirs(ImageSaver.folder, exist_ok=True)

    @staticmethod
    def saveImage(imageName: str, image: bytes):
        if imageName:
            filePath = os.path.join(ImageSaver.folder, imageName)
            filePath = os.path.normpath(filePath)
            with open(filePath, "wb") as f:
                f.write(image)

        else:
            filePath = "Null"
        return filePath
