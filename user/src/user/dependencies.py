from typing import Annotated

from fastapi import Depends, Security

from fastapi_users.manager import BaseUserManager

from fastapi_jwt import JwtAuthorizationCredentials

from src.utils.unitofworks import UnitOfWork
from src.conf import access_security

from .managers import get_user_manager


UserManagerDep = Annotated[BaseUserManager, Depends(get_user_manager)]
JwtAuthCredentials = Annotated[JwtAuthorizationCredentials, Security(access_security)]
UOWDep = Annotated[UnitOfWork, Depends(UnitOfWork)]