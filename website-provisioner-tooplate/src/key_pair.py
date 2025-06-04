def create_key_pair(ec2_client, key_pair_name):
    key_pair = ec2_client.create_key_pair(KeyName=key_pair_name)
    with open(f"{key_pair_name}.pem", "w") as key_file:
        key_file.write(key_pair['KeyMaterial'])
    return key_pair_name