from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from mosreg import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/")


def get_current_user(data:str = Depends(oauth2_scheme)):

    print(data, 1111)
    print(oauth2_scheme, 1111)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
        
    return token.verify_token(data, credentials_exception)

