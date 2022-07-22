from creativiousUtilities.config import YAMLConfig

config = YAMLConfig("config/default_config.yaml", "config/config.yaml").load()

print("Message 1: " + config['test messages']["message 1"])