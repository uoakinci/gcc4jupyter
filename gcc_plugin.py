from v2.v2 import GCCPlugin as GCC


def load_ipython_extension(ip):
    gcc_plugin = GCC(ip)
    ip.register_magics(gcc_plugin)

