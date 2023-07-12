import yaml

def read_yaml(config_path):
    try:
        with open(config_path, "r") as config:
            config_data = yaml.safe_load(config)
        return config_data
    except Exception as e:
        return {"error": str(e)}

config_loader = read_yaml(f"config.yaml")

