
from image_reciever.server import ServerConfig, get_server


if __name__ == '__main__':
    import uvicorn
    import argparse

    myport = 8080
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port', '-P', type=int, default=myport, help='port for http server'
    )
    args = parser.parse_args()
    print("port: ", args.port)
    
    cfg = ServerConfig.from_defaults(
        "image-reciever",
        "v0.0.1",
        args.port
    )
    server = get_server(cfg)
    uvicorn.run(
        server,
        host="0.0.0.0",
        port=args.port
    )