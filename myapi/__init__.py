from typing import Dict, Any
from sanic import Sanic, json
from sanic.config import Config
from configparser import ConfigParser

class IniConfig(Config):
    def __init__(self, *args, path: str, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_parser = ConfigParser()
        self.config_parser.read(path)
        self.apply(self.config_parser['sanic'])

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

def run(testing=False):
    app = Sanic(__name__)
    config_state = None
    if not app.state.is_debug and not testing:
        config_state = "config_prod"
    elif testing:
        config_state = "config_test"
    else:
        config_state = "config_dev"

    @app.before_server_start
    def load_config(app, loop):
        ini_config = IniConfig(path=f"{config_state}.ini")
        app.config.update(ini_config)

    @app.get("/health_check")
    async def health_check(request):
        return json({"health": "ok"})

    return app