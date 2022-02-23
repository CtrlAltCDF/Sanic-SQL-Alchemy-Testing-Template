from typing import Dict, Any
from sanic import Sanic, json
from sanic.config import Config
from configparser import ConfigParser

from myapi.routes import load_routes

class IniConfig(Config):
    def __init__(self, *args, path: str, **kwargs):
        super().__init__(*args, **kwargs)
        config_parser = ConfigParser()
        config_parser.read(path)
        self.apply(config_parser['sanic'])

    def apply(self, config):
        self.update(self._to_uppercase(config))

    def _to_uppercase(self, obj: Dict[str, Any]) -> Dict[str, Any]:
        retval: Dict[str, Any] = {}
        for key, value in obj.items():
            upper_key = key.upper()
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

    load_routes(sanic_app)

    @sanic_app.get("/health_check")
    async def health_check(request):
        return json({"health": "ok"})

    return sanic_app