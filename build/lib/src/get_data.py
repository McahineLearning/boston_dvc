import os
import yaml
import pandas as pd
import argparse
##STAGE 2
def read_params(cconfig_path):
    with open(cconfig_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    print(config)
    data_path = config['data_source']['s3_source']
    df = pd.read_csv(data_path, sep = ",")
    df.drop(columns= "Unnamed: 0", axis = 1, inplace= True)
    print(df.head())
    return df



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(parsed_args.config)
