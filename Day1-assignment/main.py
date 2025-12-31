from fastapi import FastAPI

from app.models.users import UserModel


app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.


@app.post("/users")
async def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return user.id


@app.get("/users")
async def get_all_users():
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=404)
    return result


@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
