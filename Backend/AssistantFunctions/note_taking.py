import os
import json
import pyrebase

config = json.loads(open("Backend/firebase_config.json","r").read())
#print(config)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def add_note(id_,title,note):
  db.child("NOTES").child(id_).child(title).set(note)
    
def del_note(id_,title):
  db.child("NOTES").child(id_).child(title).remove()
    
def list_notes(id_):
  notes = db.child("NOTES").child(id_).get().val()
  if notes==None:
    return []
  else:
    return dict(notes)

#add_note(id_=69420,title="t1",note="lalalala") # add note to id 69420 as lalalala
# add_note(69420,"t2","lululul")
# del_note(69420,"t1")          # delete note of id 69420 at position 0
  # list notes of an id