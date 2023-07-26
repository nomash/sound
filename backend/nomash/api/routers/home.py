from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get('/', responses={
    status.HTTP_200_OK: {"model": str, "description": "Home Page"},
})
def home():
    return ""