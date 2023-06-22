from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from app.xvideos import Xvideos
from app.pornHub import PornHub
import json
from app.spankbang import Spankbang
from app.vjav import Vjav
from fastapi.responses import RedirectResponse
app = FastAPI()



@app.get("/xvideos/{file_path:path}", response_class=PlainTextResponse)
async def read_user(file_path: str):
    file_path = "https://www.xvideos.com/" + file_path
    m3u8 = Xvideos(file_path).GetVideo()
    return RedirectResponse(m3u8)

@app.get("/pornhub/{file_path:path}",response_class=PlainTextResponse)
async def read_user(file_path: str):
    file_path = "https://cn.pornhub.com/view_video.php?viewkey=" + file_path
    urls = json.loads(PornHub(file_path).GetVideo())
    if len((urls["quality"][3])) != 0:
        return RedirectResponse(urls["quality"][3]["videoUrl"])
    elif ((len((urls["quality"][3])) == 0 )& (len((urls["quality"][2]))!=0)):
        return RedirectResponse(urls["quality"][2]["videoUrl"])
    else:
        return RedirectResponse(urls["quality"][1]["videoUrl"])


@app.get("/spankbang/{file_path:path}",)
async def read_user(file_path: str):
    file_path = "https://spankbang.com/" + file_path
    m3u8=Spankbang(file_path).GetVideo()
    return RedirectResponse(m3u8)


@app.get("/vjav/{file_path:path}",)
async def read_user(file_path: str):
    file_path = "https://vjav.com/videos/" + file_path
    m3u8=Vjav(file_path).GetVideo()
    return RedirectResponse(m3u8)