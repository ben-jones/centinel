#!/usr/bin/env python
import sys
import argparse

import centinel
import centinel.config


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version',
                        version="Centinel %s" % (centinel.__version__),
                        help='Sync data with server')
    parser.add_argument('--experiment', '-e', help='Experiment name',
                        nargs="*", dest="experiments")
    parser.add_argument('--config', '-c', help='Configuration file',
                        dest='config')
    parser.add_argument('--sync', help='Sync data with server',
                        action='store_true')
    wait_help = 'Wait a random period of time, up to 15 min, before syncing'
    parser.add_argument('--random-wait', help=wait_help, dest='randomWait',
                        action='store_true')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    # create the configuration at runtime (what we were doing before)
    # by default, but use the user specified file parameters instead
    # if specified
    configuration = centinel.config.Configuration()
    if args.config:
        configuration.parse_config(args.config)

    client = centinel.client.Client(configuration.params)
    client.setup_logging()

    if args.sync:
        centinel.backend.sync(configuration.params,
                              random_wait=args.randomWait)
    else:
        client.run()
