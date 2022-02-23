from distutils.log import debug
import getopt, sys
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

    config = find_arg(["-c", "--config"])
    if config in ["dev", "prod"]:
        if config == "dev":
            app(config).run(debug=True)
        else:
            app(config).run()
    else:
        raise ValueError("Invalid config.")

if __name__ == "__main__":
    main()