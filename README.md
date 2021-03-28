# dca-cbp

Needed a quick script to easily Dollar Cost Average on Coinbase Pro

I am running this script everyday at 6:30AM with the cron 

`30 6 * * * /usr/bin/python3 <PATH_TO_DCA_CBP>/buy_dca.py`

Note you will want to set the following environment variables with your Coinbase Pro API Credentials

```bash
export CBPRO_KEY="API_KEY"
export CBPRO_SECRET="SECRET_KEY"
export CBPRO_PASS="PASSPHRASE"
```
