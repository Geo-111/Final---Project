from fastapi import FastAPI, BackgroundTasks
from myauto import mycol, get_data

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/api/product/")  # /api/product/?page=5 მაგალიტად
def post_car(page: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(get_data, page)
    return {"message": "running in background"}


@app.get("/api/product/")
def get_car(car_id: int):
    mycol_filter = {"car_id": car_id}
    car = mycol.find_one(mycol_filter, {"_id": 0})
    return {"car": car}


@app.put("/api/product/")
def put_car(car_id: int, data: dict):
    mycol_filter = {"car_id": car_id}
    mycol_values = {"$set": data}
    mycol.update_one(mycol_filter, mycol_values)
    return {"message": "car updated"}


@app.get("/api/appraisal/")
def get_appraisal(year: int):
    mycol_filter = {"prod_year": year}
    result = mycol.find(mycol_filter)
    car_price = []
    for item in result:
        car_price.append(item["price_usd"])
    car_count = len(car_price)
    car_total = sum(car_price)
    if car_count != 0:
        car_average = car_total / car_count
    else:
        car_average = 0
    return {
        "manufacture_year": year,
        "total_cars": car_count,
        "total_usd": car_total,
        "average_price": round(car_average),
        "price": car_price,
    }
