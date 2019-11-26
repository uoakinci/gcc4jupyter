import argparse


def get_argparser():
    parser = argparse.ArgumentParser(description='GCCPlugin params')
    parser.add_argument("-t", "--timeit", action='store_true',
                        help='flag to return timeit result instead of stdout')
    return parser


def print_out(out: str):
    for l in out.decode('utf8').split('\n'):
        print(l)
