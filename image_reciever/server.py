
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import shutil
from dataclasses import dataclass


@dataclass
class ServerConfig:
    name: str
    version: str
    port: int
    
    @classmethod
    def from_defaults(
        cls,
        name: str,
        version: str,
        port: int
    ) -> 'ServerConfig':
        return cls(
            name, version, port
        )



def get_server(cfg: ServerConfig) -> FastAPI:
    app = FastAPI()

    @app.get("/")
    async def main():
        content = """
    <body>
    <form action="/uploadfile/" enctype="multipart/form-data" method="post">
    <input name="file" type="file">
    <input type="submit">
    </form>
    </body>
        """
        return HTMLResponse(content=content)

    @app.post("/uploadfile/")
    async def create_upload_file(file: UploadFile = File(...)):
        # with open(f"uploaded_images/{file.filename}", "wb") as buffer:
        #     shutil.copyfileobj(file.file, buffer)
        return dict(
            filename=file.filename,
            status="OK"
        )


    return app