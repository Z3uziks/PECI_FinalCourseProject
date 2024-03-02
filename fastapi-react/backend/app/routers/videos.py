from repository.pts import PersonalTrainersRepository
from fastapi import APIRouter, UploadFile, File
from repository.users import UsersRepository
from fastapi.responses import FileResponse
from auth.oauth2_jwt import *
from pathlib import Path
import schemas

VIDEOS_DIR = Path("videos")
router = APIRouter(prefix="/videos")

def is_safe_path(video_name: str) -> bool:
    # basic directory traversal mitigation
    return not (".." in video_name or "\\" in video_name or "/" in video_name)

@router.get("/{video_name}")
async def get_video(token: schemas.TokenData, video_name: str):
    jwt_data = get_jwt_token_data(token=token.token)
    if jwt_data == None:
        return { "result": "no", "error": "Unauthorized." }

    if jwt_data["isNormalUser"] == True:
        user_id: int = UsersRepository.get_user_by_token(token=jwt_data["token"]).id
        if not UsersRepository.hasAccessToVideo(user_id, video_name):
            return { "result": "no", "error": "Unauthorized." }
    else:
        pt_id: int = PersonalTrainersRepository.get_pt_by_token(token=jwt_data["token"]).id
        if not PersonalTrainersRepository.hasAccessToVideo(pt_id, video_name):
            return { "result": "no", "error": "Unauthorized." }

    if not is_safe_path(video_name):
        return { "result": "no", "error": "Video not found." }

    video_path = VIDEOS_DIR / video_name 
    if not video_path.exists():
        return { "result": "no", "error": "Video not found." }

    return FileResponse(video_path)

@router.post("/upload")
async def upload_video(token: schemas.TokenData, video: UploadFile = File(...)):
    jwt_token_data = get_jwt_token_data(token=token.token)
    if jwt_token_data == None:
        return { "result": "no", "error": "Unauthorized." }

    if jwt_token_data["isNormalUser"]:
        return { "result": "no", "error": "Unauthorized." }

    # save the video to disk
    with open(VIDEOS_DIR / video.filename, "wb") as buffer:
        buffer.write(video.file.read())
    
    return { "result": "ok" }

@router.post("/getAccessibleVideos")        
def get_accessible_videos(token: schemas.TokenData):
    jwt_data: Optional[str] = get_jwt_token_data(token=token.token)
    if jwt_data == None:
        return { "result": "no", "error": "Unauthorized." }

    if jwt_data["isNormalUser"] == True:
        user_id: int = UsersRepository.get_user_by_token(token=jwt_data["token"]).id
        if user_id == None:
            return { "result": "no", "error": "Unauthorized." }

        # retrieve the videos that the user has access to
        videos = UsersRepository.getAccessibleVideos(user_id)
    else:
        pt_id: int = PersonalTrainersRepository.get_pt_by_token(token=jwt_data["token"]).id
        if pt_id == None:
            return { "result": "no", "error": "Unauthorized." }

        videos = PersonalTrainersRepository.getAccessibleVideos(pt_id)

    videos = [ {"title": video.videoname, "mainMuscles": video.muscletargets, "thumbnail": video.thumbnail, "releasedate": video.releasedate} for video in videos]
    return { "result": "ok", "videos": videos if videos != None else [] }

@router.post("/getPTPreVideos")
async def get_pt_premium_videos(token: schemas.TokenData):
    jwt_data: Optional[str] = get_jwt_token_data(token=token.token)
    if jwt_data == None:
        return { "result": "no", "error": "Unauthorized." }

    if jwt_data["isNormalUser"] == True:
        user_id: int = UsersRepository.get_user_by_token(token=jwt_data["token"]).id
        #print("user_id",user_id)
        if user_id == None:
            return { "result": "no", "error": "Unauthorized." }

        # retrieve the premium videos that the user has access to
        videos = UsersRepository.getPTVideos(user_id)
    else:
        pt_id: int = PersonalTrainersRepository.get_pt_by_token(token=jwt_data["token"]).id
        if pt_id == None:
            return { "result": "no", "error": "Unauthorized." }

        videos = PersonalTrainersRepository.getPTVideos(pt_id)
    
    # sort the videos by personal trainer id
    videos = sorted(videos, key=lambda video: video.personal_trainer_id)
    #print("videos",videos)
    #print("video.pt_username",videos[0].pt_username)
    
    videos = [ {"title": video.videoname, "mainMuscles": video.muscletargets, "username": video.pt_username ,"releasedate": video.releasedate} for video in videos]
    
    # depois de dar update á db deverá ficar este:
    #videos = [ {"title": video.videoname, "mainMuscles": video.muscletargets, "rating": video.rating, "duration": video.duration, "thumbnail": video.thumbnail, "dificulty": video.dificulty, "releasedate": video.releasedate} for video in videos if video.restricted == 1]


    return { "result": "ok", "videos": videos if videos != None else [] }
    


# @router.post("/getPTvideos")
# async def read_root3():
#     # Retrieve the videos from pt with id '1'
#     pt_id = 1
#     videos = VideosRepository.get_pt_videos(pt_id)
#     print(videos)
#     return videos

# @router.post("/addVideo")  # NÃO ASSOCIA O VIDEO AO PT 
# async def read_root3(videopath,videoname,description,muscletargets,releasedate,restricted=0):
#     video = Video(videopath=videopath,videoname=videoname,description=description,muscletargets=muscletargets,releasedate=releasedate,restricted=restricted)
#     video = VideosRepository.create(video)
#     return video

# @router.post("/getAllVideos")
# async def read_root3():
#     # Retrieve the user with name 'user2' and eagerly load the related PTs
#     videos = VideosRepository.getAllVideos()
#     print(videos)
#     return videos
