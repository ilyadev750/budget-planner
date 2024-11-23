from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated
from jose import jwt, JWTError, JWSError
from passlib.context import CryptContext
from dotenv import load_dotenv
import os


load_dotenv()
oauth2_bearer = HTTPBearer()
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')


def get_current_user(credentials:
                     Annotated[HTTPAuthorizationCredentials,
                               Depends(HTTPBearer())]):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        role: str = payload.get('role')
        if not username or not user_id or not role:
            raise HTTPException(status_code=401, detail="Authorization failed!")
        return {
            'username': username,
            'user_id': user_id,
            'role': role
        }
    except (JWSError, JWTError):
        raise HTTPException(status_code=401, detail="Authorization failed!")