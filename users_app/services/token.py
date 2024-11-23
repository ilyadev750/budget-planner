from repositories.base_repository import TokenRepository
from datetime import timedelta, datetime, timezone
from dotenv import load_dotenv
from jose import jwt
import os


load_dotenv()


class TokenService(TokenRepository):
    expires_time = timedelta(minutes=90)
    secret_key = os.environ.get('SECRET_KEY')
    algorithm = os.environ.get('ALGORITHM')

    async def create_access_token(self, obj: object):
        encode = {'sub': obj.username,
                  'id': obj.id,
                  'role': obj.role}
        expires = datetime.now(timezone.utc) + self.expires_time
        encode.update({'exp': expires})
        return jwt.encode(encode, self.secret_key, algorithm=self.algorithm)
