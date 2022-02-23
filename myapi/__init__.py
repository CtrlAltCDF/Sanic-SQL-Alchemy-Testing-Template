from curses import echo
from typing import Dict, Any
from sanic import Sanic, json
from sanic.config import Config
from configparser import ConfigParser
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from contextvars import ContextVar
from sqlalchemy.orm import sessionmaker

from myapi.models import BaseModel, list_all_models


class IniConfig(Config):
    def __init__(self, *args, path: str, **kwargs):
        super().__init__(*args, **kwargs)
        config_parser = ConfigParser()
        config_parser.read(path)
        self.apply(config_parser['sanic'])
        self.apply(config_parser['alembic'])

    def apply(self, config):
        self.update(self._to_uppercase(config))

    def _to_uppercase(self, obj: Dict[str, Any]) -> Dict[str, Any]:
        retval: Dict[str, Any] = {}
        for key, value in obj.items():
            upper_key = key.upper().replace('.', "_")
            if isinstance(value, list):
                retval[upper_key] = [
                    self._to_uppercase(item) for item in value
                ]
            elif isinstance(value, dict):
                retval[upper_key] = self._to_uppercase(value)
            else:
                retval[upper_key] = value
        return retval

def app(config=None):
    ini_config = IniConfig(path=f"config_{config}.ini")
    sanic_app = Sanic(ini_config.APP_NAME, config=ini_config)

    _base_model_session_ctx = ContextVar("session")
    bind = create_async_engine(ini_config["SQLALCHEMY_URL"], echo=True)

    if config == "test":
        for model in list_all_models():
            model.metadata.create_all(bind)

    @sanic_app.on_request
    async def inject_session(request):
        request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
        request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)

    @sanic_app.on_response
    async def close_session(request, response):
        if hasattr(request.ctx, "session_ctx_token"):
            _base_model_session_ctx.reset(request.ctx.session_ctx_token)
            await request.ctx.session.close()

    from myapi.routes import people


    @sanic_app.get("/health_check")
    async def health_check(request):
        return json({"health": "ok"})

    return sanic_app