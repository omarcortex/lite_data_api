from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/calculate/")
async def calculate_val(user_val: int=1):
    val_squared = user_val**2
    return { "The square of your value is" : val_squared }

@app.get("/locate")
async def locate():
   url = "http://maps.googleapis.com/maps/api/geocode/json"
   location = "Golden Gate Bridge" # user given
   query_params = { "address" : location } 
   response = requests.get(url, params = query_params)
   response_json = response.json()
   return response_json # assumes correct format

@app.get("/")
async def root():
    return {"message": "Bonjour!"}
