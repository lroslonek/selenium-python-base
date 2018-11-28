import yaml


def read_configuration(key):
    with open("../configuration/config.yaml", 'r') as yamlfile:
        all_conf = yaml.load(yamlfile)
        return all_conf[key]
