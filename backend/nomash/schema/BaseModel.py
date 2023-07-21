from pydantic import BaseModel as PydanticBaseModel
from datetime import datetime
from api.helpers import encoders


class BaseModel(PydanticBaseModel):
    class Config:
        populate_by_name = True
