from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import yfinance as yf
app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/stock/{ticker}")
def get_stock_data(ticker:str):
    
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        return {"ticker": ticker, "data": data.to_dict()}
    
    except Exception as e:
        return {"error: str(e)"}
