import toml
import os
import simplematrixbotlib as botlib
import matrixmatrixbridge as mmb


def main() -> None:
    config_path = os.environ.get("CONFIG_PATH", "config.toml")
    try:
        with open(config_path, "r") as f:
            config = toml.loads(f.read())
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
        return

    homeserver=config["homeserver"]
    username=config["username"]
    try:
        password=config["password"]
        access_token = ""
    except:
        password = ""
        access_token=config["access_token"]

    creds = botlib.Creds(homeserver, username, password, access_token=access_token)
    bot = botlib.Bot(creds)
    mmb.setup_handlers(bot, config)
    bot.run()

if __name__ == "__main__":
    main()
