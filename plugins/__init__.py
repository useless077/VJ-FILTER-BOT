# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @TamilBots
# Ask Doubt on telegram @TamilSupport

from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
