# My-Auto-Project
web scraping json python,fastapi,pymongo

## Start here
Download and copy project to folder  
Open terminal in project folder you copied.  
Run code:  
### 1)
```
pip install -r req.txt
```
### 2)
You need to install mongoDB on you local computer  
Or you could use mongoDB Atlas  
Incase your local enviroment, dont change in `myauto.py`
```python
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
```  
Incase mongoDB Atlas change in `myauto.py` this  `mongodb://127.0.0.1:27017/` to your mongoDB Atlas URI
  
### 3)
After run from project folder in terminal
```bash
uvicorn main:app --reload
```
API url will be in console

## API usage
### [GET] : /api/product/
Usage: `http://127.0.0.1:8000/api/product/?car_id=98849751`  

Parameter: `car_id`, 

Value: `98849751`  

Response:  
```json
{
    "car": {
        "car_id": 98849751,
        "prod_year": 2010,
        "price_usd": 6000,
    }
}
```

### [POST] : /api/product/
Usage: `http://127.0.0.1:8000/api/product/?page=10`

Parameter: `page`,

Value: `10`  

Response:  
```json
{"message": "running in background"}
```

### [PUT] : /api/product/
Usage: `http://127.0.0.1:8000/api/product/?car_id=98849751`

Parameter 1 : `car_id`,  
Value 1: `98849751`  
  
## NOTE: Data must be in request body in JSON, example for data : 

Parameter 2 : `data`  
Value 2: 
 ```json
{"prod_year": 2010, "price_usd": 6000,}
``` 
Response:  
```json
{"message": "car updated"}
```

### [GET] : /api/appraisal/
Usage: `http://127.0.0.1:8000/api/appraisal/?year=2010`

Parameter 1 : `year`,  
Value 1: `2010`  
  

Response:  
```json
{
    "manufacture_year": 2023,
    "total_cars": 14,
    "total_usd": 766599,
    "average_price": 54757,
    "price": [
        97900,
        42999,
        58000,
        42500,
        67000,
        52500,
        42500,
        85000,
        36000,
        36000,
        22500,
        19900,
        129900,
        33900
    ]
}
```
