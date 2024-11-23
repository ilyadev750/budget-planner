from fastapi import APIRouter, Depends, HTTPException
from repositories.users import UserRepository
from services.token import TokenService
from api.v1.dependencies import get_token_service
from schemas.token import TokenBase
from schemas.users import CreateUserBase
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from dotenv import load_dotenv
import os


# Добавить валидацию электронной почты!
load_dotenv()
base_prefix = os.environ.get('API_V1_STR')
router = APIRouter(prefix=f'{base_prefix}/auth', tags=['Пользователи'])


@router.post("/create-user")
async def create_user(create_user_request: CreateUserBase):
    create_user_dict = create_user_request.model_dump()
    await UserRepository().create_user(data=create_user_dict)
    return {'Успех!': 'Новый пользователь успешно создан!'}


@router.post("/login", response_model=TokenBase)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    token_service: Annotated[TokenService, Depends(get_token_service)]
        ):

    user = await UserRepository().authenticate_user(
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=401, detail="Authorization failed!")

    token = await token_service.create_access_token(obj=user)

    return {'access_token': token,
            'token_type': 'Bearer'}
