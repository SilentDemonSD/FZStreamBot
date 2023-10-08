from aiohttp.web import Application
from FZStream.core.server.stream_routes import routes

async def initiate_server():
    return Application(client_max_size=30000000).add_routes(routes)
