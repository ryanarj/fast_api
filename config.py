from configparser import ConfigParser

config = ConfigParser()


def config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items()
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} is not in {filename} file ")
    return db["postgresql"]
