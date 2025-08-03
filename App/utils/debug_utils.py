import app.config as config

def print_message(message):
    if config.IS_DEBUG:
        print(message)
