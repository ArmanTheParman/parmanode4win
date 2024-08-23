from config_f import *
from variables import *
from functions import *


def make_mempool_docker_compose():

    IP = get_IP_variables
    print(IP["IP"])
    input()

    # while True:
    #     try: bco.grep("rpcuser") 
    #     except: 
    #         rpcpassword="parman"
    #         rpcuser="parman"
    #         break
    #     rpcuser = bco.grep("rpcuser=", returnline=True).strip().split('=')[1]
    #     rpcpassword = bco.grep("rpcpassword=", returnline=True).strip().split('=')[1]
    #     break

    # print(rpcuser)
    # input()


    mariadb_data="mariadb_data"
    mysql_data="mysql_data"

#     text = f"""networks:
#     PM_network:
#       driver: bridge

# services:
#   mempool_web:
#     environment:
#       FRONTEND_HTTP_PORT: "8180"
#       BACKEND_MAINNET_HTTP_HOST: "api"
#     image: mempool/frontend:latest
#     user: "0:0"
#     restart: on-failure
#     stop_grace_period: 1m
#     command: "./wait-for db:3306 --timeout=720 -- nginx -g 'daemon off;'"
#     ports:
#       - 8180:8180
#     networks:
#       - PM_network
#   api:
#     environment:
#       MEMPOOL_BACKEND: "none"
#       CORE_RPC_HOST: "{IP["IP"]}"
#       CORE_RPC_PORT: "8332"
#       ELECTRUM_HOST: "{IP["IP"]}"
#       ELECTRUM_PORT: "50005"
#       ELECTRUM_TLS_ENABLED: "false"
#       CORE_RPC_USERNAME: "{rpcuser}"
#       CORE_RPC_PASSWORD: "{rpcpassword}"
    text = f"""
      DATABASE_ENABLED: "true"
      DATABASE_HOST: "db"
      DATABASE_DATABASE: "mempool"
      DATABASE_USERNAME: "mempool"
      DATABASE_PASSWORD: "mempool"
      STATISTICS_ENABLED: "true"
      SECOND_CORE_RPC_HOST: ""
      SECOND_CORE_RPC_PORT: ""
      SECOND_CORE_RPC_USERNAME: ""
      SECOND_CORE_RPC_PASSWORD: ""
      SECOND_CORE_RPC_TIMEOUT: ""
      SECOND_CORE_RPC_COOKIE: "false"
      SECOND_CORE_RPC_COOKIE_PATH: ""
      SOCKS5PROXY_ENABLED: "false"
      SOCKS5PROXY_HOST: "127.0.0.1"
      SOCKS5PROXY_PORT: "9050"
      SOCKS5PROXY_USERNAME: "" #leave blank
      SOCKS5PROXY_PASSWORD: "" #leave blank
      LIGHTNING_ENABLED: "false"
      LIGHTNING_BACKEND: "lnd"
      LIGHTNING_TOPOLOGY_FOLDER: ""
      LIGHTNING_STATS_REFRESH_INTERVAL: 600
      LIGHTNING_GRAPH_REFRESH_INTERVAL: 600
      LIGHTNING_LOGGER_UPDATE_INTERVAL: 30
      LND_TLS_CERT_PATH: "{HOME / '.lnd'}"
      LND_MACAROON_PATH: "{HOME / '.lnd/data/chain/bitcoin/mainnet'}"
      LND_REST_API_URL: "https://localhost:8080"
      LND_TIMEOUT: 10000
    image: mempool/backend:latest
    user: "0:0"
    restart: on-failure
    stop_grace_period: 1m
    command: "./wait-for-it.sh db:3306 --timeout=720 --strict -- ./start.sh"
    volumes:
      - {mariadb_data}:/backend/cache
    networks:
      - PM_network
  db:
    environment:
      MYSQL_DATABASE: "mempool"
      MYSQL_USER: "mempool"
      MYSQL_PASSWORD: "mempool"
      MYSQL_ROOT_PASSWORD: "admin"
    image: mariadb:10.5.21
    user: "0:0"
    restart: on-failure
    stop_grace_period: 1m
    volumes:
      - {mysql_data}:/var/lib/mysql
    networks:
      - PM_network
volumes:
  mariadb_data:
  mysql_data:"""
    
    file = pp / "mempool" / "docker" / "docker-compose.yml"
    file = config(file)
    tmpo.truncate()
    tmpo.add(config)