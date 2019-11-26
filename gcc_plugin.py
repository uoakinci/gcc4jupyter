from v1.gccp1 import GCCPlugin as GVCC_V1
from v2.gccp2 import GCCPluginV2 as GCC_V2


def load_ipython_extension(ip):
    gcc_plugin = GCC_V1(ip)
    ip.register_magics(gcc_plugin)

    gcc_plugin_v2 = GCC_V2(ip)
    ip.register_magics(gcc_plugin_v2)
