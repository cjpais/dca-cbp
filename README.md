# dca-cbp

Needed a quick script to easily Dollar Cost Average on Coinbase Pro.

## Installation

1. Install the required `cbpro` library.

* `pip install -r requirements.txt`

2. Set the following environment variables with your Coinbase Pro API Credentials
 
```bash
export CBPRO_KEY="API_KEY"
export CBPRO_SECRET="SECRET_KEY"
export CBPRO_PASS="PASSPHRASE"
```

3. Set up to run on a repeating basis using cron

* `crontab -e`

* `30 6 * * * /usr/bin/python3 <PATH_TO_DCA_CBP>/buy_dca.py`
