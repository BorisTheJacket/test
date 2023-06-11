from fastapi import FastAPI, status, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, Response
from models import NewUser, AudioFile
import uuid
from db import SessionLocal
import base64


app=FastAPI()


db=SessionLocal()


@app.post('/create-user',
status_code=status.HTTP_201_CREATED)
def add_user(user_name: str):
    new_user=NewUser(
        name = user_name,
        id = str(uuid.uuid1()),
        token = str(uuid.uuid4())
    )

    db.add(new_user)
    db.commit()
    
    json_dict = {'id': new_user.id,
                 'token': new_user.token}

    return JSONResponse(content=json_dict, status_code=status.HTTP_201_CREATED)


@app.post('/user/{user_id}/audio-create', status_code=status.HTTP_201_CREATED)
def add_audio(user_id: str, token: str, audio_file: UploadFile=File(...) ):
    user = db.query(NewUser).get(user_id)

    if user == None :
        raise HTTPException(status_code=404, detail='User not found')
    if user.token != token:
        raise HTTPException(status_code=403, detail='Token not valid')

    code = base64.b64encode(audio_file.file.read())

    temp_file = AudioFile(
        id = str(uuid.uuid1()),
        uid = user_id,
        file = code.decode('ascii')
    )

    db.add(temp_file)
    db.commit()

    return f'http://localhost/record?id={temp_file.id}&user={temp_file.uid}'


@app.get('/record', response_class=Response)
def download_audio(id:str, user: str):
    audio_file = db.query(AudioFile).get(id)

    if audio_file == None:
        raise HTTPException(status_code=404, detail='File not found')
    if audio_file.uid != user:
        raise HTTPException(status_code=404, detail='User not found')
    
    return Response(content=base64.b64decode(bytes(audio_file.file, encoding='ascii')), media_type="audio/mpeg")
