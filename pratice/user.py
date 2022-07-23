from fastapi import Body, FastAPI,Depends
from main import app
from sqlalchemy.orm import Session
from database import get_db
import models
from main import Data

@app.get("/all")
def get_all(db: Session = Depends(get_db)):
    address = db.query(models.Address).all()
    return {"message":address}



@app.post("/createaddress")
def create_address(post:Data,db: Session = Depends(get_db)):
    user =  models.Address(user=post.user,address=post.address)    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return{"data":user}

@app.get("/{id}")
def get_id(id:int,db: Session = Depends(get_db)):
    user =db.query(models.Address).filter(models.Address.id==id).first()
    
    if not user:
        return ("user does not exist")
    return{"user_detail": user}




@app.delete("/user/{id}")
def delete_address(id:int,db: Session = Depends(get_db)):
    post_query = db.query(models.Address).filter(models.Address.id==id)

    post = post_query.first()

    if post== None:
        return ("user does not exist")

    post_query.delete(synchronize_session=False)
    db.commit
    db.refresh(post)

    return {'message':'user deleted'}

@app.put("/user/{id}")
def update_address(id:int,user:Data,db: Session = Depends(get_db)):

    post_query = db.query(models.Address).filter(models.Address.id==id)
    post = post_query.first()

    if post ==None:
        return("user does not exist")

    post_query.update(models.Address.dict(),synchronize_session = False)

    db.commit
    db.refresh(post)
    return post
