from typing import Optional, Tuple, Any, List
from schema.BaseModel import BaseModel
import logging

#
#   Using ErrorMessages:
#
#   if bad_thing:
#       raise OrderException(ErrorMessages('ORD0008',(5)))
#
#   The ErrorMessages class returns an instance of ErrorMessage that contains the code and 
#   formatted error message. The HTTP exception handler in main.py will check to see if the object
#   pass in is an ErrorMessage, and if so, will include the error code in the HTTP response. The 
#   ErrorMessage class overrides the __str__ method, so calling str(ErrorMessage) returns the error
#   message text.
#

logger: logging.Logger = logging.getLogger(__name__)


class ErrorResponse(BaseModel):
    message: str


class HTTPErrorResponse(BaseModel):
    message: str
    code: Optional[str]
    params: Optional[List[Any]]


class ErrorMessages(BaseModel):
    pass


class ErrorMessage(BaseModel):
    code: str
    message: str
    template: str
    params: Optional[List[Any]]

    def __str__(self) -> str:
        return self.message
