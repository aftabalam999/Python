from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import client
from schema.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def show(request: Request):
    docs = client.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "_id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"]
        })
    # print(newDocs)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"newDocs": newDocs}
    )

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    title = form["title"]
    desc = form["desc"]
    client.notes.notes.insert_one({"title": title, "desc": desc})
    return {"Success": True}
