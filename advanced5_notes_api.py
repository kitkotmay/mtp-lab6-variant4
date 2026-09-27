from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Notes API")


class Note(BaseModel):
    title: str
    content: str


notes = {}
next_id = 1


@app.get("/notes")
def get_notes():
    return notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(
            status_code=404,
            detail="Заметка не найдена",
        )

    return notes[note_id]


@app.post("/notes")
def create_note(note: Note):
    global next_id

    note_data = {
        "id": next_id,
        **note.model_dump(),
    }

    notes[next_id] = note_data
    next_id += 1

    return note_data


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    if note_id not in notes:
        raise HTTPException(
            status_code=404,
            detail="Заметка не найдена",
        )

    note_data = {
        "id": note_id,
        **note.model_dump(),
    }

    notes[note_id] = note_data

    return note_data


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(
            status_code=404,
            detail="Заметка не найдена",
        )

    deleted_note = notes.pop(note_id)

    return {
        "message": "Заметка удалена",
        "note": deleted_note,
    }
