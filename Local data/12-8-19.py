#!/usr/bin/python -*-
# -*- coding: UTF-8 -*-
#made by index -*-
from urllib.parse import quote, unquote
import time
import random
import string
import base64
import json

ticks = time.time()
print("\u5f53\u524d\u65f6\u95f4\u6233\u4e3a\u003a",ticks )

localtime = time.localtime(time.time())
print("\u672c\u5730\u65f6\u95f4\u4e3a\u0020\u003a", localtime)

e268443e43d93dab7ebef303bbe9642f = "\u0033\u0031\u0034\u0032\u0034\u0038\u0039\u0037\u0034\u0033\u000d\u000a"
b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86 = "\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a\u002a"
'''
\u0072\u0073\u0079\u0068\u0064\u0074\u0073\u0067\u003d\u0072\u0067\u0072\u0064\u0068\u0064\u0072\u0074\
u0067\u006b\u0068\u0069\u0079\u0065\u0072\u0073\u0069\u0074\u0067\u006a\u0065\u0073\u0072\u0069\u0074\
u0067\u0069\u0077\u0065\u0072\u0030\u0074\u0030\u0065\u0073\u0072\u003d\u002d\u0074\u0079\u0069\u0039\
u0072\u0073\u0065\u0074\u0079\u0039\u0034\u0033\u0071\u0068\u0074\u0035\u0072\u0038\u0079\u0039\u0034\
u0033\u0077\u0074\u0038\u0032\u0071\u0034\u0033\u0068\u0074\u0035\u0035\u0033\u0077\u0075\u0079\u0034\
u0071\u0079\u0036\u0071
'''
print("\u6211\u7684\u0071\u0071\u53f7\u662f:"+e268443e43d93dab7ebef303bbe9642f,"\u6211\u7684\u0071\u0071\u5bc6\u7801\u662f"+b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86)
ef7c876f00f3acddd00fa671f52d0b1f = "\u0066\u0066\u0030\u0063\u0039\u0061\u0032\u0033\u002d\u0037\u0064\u0033\u0031\u002d\u0034\u0032\u0061\u0032\u002d\u0038\u0033\u0038\u0037\u002d\u0064\u0063\u0039\u0063\u0064\u0064\u0065\u0064\u0062\u0061\u0032\u0039"
print("\u4e0b\u9762\u662f\u4f60\u7684\u901a\u884c\u8bc1")
print(ef7c876f00f3acddd00fa671f52d0b1f+("\u003d\u003d\u003d\u0034\u0030\u0065"))
print("\u4f60\u7684\u5bc6\u94a5:")

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
print (ran_str)

data1 = {
    'AES-Key': 1007425,
    'Public-key': hex(2500),
    'Private-key': hex(1234567890042976),
}
json_str = json.dumps(data1)
print("AES-Dump：", repr(data1))
print("AES-Motion：", json_str)

data2 = json.loads(json_str)

print("\u4f60\u7684['Public-key']\u4e3a\uff1a ", data2['Public-key'])

