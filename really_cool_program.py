
aws_config = {
    "default": {
        "aws_access_key_id": "redacting this",
        "aws_secret_access_key": "security team told me to redact this",
        "output": "json",
        "region": "us-east-2"
    }
}


def write_aws_config(config: dict, filepath: str):
    with open(filepath, "w") as f:
        for profile, settings in config.items():
            f.write(f"[{profile}]\n")
            for key, value in settings.items():
                f.write(f"{key} = {value}\n")
            f.write("\n")

write_aws_config(aws_config, "credentials")  # or ~/.aws/credentials
