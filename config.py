from typing import Optional

from pydantic import BaseSettings


class SettingsLocal(BaseSettings):
    NORMAL_VAR: Optional[str]
    SECRET_VAR: Optional[str]

    class Config:
        env_file = "./.env"
        secrets_dir = "./secrets-in-project"


class SettingsRoot(BaseSettings):
    NORMAL_VAR: Optional[str]
    SECRET_VAR: Optional[str]

    class Config:
        env_file = "/.env"
        secrets_dir = "/secrets-at-root"


if __name__ == '__main__':
    print("--- Pydantic vars from project dir ---")
    cnf_local = SettingsLocal()
    print(f"normal var: {cnf_local.NORMAL_VAR}")
    print(f"secret var: {cnf_local.SECRET_VAR}")
    print()
    print("Contents of the secret in project, read directly:")
    secret_in_project = open(cnf_local.Config.secrets_dir + "/SECRET_VAR").read()
    print(secret_in_project)

    print()

    print("--- Pydantic vars from OS root ---")
    cnf_root = SettingsRoot()
    print(f"normal var: {cnf_root.NORMAL_VAR}")
    print(f"secret var: {cnf_root.SECRET_VAR}")
    print()
    print("Contents of the secret at root dir, read directly:")
    secret_at_root = open(cnf_root.Config.secrets_dir + "/SECRET_VAR").read()
    print(secret_at_root)



