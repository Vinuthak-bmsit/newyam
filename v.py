import yaml

# Load the YAML configuration file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Accessing the configuration values
program_name = config["program"]["name"]
input_file = config["parameters"]["input_file"]
enable_feature = config["options"]["enable_feature"]

print(f"Program Name: {program_name}")
print(f"Input File: {input_file}")
print(f"Feature Enabled: {enable_feature}")
