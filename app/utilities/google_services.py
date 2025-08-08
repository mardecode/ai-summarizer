import json

from google.cloud import secretmanager


def get_secrets_values(secret_id: str, debug: bool = False) -> dict:
    """
    Reads a secret from Secret Manager.

    Args:
        secret_id (str): The ID of the secret to read.
        debug (bool, optional): Whether to run in debug mode.
        Defaults to False.

    Returns:
        dict: The secrets values as a dictionary.
    """
    if debug:
        #read from a local file
        try:
            with open(f"{secret_id}.json", "r") as file:
                secret_json = json.load(file)
                print(f"Secret {secret_id[:5]}... loaded from local file")
                return secret_json
        except FileNotFoundError as e:
            print(f"Local secret file {secret_id}.json not found, falling back to Secret Manager.")
            raise FileNotFoundError(f"Secret file {secret_id}.json not found in app/utilities/secrets/") from e
            

    client = secretmanager.SecretManagerServiceClient()
    project_id = "373816134831"
    parent = f"projects/{project_id}"
    name = f"{parent}/secrets/{secret_id}/versions/latest"
    try:
        response = client.access_secret_version(name=name)
        secret_data = response.payload.data.decode("UTF-8")
        secret_json = json.loads(secret_data)
        print(f"Secret {secret_id[:5]}... loaded")

        return secret_json
    except Exception as e:
        print(f"Error accessing secret {secret_id}: {str(e)}")
        raise RuntimeError(f"Secret {secret_id} not found in Secret Manager") from e