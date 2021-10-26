from fastapi import APIRouter
from starlette.responses import JSONResponse

from .repository import data

router = APIRouter(
    prefix="/api",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/folders")
async def get_timecodes():
    return JSONResponse({"folders": list(data.folders.keys())})


@router.get("/data/{folder}")
async def get_timecodes(folder: str):
    csv_one = data.get_csv_path_from_folder(folder)
    return JSONResponse(
        {
            "timecodes": data.get_timecodes_data(csv_one),
            "video_path": str((folder + "/video.mp4")),
            "picture_path": str(folder + "/pic.png"),
        }
    )