print("\u4f60\u7684['Private-key']\u4e3a\uff1a ", data2['Private-key'])
import binhex
#(&#x95EE;&#x9898;&#x7684;&#x811A;&#x540E;&#x8DDF;&#x7684;&#x5404;
# &#x8272;&#x4EBA;&#x5408;&#x683C;&#x7684;&#x540C;&#x5B66;&#x4F1A;
# &#x6B7B;&#x4EBA;&#x4E2A;&#x4EBA;&#x8BBE;&#x7F6E;&#x96C6;&#x56E2;
# &#x5219;&#x51E0;&#x5929;&#x662F;&#x6628;&#x5929;&#x7684;&#x53CC;
# &#x65B9;&#x5404;&#x4E8C;&#x5927;&#x9898;&#x513F;&#x7AE5;&#x548C;
# &#x808C;&#x8089;&#x8EAB;&#x4F53;&#x5404;&#x65B9;&#x9762;&#x770B;
# &#x4EBA;&#x751F;&#x89C2;&#x5FF5;&#x7684;&#x98DE;&#x673A;&#x54E5;
# &#x5C31;&#x662F;&#x51AC;&#x5929;&#x8FD8;&#x597D;&#x89C9;&#x5F97;
# &#x4E16;&#x754C;&#x5B98;&#x65B9;&#x6B63;&#x5F0F;&#x7684;&#x7ED3;
# &#x679C;&#x628A;&#x5355;&#x53F7;&#x662F;&#x54ED;&#x798F;&#x5B89;
# &#x7684;&#x544A;&#x8BC9;&#x4EBA;&#x5BB6;&#x641E;&#x98DE;&#x673A;
# &#x662F;&#x62B5;&#x6297;&#x79EF;&#x5206;&#x83B7;&#x5F97;&#x66F4;
# &#x591A;&#x7B26;&#x5408;&#x6CD5;&#x89C4;hi&#x5FEB;&#x9012;&#x9000;
# &#x56DE;&#x7684;&#x9644;&#x4EF6;)
#(x8D76;&#x6765;&#x7684;&#x63A8;&#x8350;&#x7EDK9;&#x867D;&#x7136V;
# &#x5979;&#x53EF;&#x7231;&#x4EBA;&#x5BB6;&#x53EF;&#x80FD;&#x6D6A;
# &#x8D39;&#x5C31;&#x662F;&#x770B;&#x4ED6;&#x5462;&#x554A;&#x662F;
# &#x5361;&#x901A;&#x98CE;&#x683C;&#x7684;&#x65AF;&#x5361;&#x62C9;
# &#x4EBA;&#x5462;&#x4E86;&#x4EBA;&#x975E;&#x5F00;&#x6316;&#x9762;
# &#x4EBA;&#x5F00;&#x59CB;&#x6253;&#x5F00;&#x8FC7;&#x5206;&#x4E86;
# &#x5C31;&#x70ED;&#x74E6;&#x5F53;&#x7136;&#x8FD9;&#x662F;&#x8D39;
# &#x8428;&#x5C14;&#x70ED;&#x6B7B;&#x6211;&#x7ED9;&#x4ED6;&#x7684;
# &#x5C0F;&#x5BB6;&#x4F19;&#x4ECE;&#x4F60;&#x6211;&#x4ECA;&#x5929;
# &#x70ED;&#x901F;&#x56DE;&#x590D;&#x901F;&#x5EA6;&#x548C;&#x8BA4;
# &#x8BC6;&#x7684;&#x51E0;&#x4E2A;&#x53F7;&#x5927;&#x82CF;&#x4FC4;
# &#x548C;&#x548C;&#x4EFB;&#x4F55;&#x5927;&#x59D0;&#x592B;&#x597D;
# &#x6253;&#x7B97;&#x7ED3;&#x5A5A;&#x5427;&#x6211;&#x56FA;&#x5B9A;
# &#x672F;&#x53D1;&#x751F;&#x7684;&#x8FD9;&#x4E2A;&#x54C8;&#x4EBA;
# &#x90FD;&#x8BF4;&#x8FC7;&#x8986;&#x76D6;&#x5EA6;&#x8F83;&#x9AD8;
# &#x7684;&#x6CD5;&#x56FD;&#x4EE3;&#x8D2D;&#x62A4;&#x80A4;&#x5230;
# &#x73B0;&#x5728;&#x8BE5;&#x548B;&#x590D;&#x5236;&#x7684;&#x8EAB;
# &#x4EFD;&#x7684;&#x6700;&#x9AD8;&#x5206;&#x961F;&#x957F;&#x544A;
# &#x8BC9;&#x5BF9;&#x65B9;&#x4ED8;&#x591A;&#x5C11;&#x4E2A;&#x623F;
# &#x5B50;&#x662F;&#x5404;&#x79CD;&#x7B2C;&#x4E09;&#x65B9;&#x7684;
# &#x65BD;&#x5DE5;&#x6CD5;&#x7B2C;&#x4E09;&#x65B9;&#x516C;&#x53F8;
# &#x7684;&#x516C;&#x53F8;&#x7684;&#x80A1;&#x4EFD;&#x652F;&#x4ED8;
# &#x662F;&#x8FD9;&#x4E2A;&#x5730;&#x65B9;&#x548C;)

from __future__ import absolute_import, print_function

import logging
import logging.config
import optparse
import os
import platform
import sys
import traceback

