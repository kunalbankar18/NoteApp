from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates=Jinja2Templates(directory='templates')

@note.get('/',response_class=HTMLResponse)
async def home_page(request:Request):
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append(
            {
                'id':doc['_id'],
                'title':doc['title'],
                'content':doc['content'],
                'important':doc['important']
            }
        )
    
    return templates.TemplateResponse('index.html',{'request':request,"newDocs":newDocs})

@note.post('/add_note')
async def add_note(request:Request):
    form = await request.form()
    dict_form = dict(form)
    dict_form['important'] = True if dict_form.get('important') == 'on' else False
    new_note = conn.notes.notes.insert_one(dict_form)
    return {'Success': 'Note added successfully'}