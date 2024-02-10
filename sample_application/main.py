from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import List,Optional

app = FastAPI()



class User(BaseModel):
    username: str = Field(
        alias="name",
        title="Username",
        description="The name of the user",
        max_length=50,
        min_length=3,
        default="John Doe"
    )
    age: int
    email: str
    liked_posts: Optional[List[int]] = Field(
        description="The IDs of the posts that the user has liked",
        min_items=1,
        max_items=10
    )

    class Config:
        max_anystr_length = 50


class FullUserProfile(BaseModel):
    short_bio: str
    long_bio: str


def get_user_info(user_id:str = None)-> (str,str):
    user_content = {
        "name": "John Doe",
        "age": 25,
        "email": "martin@gmail.com",
        "liked_posts": [1,2,3],
        "profile_info": profile_info
    }

    profile_info = {
        "short_bio": "I am a software developer",
        "long_bio": "I am a software developer with 5 years of experience. I have worked on various projects and have experience in a wide range of technologies."
    }

    user = User(**user_content)
    full_user_profile = {
        **user.dict(),
        **profile_info
    }


    return  FullUserProfile(**full_user_profile)



@app.get("/", response_class=JSONResponse)
def home():
    return {"message": "Hello, World"}

@app.get("/test", response_class=PlainTextResponse)
def test_endpoint():
    return "Mic check 1, 2, 3..."

@app.post("/user", response_model=User)
def get_user(user: User):
    user = get_user_info()
    return user

@app.post("/user/{user_id}/{company_id}", response_model=User)
def get_user_by_id(user_id: int, company_id:int):
    print(f'User ID: {user_id} and Company ID: {company_id}')
    user = get_user_info(user_id)
    return user
    