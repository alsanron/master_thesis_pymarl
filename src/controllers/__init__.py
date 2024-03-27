REGISTRY = {}

from .basic_controller import BasicMAC
from .basic_controller_transformer import BasicMACTransformer

REGISTRY["basic_mac"] = BasicMAC
REGISTRY["basic_mac_transformer"] = BasicMACTransformer