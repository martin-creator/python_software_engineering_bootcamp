from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import List,Optional

app = FastAPI()

# Asynchronous programming is a programming paradigm that allows multiple tasks to be executed concurrently, or in parallel.
# It is commonly used in web applications to improve performance and responsiveness.
# Asynchronous programming can be achieved using various techniques, such as callbacks, promises, and coroutines.
# In Python, asynchronous programming is commonly done using the `async` and `await` keywords, which allow functions to be executed asynchronously.
# The difference between a coroutine and a regular function is that a coroutine can be paused and resumed, while a regular function cannot.
# The difference betweene a couroutine and promise is that a coroutine is a function that can be paused and resumed, while a promise is an object that represents the eventual result of an asynchronous operation.



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


async def get_user_info(user_id:str = None)-> (str,str):
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

def create_user(user: User):
    return user.dict()


@app.get("/", response_class=JSONResponse)
def home():
    return {"message": "Hello, World"}

@app.get("/test", response_class=PlainTextResponse)
def test_endpoint():
    return "Mic check 1, 2, 3..."

@app.post("/user", response_model=User)
async def get_user(user: User):
    user =  await get_user_info()
    return user

@app.post("/user/{user_id}/{company_id}", response_model=User)
def get_user_by_id(user_id: int, company_id:int):
    """
    Get the details of a user by user ID and company ID.

    Endpoint: /user/{user_id}/{company_id}
    Method: POST
    Access: Public

    Args:
    - user_id: The ID of the user.
    - company_id: The ID of the company.

    Returns:
    - 201 Created: Item created successfully.
    - 401 Unauthorized: Invalid token provided.

    Example:
    ```
    {
        "user_id": 123,
        "company_id": 456
    }
    ```
    
    """
    print(f'User ID: {user_id} and Company ID: {company_id}')
    # Print documentation of this endpoint
    print(get_user_by_id.__doc__)
    user = get_user_info(user_id)
    return user

@app.post("/user/{user_id}", response_model=User)
async def create_user(user: User):
    """
    Create a new user.

    Endpoint: /user/{user_id}
    Method: POST
    Access: Public

    Args:
    - user_id: The ID of the user.

    Returns:
    - 201 Created: Item created successfully.
    - 401 Unauthorized: Invalid token provided.

    Example:
    ```
    {
        "user_id": 123
    }
    ```

    """
    user = create_user(user)
    return user

@app.get("/users", response_model=List[User])
def get_users_pagination(page:int, limit:int):
    return {"page": page, "limit": limit}


@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "user": user.dict()}

@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    return {"user_id": user_id}

# The difference between post and put is that post is used to create a new resource, while put is used to update an existing resource.
# Patch is used to update a resource with partial data, while put is used to update a resource with full data.


# Pagination
# Pagination is a technique used to divide a large set of data into smaller parts, or pages, to make it easier to manage and navigate.
# It is commonly used in web applications to display a large number of items in a list or table.
# Pagination is often used in combination with sorting and filtering to provide a better user experience.
# Types of pagination include:
# - Offset-based pagination: This method uses an offset and limit to specify the range of items to return.
# - Cursor-based pagination: This method uses a cursor to specify the starting point of the next page of items.
# - Keyset pagination: This method uses a keyset to specify the starting point of the next page of items.

# Example:
from typing import List

def get_users(page: int, limit: int) -> List[User]:
    # Query the database for users
    users = [
        {"name": "John Doe", "age": 25, "email": "marta@", "liked_posts": [1, 2, 3]},
        {"name": "Jane Smith", "age": 30, "email": "jane@", "liked_posts": [4, 5, 6]},
        {"name": "Bob Johnson", "age": 35, "email": "bob@", "liked_posts": [7, 8, 9]},
    ]
    return [User(**user) for user in users]

# Sorting
# Sorting is the process of arranging items in a specific order, such as ascending or descending.
# It is commonly used to organize data in a more meaningful way and make it easier to find and analyze.
# Sorting can be done based on one or more fields, and can be done in ascending or descending order.
# Example:
from typing import List

def sort_users(users: List[User], field: str, order: str) -> List[User]:
    # Sort the users based on the specified field and order
    if order == "asc":
        users.sort(key=lambda user: getattr(user, field))
    else:
        users.sort(key=lambda user: getattr(user, field), reverse=True)
    return users

# Filtering
# Filtering is the process of selecting a subset of items from a larger set based on specific criteria.
# It is commonly used to narrow down the data to only the items that meet certain conditions.
# Filtering can be done based on one or more fields, and can be done using various comparison operators.
# Example:
from typing import List

def filter_users(users: List[User], field: str, value: str) -> List[User]:
    # Filter the users based on the specified field and value
    return [user for user in users if getattr(user, field) == value]

# Combining pagination, sorting, and filtering

# Pagination, sorting, and filtering can be combined to provide a more powerful and flexible way to manage and navigate large sets of data.
# For example, users can be paginated, sorted, and filtered based on various criteria to provide a better user experience.
# Example:
from typing import List

def get_users(page: int, limit: int, sort_field: str, sort_order: str, filter_field: str, filter_value: str) -> List[User]:
    # Query the database for users
    users = [
        {"name": "John Doe", "age": 25, "email": "msdf@", "liked_posts": [1, 2, 3]},
        {"name": "Jane Smith", "age": 30, "email": "jane@", "liked_posts": [4, 5, 6]},
        {"name": "Bob Johnson", "age": 35, "email": "bob@", "liked_posts": [7, 8, 9]},
    ]
    users = [User(**user) for user in users]

    # Sort the users based on the specified field and order
    if sort_field:
        users = sort_users(users, sort_field, sort_order)

    # Filter the users based on the specified field and value
    if filter_field:
        users = filter_users(users, filter_field, filter_value)

    # Paginate the users based on the specified page and limit
    start_index = (page - 1) * limit
    end_index = start_index + limit

    return users[start_index:end_index]

    