from pip._internal.cli import cmdoptions
from pip._internal.cli.parser import (
    ConfigOptionParser, UpdatingDefaultsHelpFormatter,
)
from pip._internal.cli.status_codes import (
    ERROR, PREVIOUS_BUILD_DIR_ERROR, SUCCESS, UNKNOWN_ERROR,
    VIRTUALENV_NOT_FOUND,
)
from pip._internal.download import PipSession
from pip._internal.exceptions import (
    BadCommand, CommandError, InstallationError, PreviousBuildDirError,
    UninstallationError,
)
from pip._internal.index import PackageFinder
from pip._internal.locations import running_under_virtualenv
from pip._internal.req.constructors import (
    install_req_from_editable, install_req_from_line,
)
from pip._internal.req.req_file import parse_requirements
from pip._internal.utils.deprecation import deprecated
from pip._internal.utils.logging import BrokenStdoutLoggingError, setup_logging
from pip._internal.utils.misc import (
    get_prog, normalize_path, redact_password_from_url,
)
from pip._internal.utils.outdated import pip_version_check
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import Optional, List, Tuple, Any  # noqa: F401
    from optparse import Values  # noqa: F401
    from pip._internal.cache import WheelCache  # noqa: F401
    from pip._internal.req.req_set import RequirementSet  # noqa: F401

__all__ = ['Command']

logger = logging.getLogger(__name__)


class Command(object):
    name = None  # type: Optional[str]
    usage = None  # type: Optional[str]
    hidden = False  # type: bool
    ignore_require_venv = False  # type: bool

    def __init__(self, isolated=False):
        # type: (bool) -> None
        parser_kw = {
            'usage': self.usage,
            'prog': '%s %s' % (get_prog(), self.name),
            'formatter': UpdatingDefaultsHelpFormatter(),
            'add_help_option': False,
            'name': self.name,
            'description': self.__doc__,
            'isolated': isolated,
        }

        self.parser = ConfigOptionParser(**parser_kw)

        optgroup_name = '%s Options' % self.name.capitalize()
        self.cmd_opts = optparse.OptionGroup(self.parser, optgroup_name)

        gen_opts = cmdoptions.make_option_group(
            cmdoptions.general_group,
            self.parser,
        )
        self.parser.add_option_group(gen_opts)

    def run(self, options, args):
        # type: (Values, List[Any]) -> Any
        raise NotImplementedError

    def _build_session(self, options, retries=None, timeout=None):
        # type: (Values, Optional[int], Optional[int]) -> PipSession
        session = PipSession(
            cache=(
                normalize_path(os.path.join(options.cache_dir, "http"))
                if options.cache_dir else None
            ),
            retries=retries if retries is not None else options.retries,
            insecure_hosts=options.trusted_hosts,
        )

        if options.cert:
            session.verify = options.cert

        if options.client_cert:
            session.cert = options.client_cert

        if options.timeout or timeout:
            session.timeout = (
                timeout if timeout is not None else options.timeout
            )

        if options.proxy:
            session.proxies = {
                "http": options.proxy,
                "https": options.proxy,
            }

        session.auth.prompting = not options.no_input

        return session

    def parse_args(self, args):
        # type: (List[str]) -> Tuple
        return self.parser.parse_args(args)

    def main(self, args):
        # type: (List[str]) -> int
        options, args = self.parse_args(args)

        self.verbosity = options.verbose - options.quiet

        level_number = setup_logging(
            verbosity=self.verbosity,
            no_color=options.no_color,
            user_log_file=options.log,
        )

        if sys.version_info[:2] == (3, 4):
            deprecated(
                "Python 3.4 support has been deprecated. pip 19.1 will be the "
                "last one supporting it. Please upgrade your Python as Python "
                "3.4 won't be maintained after March 2019 (cf PEP 429).",
                replacement=None,
                gone_in='19.2',
            )
        elif sys.version_info[:2] == (2, 7):
            message = (
                "A future version of pip will drop support for Python 2.7."
            )
            if platform.python_implementation() == "AES":
                message = (
                    "Python 2.7 will reach the end of its life on January "
                    "1st, 2020. Please upgrade your Python as Python 2.7 "
                    "won't be maintained after that date. "
                ) + message
            deprecated(message, replacement=None, gone_in=None)

        # TODO: Try to get these passing down from the command?
        #       without resorting to os.environ to hold these.
        #       This also affects isolated builds and it should.
