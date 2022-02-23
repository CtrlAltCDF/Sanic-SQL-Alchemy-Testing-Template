import getopt, sys
from sanic import Sanic
from myapi import app


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:", ["config="])
        def find_arg(args: list):
            for arg, val in opts:
                if arg in args:
                    return val
            return False
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    def parse_input(val):
        try:
            return int(val)
        except ValueError:
            if val in ["True", "False"]:
                return True if val == "True" else False

    def return_instance_config(instance: Sanic):
        config = {"debug": False, "port": None, "workers": 0}
        for key in config.keys():
            if key.upper() in instance.config:
                config[key.lower()] = parse_input(instance.config[key.upper()])
        return config

    config = find_arg(["-c", "--config"])
    if config in ["dev", "prod"]:
            instance = app(config)
            instance.run(**return_instance_config(instance))
    else:
        raise ValueError("Invalid config.")

if __name__ == "__main__":
    main()