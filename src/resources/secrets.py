from os import environ as env
import config


VALID_SECRETS = ("DISCORD_PUBLIC_KEY", "MONGO_URL")



for secret in VALID_SECRETS:
    globals()[secret] = env.get(secret) or getattr(config, secret, "")
