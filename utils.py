import yaml
import tiktoken

def read_yaml(config_path):
    try:
        with open(config_path, "r") as config:
            config_data = yaml.safe_load(config)
        return config_data
    except Exception as e:
        return {"error": str(e)}

def tiktoken_len( text):
    tiktoken.encoding_for_model(config_loader["tiktoken_model"])
    tokenizer = tiktoken.get_encoding(config_loader["tiktoken_embeddings"])
    tokens = tokenizer.encode(text, disallowed_special=())
    return len(tokens)

config_loader = read_yaml(f"config.yaml")
