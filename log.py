import rpgframe


def Log(x):
    if rpgframe.settings.debug:
        print(f"Log: {x}")