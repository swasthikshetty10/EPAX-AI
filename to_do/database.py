import os
import json
import pyrebase

config = json.loads(open("Backend/firebase_config.json","r").read())
#print(config)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

###### FOR NOTES #########
def add_note(id_,title,note):
  db.child("DATA").child(id_).child("NOTES").child(title).set(note)
    
def del_note(id_,title):
  db.child("DATA").child(id_).child("NOTES").child(title).remove()
    
def list_notes(id_):
  notes = db.child("DATA").child(id_).child("NOTES").get().val()
  if notes==None:
    return {}
  else:
    return dict(notes)
    
####### FOR TASKS #########
def add_task(id_,task,done=0):
  db.child("DATA").child(id_).child("TASKS").child(task).set(done)
    
def del_task(id_,task):
  db.child("DATA").child(id_).child("TASKS").child(task).remove()
    
def list_tasks(id_):
  tasks = db.child("DATA").child(id_).child("TASKS").get().val()
  if tasks==None:
    return []
  else:
    return list(tasks.keys()) 
    


#add_note(id_=69420,title="t1",note="lalalala") # add note to id 69420 as lalalala
# add_note(69420,"t2","lululul")
# del_note(69420,"t1")          # delete note of id 69420 at position 0
# print(list_notes(69420))   # list notes of an id

add_task(69420,"some task hdsere",1)
print(list_tasks(69420))
