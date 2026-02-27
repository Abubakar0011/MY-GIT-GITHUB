from fast_appi import FastAppi

app = FastAppi()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None): 
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    app.run()   
    