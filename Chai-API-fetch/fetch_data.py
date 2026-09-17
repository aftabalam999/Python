import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def fetchData():
    url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
    if data["statusCode"] == 200 and data["data"]["data"] != []:
        return {"data": data["data"]}
    else:
        return {"data": []}

allData = fetchData()
@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    print(allData["data"]["data"][0]["name"]["first"])
    return templates.TemplateResponse(name="index.html", request=request,
        context={"allData": allData})