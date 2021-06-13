from requests import get

from WebStreamer.logger import LOGGER
from WebStreamer.vars import Var


def ping_server():
    k = get(f"https://ping-pong-sn.herokuapp.com/pingback?link={Var.URL}").json()
    if not k.get("error"):
        LOGGER.info(f"KeepAliveService: Pinged {Var.FQDN} with status {k['status']}")
    else:
        LOGGER.error("Couldn't Ping the Server!")
