from typing import List, Optional

from fastapi import APIRouter, status

from src.app.models.user import User

router = APIRouter()

users = []

@router.get("/", status_code=status.HTTP_200_OK)
async def get_users() -> List[User]:
    return users

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User) -> User:
    users.append(user)
    return user

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: str) -> Optional[User]:
    for user in users:
        if user.id == user_id:
            return user
    return None

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str) -> None:
    for user in users:
        if user.id == user_id:
            users.remove(user)

@router.put("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user_id: str, new_user: User) -> None:
    print("HERE")
    print(new_user)
    print("HERE")
    for user in users:
        if user.id == user_id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
