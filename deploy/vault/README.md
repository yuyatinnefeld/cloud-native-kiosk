# Vault

## deploy Vault Server (Terminal 1)
```bash
# run server
#vault server -config=config.hcl

vault server -dev -dev-root-token-id=yt-root-token


# initialize the vault
export VAULT_ADDR='http://127.0.0.1:8200'

# initiaze unseal keys
vault operator init
export VAULT_TOKEN="hvs.xxxx"
```

## Create and Read Secrets (Terminal 2)
```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN="hvs.xxxx"

python create_secrets.py
```
