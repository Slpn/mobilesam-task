from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image, UnidentifiedImageError
import io

from main import segment_everything

app = FastAPI()

@app.post("/segment-image")
async def segment_image(file: UploadFile = File(...)):
    
    try:
        image_data = await file.read()

        image_convert_byte = Image.open(io.BytesIO(image_data))
        image = image_convert_byte.convert("RGB")

        segmentation_result = segment_everything(image)

        img_segmented = io.BytesIO()
        segmentation_result.save(img_segmented, format="PNG")
        img_segmented = img_segmented.getvalue()
        
        return JSONResponse(content=img_segmented, media_type="image/png")
    
    except UnidentifiedImageError:
        return JSONResponse(content={"error": "Only JPEG/PNG/JPG images are supported"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
