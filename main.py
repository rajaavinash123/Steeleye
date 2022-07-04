from fastapi import FastAPI
from typing import Optional



app=FastAPI()


@app.get('/tradeslist')
def get_all_trades(limit=10):
    return 

@app.get('/tradeslist/{trade_id}')
def get_trade_by_id(trade_id :str):
    return 


@app.get('/tradeslist/{instrument_id}')
def get_all_trades_by_instrument_id(instrument_id : str):
    return 

@app.get('/tradeslist/{instrument_name}')
def get_all_trades_by_instrument_name(instrument_name :str):
    return 

@app.get('/tradeslist/{counterparty}')
def get_all_trades_by_counterparty(counterparty):
    return 

@app.get('/tradeslist/{trader}')
def get_all_trades_by_trader(trader :str):
    return



#if __name__ == "__main__":
  #  uvicorn.run(app,host="127.0.0.1",port=9000)