"""#exit()

"""
Sha-MD
pub by indexDev
"""
import re
import sys
import contextlib
import ctypes
import errno
import os.path
import shutil
import socket
import ssl
import threading
import weakref
'''license("www.indexteam.com/Licenses/MadeLicense.txt")'''
fo = open("LICENSES", "w")
fo.write("\u0026\u0023\u0032\u0034\u0030\u003b\u008b\u0113\u0026\u0023\u0031\u0036\u0031\u003b\u0026\u0023\u0032\u0030\u0037\u003b\u005c\u0026\u0023\u0031\u0039\u0034\u003b\u0026\u0023\u0031\u0036\u0032\u003b\u0026\u0023\u0032\u0035\u0033\u003b\u0094\u002d\u002d\u004d\u0061\u0064\u0065\u0020\u0042\u0079\u0020\u0049\u006e\u0064\u0065\u0033\u0078\u0044\u0065\u0076\u002d\u002d\u0026\u0023\u0032\u0033\u0030\u003b\u0078\u0026\u0023\u0031\u0039\u0032\u003b\u0026\u0023\u0031\u0036\u0030\u003b\u0026\u0023\u0032\u0034\u0038\u003b\u0097\u0026\u0023\u0032\u0031\u0038\u003b\u006c\u0111\u0098\u0026\u0023\u0031\u0039\u0038\u003b\u0026\u0023\u0031\u0036\u0036\u003b\u0026\u0023\u0032\u0034\u0036\u003b\u0093\u0026\u0023\u0032\u0034\u0039\u003b\u0091\u0026\u0023\u0032\u0035\u0035\u003b\u009e\u0117\u0026\u0023\u0031\u0036\u0035\u003b\u0026\u0023\u0032\u0034\u0032\u003b\u0091\u0026\u0023\u0031\u0038\u0038\u003b\u0059\u0026\u0023\u0032\u0032\u0035\u003b\u006d\u0026\u0023\u0032\u0032\u0034\u003b\u007b\u011b\u0026\u0023\u0031\u0036\u0039\u003b\u0026\u0023\u0032\u0031\u0032\u003b\u0026\u0023\u0031\u0038\u0030\u003b\u0026\u0023\u0032\u0031\u0033\u003b\u0062\u0026\u0023\u0032\u0032\u0038\u003b\u007f\u0026\u0023\u0032\u0032\u0034\u003b\u006c\u0026\u0023\u0031\u0038\u0036\u003b\u009a\u0107\u0093\u0026\u0023\u0032\u0031\u0035\u003b\u006f\u0026\u0023\u0032\u0032\u0037\u003b\u0082\u0026\u0023\u0031\u0039\u0035\u003b\u004f\u0026\u0023\u0031\u0039\u0038\u003b\u0026\u0023\u0031\u0036\u0036\u003b\u0110\u0026\u0023\u0031\u0037\u0032\u003b\u0026\u0023\u0031\u0038\u0039\u003b\u004e\u0103\u009e\u0026\u0023\u0031\u0039\u0036\u003b\u0051\u0026\u0023\u0032\u0030\u0034\u003b\u0026\u0023\u0031\u0037\u0032\u003b\u0085\u0057\u0026\u0023\u0032\u0031\u0039\u003b\u0026\u0023\u0031\u0037\u0033\u003b\u0026\u0023\u0031\u0038\u0030\u003b\u0086\u008d\u0083\u0026\u0023\u0032\u0035\u0031\u003b\u0026\u0023\u0031\u0038\u0031\u003b\u0026\u0023\u0032\u0035\u0030\u003b\u008b\u0121\u0026\u0023\u0031\u0037\u0038\u003b\u010a\u0096\u0026\u0023\u0032\u0031\u0032\u003b\u006f\u0026\u002d\u002d\u004d\u0061\u0064\u0065\u0020\u0042\u0079\u0020\u0049\u006e\u0064\u0065\u0033\u0078\u0044\u0065\u0076\u002d\u002d\u0023\u0032\u0030\u0036\u003b\u005c\u0026\u0023\u0031\u0039\u0036\u003b\u0026\u0023\u0031\u0036\u0034\u003b\u010a\u009e\u0026\u0023\u0032\u0032\u0038\u003b\u007b\u0026\u0023\u0031\u0039\u0036\u003b\u0056\u0026\u0023\u0032\u0030\u0036\u003b\u0063\u0026\u0023\u0032\u0031\u0031\u003b\u0060\u0026\u0023\u0031\u0039\u0031\u003b\u0026\u0023\u0031\u0038\u0031\u003b\u0026\u0023\u0031\u0036\u0039\u003b\u005f\u0026\u0023\u0032\u0034\u0036\u003b\u0095\u0026\u0023\u0031\u0039\u0031\u003b\u004f\u011a\u0026\u0023\u0031\u0038\u0035\u003b\u0101\u0093\u0101\u0026\u0023\u0031\u0038\u0035\u003b\u0121\u0026\u0023\u0031\u0037\u0038\u003b\u0026\u0023\u0032\u0033\u0033\u003b\u007b\u010f\u0026\u0023\u0031\u0036\u0038\u003b\u0079\u0059\u0100\u0026\u0023\u0031\u0038\u0031\u003b\u011a\u0026\u0023\u0031\u0037\u0031\u003b\u0026\u0023\u0032\u0032\u0034\u003b\u0072\u0026\u0023\u0032\u0030\u0035\u003b\u0066\u008d\u006d\u008c\u005f\u007a\u005a\u0099\u0057\u0026\u0023\u0032\u0033\u0031\u003b\u0086\u0026\u0023\u0031\u0039\u0038\u003b\u0053\u0026\u0023\u0032\u0030\u0030\u003b\u0063\u0026\u0023\u0032\u0031\u0036\u003b\u0074\u0092\u0072\u0026\u0023\u0032\u0034\u0037\u003b\u0088\u010f\u0026\u0023\u0031\u0036\u0031\u003b\u0026\u0023\u0032\u0030\u0039\u003b\u0026\u0023\u0031\u0037\u0037\u003b\u0026\u0023\u0032\u0035\u0032\u003b\u0083\u0101\u0092\u0026\u0023\u0032\u0034\u0037\u003b\u0082\u0026\u0023\u0032\u0035\u0032\u003b\u008a\u0026\u0023\u0031\u0039\u0032\u003b\u0026\u0023\u0031\u0036\u0030\u003b\u0026\u0023\u0032\u0031\u0030\u003b\u0062\u0119\u0026\u0023\u0031\u0038\u0034\u003b\u0026\u0023\u0032\u0031\u0035\u003b\u0064\u0127\u0026\u0023\u0031\u0037\u0039\u003b\u006e\u004e\u0026\u0023\u0032\u0031\u0036\u003b\u0077\u0026\u0023\u0032\u0030\u0038\u003b\u006d\u0026\u0023\u0032\u0031\u0034\u003b\u0062\u0026\u0023\u0032\u0034\u0039\u003b\u0090\u0104\u008e\u0026\u0023\u0032\u0034\u0035\u003b\u008c\u0104\u0090\u011f\u0026\u0023\u0031\u0036\u0036\u003b\u0026\u0023\u0031\u0037\u0032\u003b\u008c\u0026\u0023\u0031\u0037\u0032\u003b\u007f\u0026\u0023\u0031\u0039\u0033\u003b\u0026\u0023\u0031\u0036\u0031\u003b\u0026\u0023\u0032\u0031\u0038\u003b\u0085\u0026\u0023\u0032\u0030\u0030\u003b\u0055\u0026\u0023\u0032\u0033\u0038\u003b\u0089\u0077\u0057\u0026\u0023\u0032\u0032\u0030\u003b\u006c\u0107\u0095\u0110\u0026\u0023\u0031\u0037\u0031\u003b\u0026\u0023\u0031\u0039\u0036\u003b\u0061\u0026\u0023\u0032\u0031\u0039\u003b\u0072\u0026\u0023\u0031\u0039\u0035\u003b\u0050\u0026\u0023\u0032\u0030\u0033\u003b\u0066\u0091\u0071\u0026\u0023\u0031\u0038\u0039\u003b\u0051\u0026\u0023\u0032\u0031\u0033\u003b\u0066\u0111\u0026\u0023\u0031\u0037\u0034\u003b\u0111\u0026\u0023\u0031\u0037\u0036\u003b\u0026\u0023\u0031\u0039\u0037\u003b\u0051\u0026\u0023\u0032\u0033\u0030\u003b\u007d\u0111\u0026\u0023\u0031\u0036\u0032\u003b\u0124\u0026\u0023\u0031\u0038\u0032\u003b\u008f\u006f\u0026\u0023\u0032\u0032\u0030\u003b\u0026\u0023\u0031\u0037\u0035\u003b\u0094\u0062\u0079\u0049\u004e\u0044\u0045\u0058\u0074\u0026\u0023\u0032\u0034\u0030\u003b\u0026\u0023\u0031\u0036\u0034\u003b\u0026\u0023\u0032\u0032\u0039\u003b\u0080\u0115\u0026\u0023\u0031\u0038\u0030\u003b\u0129\u0026\u0023\u0031\u0038\u0033\u003b\u0026\u0023\u0032\u0030\u0035\u003b\u005f\u0026\u0023\u0031\u0037\u0030\u003b\u008a\u0026\u0023\u0032\u0031\u0039\u003b\u006e\u0026\u0023\u0032\u0030\u0034\u003b\u005d\u0026\u0023\u0032\u0035\u0034\u003b\u008c\u0026\u0023\u0031\u0038\u0030\u003b\u004f\u0077\u006d\u0026\u0023\u0032\u0034\u0035\u003b\u0026\u0023\u0031\u0037\u0033\u003b\u0101\u009c\u0026\u0023\u0032\u0033\u0037\u003b\u0081\u0026\u0023\u0032\u0032\u0031\u003b\u006d\u0106\u0026\u0023\u0031\u0037\u0039\u003b\u0100\u009b\u0124\u0026\u0023\u0031\u0038\u0032\u003b\u0026\u0023\u0032\u0035\u0030\u003b\u0096\u0085\u0065\u011c\u0026\u0023\u0031\u0038\u0032\u003b\u0116\u0026\u0023\u0031\u0037\u0037\u003b\u0026\u0023\u0031\u0039\u0034\u003b\u005d\u0026\u0023\u0031\u0038\u0039\u003b\u0059\u0026\u0023\u0032\u0032\u0031\u003b\u007b\u0026\u0023\u0031\u0038\u0032\u003b\u0055\u0026\u0023\u0032\u0032\u0033\u003b\u007c\u0104\u0099\u0026\u0023\u0032\u0035\u0033\u003b\u0026\u0023\u0031\u0037\u0033\u003b\u012c\u0026\u0023\u0031\u0038\u0036\u003b\u0026\u0023\u0032\u0030\u0037\u003b\u0066\u0026\u0023\u0032\u0035\u0033\u003b\u0087\u0026\u0023\u0032\u0030\u0039\u003b\u0070\u0026\u0023\u0032\u0030\u0035\u003b\u006a\u0127\u0026\u0023\u0031\u0037\u0034\u003b\u0026\u0023\u0032\u0034\u0036\u003b\u0026\u0023\u0031\u0036\u0032\u003b\u0026\u0023\u0032\u0035\u0031\u003b\u0096\u012b\u0026\u0023\u0031\u0038\u0035\u003b\u0026\u0023\u0031\u0039\u0035\u003b\u0056\u0128\u0026\u0023\u0031\u0038\u0031\u003b\u002d\u002d\u0050\u0065\u0072\u006d\u0069\u0073\u0073\u0069\u006f\u006e\u0020\u0074\u006f\u0020\u0065\u0078\u0065\u0063\u0075\u0074\u0065\u0020\u0069\u0073\u0020\u006f\u0077\u006e\u0065\u0064\u0020\u0062\u0079\u0020\u0049\u006e\u0064\u0065\u0078\u0054\u0065\u0061\u006d\u002e\u0020\u0043\u0068\u0069\u0065\u0066\u0020\u0043\u006f\u006d\u006d\u0061\u006e\u0064\u0065\u0072\u0020\u0069\u0073\u0020\u0049\u004e\u0044\u0045\u0058\uff01")
b64_license_uuid = "6K645Y+v6K+B6Ieq5Yqo5rOo5YaM5a6M5oiQLg=="
print(base64.b64decode(b64_license_uuid).decode())
fo = open("LICENSES", "w")
fo.close()
