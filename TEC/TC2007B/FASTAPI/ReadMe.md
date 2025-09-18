# FAST API

Tutorial to create an image-based API

1. install

```bash
pip install "fastapi[standard]" python-opencv
```

2. Test _Main.py_

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}

```

3. Launch

```bash
fastapi dev Main.py
```

4. Test response

```bash
curl http://127.0.0.1:8000
```

5. Image processing

```python
from typing import Union
from fastapi import FastAPI
from PIL import Image, ImageDraw
import glob
from fastapi.staticfiles import StaticFiles # local server files

app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name = "static") # mount point to save processed images

def datetimestring():
	now = datetime.datetime.now()
	return now.strftime("%Y_%m_%d_%H_%M_%S")

def InsertBB(File, BB = [20, 20, 150, 150], color = [0,255,0]):
	try:
		I = Image.open("./src/" + File)
		File = "./static/" + File;
	except:
		File = None;
	
	I = I.convert("RGBA");
	J = Image.new("RGBA", I.size, (255,255,255,0));
	draw = ImageDraw.Draw(J);
	color = tuple(color)
	x0, y0, x1, y1 = BB;
	draw.rectangle(((x0, y0), (x1, y1)), fill = None , outline = color, width = 3);	
	J = Image.alpha_composite(I, J);
	J.save(File);
	return File;

@app.get("/")
def read_root():
	Files = glob.glob("*.png")
	return {str(Files)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	item_id = my_func(item_id);
	return {"item_id": item_id, "q": q}
	
	
@app.get("/images/{img_response}")
def read_item(img_response: str, q: Union[str, None] = None):
	URL = InsertBB(img_response);
	return {"img_response": URL, "q": q};
```

6. API call

```bash
url http://127.0.0.1:8000/images/xolo.png
```

Image path

```bash
firefox http://127.0.0.1:8000/static/axolotl.png
```

You should see a bounding box
