from typing import List, Optional
from database import db
import models, schemas

class VideosRepository():
    @staticmethod
    def create(exercise: schemas.ExerciseCreate) -> schemas.ExerciseCreate: # ESTA FUNÇÃO NÃO ASSOCIA O VIDEO AO PT 
        db_exercise = exercise
        db.add(db_exercise)
        db.commit()
        db.refresh(db_exercise)
        return db_exercise
    
    @staticmethod
    def getExercise(exercise_id) -> List[models.Exercise]:    # getExercise -> getVideo
        return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()

    @staticmethod
    def getAllExercises(skip: int = 0, limit: int = 100) -> List[models.Exercise]:
        return db.query(models.Exercise).offset(skip).limit(limit).all()

    @staticmethod
    def getPtExercises(pt_id:str) -> Optional[List[models.Exercise]]:   # getPtExercises -> getPtVideos
        personal_trainer = db.query(models.PersonalTrainer).filter(models.PersonalTrainer.id == pt_id).first()
        return personal_trainer.workouts if personal_trainer else None

    

    @staticmethod
    def getAllRestrictedVideos():
        pass

    @staticmethod
    def getAllVideosFromPt(ptId):
        pass
