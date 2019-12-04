#!/usr/bin/env python3
import json
import os.path
import yaml
from shutil import copy

from argparse import ArgumentParser, Namespace

from .base_cfg import BaseCfg


class S3ServerCfg(BaseCfg):
    __options = {}
    __cfg_path = ""


    def __init__(self, cfg_path: str=None, arg_parser: ArgumentParser=None):
        if cfg_path:
            self.__cfg_path = cfg_path
        else:
            self.__cfg_path = os.path.join(
                self._pillar_path,
                "components",
                "s3server.sls"
            )

        if os.path.exists(self.__cfg_path):
            self.__load_defaults()
        if arg_parser:
            self.__setup_args(arg_parser)

    def __setup_args(self, arg_parser=None):

        if not arg_parser:
            raise Exception("__setup_args() cannot be called without an argparse object")

        arg_parser.add_argument(
            '--s3server-file',
            dest = 's3server_file',
            action="store",
            help='Yaml file with s3server configs'
        )

        arg_parser.add_argument(
            '--show-s3server-file-format',
            dest = 'show_s3server_file_format',
            action="store_true",
            help='Display Yaml file format for s3server configs'
        )
        arg_parser.add_argument(
            '--load-default',
            dest = 'load_default',
            action = 'store_true',
            help = 'Reset default values to a modified YAML file'
        )


    def __load_defaults(self):
        with open(self.__cfg_path, 'r') as fd:
            self.__options = yaml.safe_load(fd)
        # print(json.dumps(self.__options, indent = 4))
        # TODO validations for configs.


    def process_inputs(self, program_args: Namespace) -> bool:

        if program_args.interactive:
            input("\nAccepting interactive inputs for pillar/s3server.sls. Press any key to continue...")
            input_msg = (
                "Reuse the port for s3server? (true/false)({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_REUSEPORT"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_REUSEPORT"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_REUSEPORT"]
            )

            input_msg = (
                "Enter the bind address for ipv4 ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_IPV4_BIND_ADDR"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_IPV4_BIND_ADDR"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_IPV4_BIND_ADDR"]
            )

            input_msg = (
                "Enter the bind address for ipv6 ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_IPV6_BIND_ADDR"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_IPV6_BIND_ADDR"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_IPV6_BIND_ADDR"]
            )

            input_msg = ("Enter bind port for s3server ({0}): ".format(
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_BIND_PORT"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_BIND_PORT"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_BIND_PORT"]
            )

            input_msg = (
                "Enter the endpoint for s3 ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_DEFAULT_ENDPOINT"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_DEFAULT_ENDPOINT"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_DEFAULT_ENDPOINT"]
            )

            input_msg = (
                "Enter the regional endpoints for s3 ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_REGION_ENDPOINTS"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_REGION_ENDPOINTS"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_REGION_ENDPOINTS"]
            )

            input_msg = (
                "Enter the read ahead multiple ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_READ_AHEAD_MULTIPLE"]
                )
            )
            # TODO: Put the better input message.
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_READ_AHEAD_MULTIPLE"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_READ_AHEAD_MULTIPLE"]
            )

            input_msg = (
                "Do you want to enable ssl for s3 server (true/false)? ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_SSL_ENABLE"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_SSL_ENABLE"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_SERVER_SSL_ENABLE"]
            )

            input_msg = (
                "Do you want to enable performance stats for s3 server (0/1)? ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_PERF"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_PERF"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_PERF"]
            )

            input_msg = (
                "Enter the logging mode for s3 server (DEBUG, INFO, WARN, ERROR, FATAL) ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_LOG_MODE"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_LOG_MODE"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_LOG_MODE"]
            )

            input_msg = (
                "Do you want to enable buffering during logging? ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_LOG_ENABLE_BUFFERING"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_LOG_ENABLE_BUFFERING"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_LOG_ENABLE_BUFFERING"]
            )

            input_msg = (
                "Do you want to enable ssl for s3 auth server? ({0}): ".format(
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_AUTH_SSL"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_AUTH_SSL"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_AUTH_SSL"]
            )

            input_msg = (
                "Enter ip address for s3 auth server (for ipv6 use following format: ipv6:::1)({0}): ".format(
                    self.__options["s3server"]["S3_AUTH_CONFIG"]["S3_AUTH_IP_ADDR"]
                )
            )
            self.__options["s3server"]["S3_AUTH_CONFIG"]["S3_AUTH_IP_ADDR"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_AUTH_CONFIG"]["S3_AUTH_IP_ADDR"]
            )

            input_msg = (
                "Enter the port for s3 auth server to be used for https requests ({0}): ".format(
                    self.__options["s3server"]["S3_AUTH_CONFIG"]["S3_AUTH_PORT"]
                )
            )
            self.__options["s3server"]["S3_AUTH_CONFIG"]["S3_AUTH_PORT"] = (
                input(input_msg)
                or
                self.__options["s3server"]["S3_AUTH_CONFIG"]["S3_AUTH_PORT"]
            )

            input_msg = ("Do you want to enable the Stats feature (true/false)? ({0}): ".format(
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_STATS"]
                )
            )
            self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_STATS"] = input(input_msg) \
                or self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_STATS"]

            if self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_ENABLE_STATS"]:
                input_msg = (
                    "Enter Statsd server IP address: ({0}): ".format(
                        self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATSD_IP_ADDR"]
                    )
                )
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATSD_IP_ADDR"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATSD_IP_ADDR"]
                )

                input_msg = (
                    "Enter Statsd server IP port ({0}): ".format(
                        self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATSD_PORT"]
                    )
                )
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATSD_PORT"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATSD_PORT"]
                )

                input_msg = (
                    "Provide the path of the yaml input file for White list of Stats metrics to be published to the backend ({0}): ".format(
                        self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATS_WHITELIST_FILENAME"]
                    )
                )
                self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATS_WHITELIST_FILENAME"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_SERVER_CONFIG"]["S3_STATS_WHITELIST_FILENAME"]
                )

            config_clovis = input(
                "Do you want to configure Clovis parameters? 'no' will set the defaults. (yes/no): "
            )
            if config_clovis:
                print ("Clovis configuration Section, stick to defaults if "
                    "you are not sure about the parameters")
                input_msg = (
                    "Enter maximum units per read/write request to clovis ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_UNITS_PER_REQUEST"]
                    )
                )
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_UNITS_PER_REQUEST"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_UNITS_PER_REQUEST"]
                )

                input_msg = (
                    "Enter maximum no of key value pair to be fetched from a KVS index ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_IDX_FETCH_COUNT"]
                    )
                )
                # TODO: Enter beeter input message.
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_IDX_FETCH_COUNT"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_IDX_FETCH_COUNT"]
                )

                input_msg = (
                    "Enter the minimum length of the 'tm' receive queue for Clovis ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_TM_RECV_QUEUE_MIN_LEN"]
                    )
                )
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_TM_RECV_QUEUE_MIN_LEN"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_TM_RECV_QUEUE_MIN_LEN"]
                )

                input_msg = (
                    "Enter the maximum size of the rpc message for Clovis [{0} bytes]: ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_RPC_MSG_SIZE"]
                    )
                )
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_RPC_MSG_SIZE"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_MAX_RPC_MSG_SIZE"]
                )

                print ("Clovis memory pool configuration Section, stick to "
                    "defaults if you are not sure about the parameters")
                input_msg = (
                    "Enter array of unit sizes to create Clovis memory pools ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_UNIT_SIZES_FOR_MEMORY_POOL"]
                    )
                )
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_UNIT_SIZES_FOR_MEMORY_POOL"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_UNIT_SIZES_FOR_MEMORY_POOL"]
                )

                input_msg = (
                    "Enter the read initial buffer count ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_INITIAL_BUFFER_COUNT"]
                    )
                )
                # TODO: Enter better input message.
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_INITIAL_BUFFER_COUNT"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_INITIAL_BUFFER_COUNT"]
                )

                input_msg = (
                    "Enter pool's expandable size in blocks (multiple of S3_CLOVIS_UNIT_SIZE) ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_EXPANDABLE_COUNT"]
                    )
                )
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_EXPANDABLE_COUNT"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_EXPANDABLE_COUNT"]
                )

                input_msg = (
                    "Enter the maximum memory threshold for the pool in bytes (multiple of S3_CLOVIS_UNIT_SIZE) ({0}): ".format(
                        self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_MAX_THRESHOLD"]
                    )
                )
                self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_MAX_THRESHOLD"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_CLOVIS_CONFIG"]["S3_CLOVIS_READ_POOL_MAX_THRESHOLD"]
                )

            config_libevent = input(
                "Do you want to configure libevent parameters? 'no' will set the defaults. (yes/no): "
            )

            if config_libevent:
                print ("Libevent configuration Section, stick to defaults if you are not sure about the parameters")
                input_msg = (
                    "Enter maximum read size for a single read operation in bytes (user should not try to read more than this value) ({0}): ".format(
                        self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_MAX_READ_SIZE"]
                    )
                )
                self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_MAX_READ_SIZE"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_MAX_READ_SIZE"]
                )

                input_msg = (
                    "Enter Libevent pool buffer size, (in case of "
                    "S3_CLOVIS_UNIT_SIZE of size 1MB, it is recommended to "
                    "have S3_LIBEVENT_POOL_BUFFER_SIZE of size 16384) ({0}): ".format(
                        self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_BUFFER_SIZE"]
                    )
                )
                self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_BUFFER_SIZE"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_BUFFER_SIZE"]
                )

                input_msg = ("Enter the initial pool size in bytes (should be multiple of S3_CLOVIS_UNIT_SIZE) ({0}):".format(
                        self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_INITIAL_SIZE"]
                    )
                )
                self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_INITIAL_SIZE"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_INITIAL_SIZE"]
                )

                input_msg = (
                    "Enter pool's expandable size in bytes "
                    "(should be multiple of S3_CLOVIS_UNIT_SIZE) ({0}):".format(
                        self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_EXPANDABLE_SIZE"]
                    )
                )
                self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_EXPANDABLE_SIZE"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_EXPANDABLE_SIZE"]
                )

                input_msg = ("Enter the maximum memory threshold for the pool in bytes "
                    "(should be multiple of S3_CLOVIS_UNIT_SIZE) ({0}):".format(
                        self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_MAX_THRESHOLD"]
                    )
                )
                self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_MAX_THRESHOLD"] = (
                    input(input_msg)
                    or
                    self.__options["s3server"]["S3_THIRDPARTY_CONFIG"]["S3_LIBEVENT_POOL_MAX_THRESHOLD"]
                )
            # print(json.dumps(self.__options, indent = 4))
            return True
        if program_args.show_s3server_file_format:
            print(
                yaml.safe_dump(
                    self.__options,
                    stream=None,
                    default_flow_style=False,
                    canonical=False,
                    width=1,
                    indent=4
                )
            )

            return False
        elif program_args.s3server_file:
            # Load s3server file and merge options.
            new_options = {}
            with open(program_args.s3server_file, 'r') as fd:
                new_options = yaml.safe_load(fd)
            self.__options.update(new_options)
            return True

        elif program_args.load_default:
            if os.path.exists(self.__cfg_path+".bak"):
                copy(self.__cfg_path+".bak",self.__cfg_path)
            else:
                print("Error: No Backup File exists ")
            return False
        else:
            print("Error: No usable inputs provided.")
            return False

    def pillar_backup(func):
        def backup(*args):
            copy(args[0].__cfg_path,args[0].__cfg_path+".bak")
            return func(*args)
        return backup


    @pillar_backup
    def save(self):
        with open(self.__cfg_path, 'w') as fd:
            yaml.safe_dump(
                self.__options,
                stream=fd,
                default_flow_style=False,
                canonical=False,
                width=1,
                indent=4
            )


    def validate(self, schema_dict: dict, pillar_dict: dict) -> bool:
        pass
