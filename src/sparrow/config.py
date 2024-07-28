from pmodules import *
def make_sparrow_config():

    global sparrow_config1, sparrow_config2, sparrow_config3

    sparrow_config1 = """{
    "mode": "ONLINE",
    "bitcoinUnit": "BTC",
    "unitFormat": "DOT",
    "blockExplorer": "https://mempool.space",
    "feeRatesSource": "MEMPOOL_SPACE",
    "fiatCurrency": "USD",
    "exchangeSource": "COINGECKO",
    "loadRecentWallets": true,
    "validateDerivationPaths": true,
    "groupByAddress": true,
    "includeMempoolOutputs": true,
    "notifyNewTransactions": true,
    "checkNewVersions": false,
    "theme": "LIGHT",
    "openWalletsInNewWindows": false,
    "hideEmptyUsedAddresses": false,
    "showTransactionHex": true,
    "showLoadingLog": true,
    "showAddressTransactionCount": false,
    "showDeprecatedImportExport": false,
    "signBsmsExports": false,
    "preventSleep": false,
    "dustAttackThreshold": 1000,
    "enumerateHwPeriod": 30,
    "useZbar": true,
    "serverType": "BITCOIN_CORE",
    "publicElectrumServer": "ssl://bitcoin.lu.ke:50002|bitcoin.lu.ke",
    "coreServer": "http://127.0.0.1:8332",
    "coreAuthType": "USERPASS","""

#    sparrow_config2 = '"coreDataDir": "C:\\Users\\EXAMPLE_USERNAME\\AppData\\Roaming\\Bitcoin",'
    
    sparrow_config3 = """"coreAuth": "parman:parman",
    "useLegacyCoreWallet": false,
    "useProxy": false,
    "autoSwitchProxy": true,
    "maxServerTimeout": 34,
    "maxPageSize": 100,
    "usePayNym": false,
    "mempoolFullRbf": false,
    "appWidth": 1083.0,
    "appHeight": 805.5
  }"""

    bitcoin_dir = pco.grep("bitcoin_dir=", returnline=True).strip().split('=')[1]
    coreDD = ""
    for i in bitcoin_dir:
       if i == "\\":
         i = '/'
       coreDD = coreDD + i
    
    sparrow_config2 = f'"coreDataDir": "{coreDD}",'
    sparrow_config_final = f"""{sparrow_config1}
{sparrow_config2}
{sparrow_config3}
"""
    sparrow_config_dir = HOME / "Appdata" / "Roaming" / "Sparrow"

    if not sparrow_config_dir.exists():
        sparrow_config_dir.mkdir()
      
    sparrow_config_path = sparrow_config_dir / "config"

    with sparrow_config_path.open('w') as f:
        f.write(sparrow_config_final + '\n')