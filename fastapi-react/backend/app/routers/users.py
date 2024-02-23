from repository.pts import PersonalTrainersRepository
from repository.subs import SubscriptionsRepository
from repository.users import UsersRepository
from fastapi import APIRouter
from auth.oauth2_jwt import *
from typing import Tuple
from models import User
import schemas

router = APIRouter(prefix="/users")

def check_password_requirements(password: str) -> Tuple[bool, str]:
    special_chars =  ["$", "&", "!"]
    if len(password) < 12 or len(password) > 128:
        return(False, "The password length needs to be in between 12 and 128 characters.")
    elif not any(char.isdigit() for char in password) :
        return(False, "The password needs at least one digit.")
    elif not any(char.isupper() for char in password):
        return(False, "The password needs at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        return(False, "The password needs at least one lowercase letter.")
    elif not any(char in special_chars for char in password):
        return(False, 'The passwords needs at least one of these characters: "$", "&", "!"')
    else: 
        return (True, "")

@router.post("/register")
def register_user(user: schemas.BasicUser, isNormalUser: bool):
    # check for user with same name
    if UsersRepository.get_user_by_username(username=user.username):
        return {"result": "no", "error": "Username already in use."}

    # check for pt with same name
    if PersonalTrainersRepository.get_pt_by_username(username=user.username):
        return {"result": "no", "error": "Username already in use."}

    # check password strength
    passwd_req = check_password_requirements(user.password)
    if passwd_req[0] == False:
        return {"result": "no", "error": passwd_req[1]}

    if isNormalUser:
        # register the user in the database
        new_user = UsersRepository.create(user=user)
        
        # login the new user
        jwt_token: str = UsersRepository.logIn(new_user)
    else:
        new_pt = PersonalTrainersRepository.create(pt=user)

        # login the new user
        jwt_token: str = PersonalTrainersRepository.logIn(new_pt)

    return { "result": "ok", "token": jwt_token }

@router.post("/login")
def login_user(user: schemas.BasicUser):
    # get the user instance with the provided username and password
    user_login = UsersRepository.get_user_by_username_password(**user.model_dump())
    if UsersRepository.get_user_by_username_password(**user.model_dump()):
        # login as a normal user
        jwt_token: str = UsersRepository.logIn(user_login)
        # jwt_token: str = UsersRepository.getJwtToken(user_login)
        return {"result": "ok", "token": jwt_token}

    pt_login = UsersRepository.get_user_by_username_password(**user.model_dump())
    if PersonalTrainersRepository.get_user_by_username_password(**user.model_dump()):
        # login as a pt
        jwt_token = PersonalTrainersRepository.logIn(pt_login)
        return {"result": "ok", "token": jwt_token}

    return {"result": "no", "error": "User does not exist."}

@router.post("/checkAuthentication")
def check_authentication(token: str):
    jwt_token_data = get_jwt_token_data(token=token)
    if jwt_token_data == None:
        return { "result": "no", "error": "Invalid token." }

    if jwt_token_data["isNormalUser"]:
        if UsersRepository.get_user_by_token(token=jwt_token_data["token"]) == None:
            return { "result": "no", "error": "Invalid token." }
    elif PersonalTrainersRepository.get_pt_by_token(token=jwt_token_data["token"]) == None:
            return { "result": "no", "error": "Invalid token." }

    return { "result": "ok" }

# @router.post("/addUserCustom", response_model=schemas.BasicUser)
# async def read_root2(user: schemas.BasicUser):
#     # add a user with name 'user2' and password 'password'
#     new_user = User(**user.model_dump())
#     UsersRepository.create(new_user)
#     return new_user

# @router.post("/add")
# async def read_root2(username,password):
#     # add a user with name 'user3' and password 'password'
#     newUser = User(username=username, password=password)
#     UsersRepository.create(newUser)
#     return newUser

# @router.post("/getAll")
# async def read_root2():
#     users = UsersRepository.get_users()
#     print(users)
#     return users

# @router.post("/getSubs")
# async def read_root3():
#     user_id=2
#     PTs_info = SubscriptionsRepository.get_pts_for_user(user_id)
#     return PTs_info
