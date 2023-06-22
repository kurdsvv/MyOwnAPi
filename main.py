from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from app.xvideos import Xvideos
from app.pornHub import PornHub
import json
from app.spankbang import Spankbang
app = FastAPI()




@app.get("/xvideos/{file_path:path}", response_class=PlainTextResponse)
async def read_user(file_path: str):
    file_path = "https://www.xvideos.com/" + file_path
    m3u8 = Xvideos(file_path).get_video()
    return m3u8

@app.get("/pornhub/{file_path:path}",response_class=PlainTextResponse)
async def read_user(file_path: str):
    file_path = "https://cn.pornhub.com/view_video.php?viewkey=" + file_path
    urls = json.loads(PornHub(file_path).get_video())
    if len((urls["quality"][3])) != 0:
        return (urls["quality"][3]["videoUrl"])
    elif ((len((urls["quality"][3])) == 0 )& (len((urls["quality"][2]))!=0)):
        return (urls["quality"][2]["videoUrl"])
    else:
        return (urls["quality"][1]["videoUrl"])


@app.get("/Spankbang/{file_path:path}",response_class=PlainTextResponse)
async def read_user(file_path: str):
    file_path = "https://spankbang.com/" + file_path
    m3u8=Spankbang(file_path).get_video()
    return m3u8