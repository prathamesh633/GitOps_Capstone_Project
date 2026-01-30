import yaml
 
def load_config():
    with open("config/app_config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config
 
if __name__ == "__main__":
    config = load_config()
    print("Application Name:", config["app"]["name"])
    print("Environment:", config["app"]["environment"])