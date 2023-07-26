from fastapi import APIRouter, HTTPException, status
from uuid import UUID
import logging
from schema.Errors import ErrorResponse

router = APIRouter()

logger: logging.Logger = logging.getLogger(__name__)

@router.get('/', responses={
    status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse, "description": "Not Authorized"},
    status.HTTP_404_NOT_FOUND: {"model": ErrorResponse, "description": "User not found"},
    status.HTTP_200_OK: {"model": str, "description": "A list of tracks"},
    })
def tracks():

    return []

@router.get('/{track_id}', responses={
    status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse, "description": "Not Authorized"},
    status.HTTP_404_NOT_FOUND: {"model": ErrorResponse, "description": "User not found"},
    status.HTTP_200_OK: {"model": str, "description": "A list of tracks"},
    })
def get_track(track_id: UUID):
    

    return {}