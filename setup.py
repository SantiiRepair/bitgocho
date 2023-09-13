#!/usr/bin/env python3

from distutils.core import setup
import bitgocho

setup(
    name="bitgocho",
    version=bitgocho.version,
    author="Chris Markiewicz, Bram Cohen, John Hoffman, Uoti Arpala et. al.",
    author_email="<effigies@gmail.com>",
    url="https://github.com/effigies/bitgocho",
    description="John Hoffman's fork of the original bittorrent",
    license="MIT",
    packages=[
        "bitgocho",
        "bitgocho.Application",
        "bitgocho.Client",
        "bitgocho.Meta",
        "bitgocho.Network",
        "bitgocho.Storage",
        "bitgocho.Tracker",
        "bitgocho.Types",
    ],
    scripts=[
        "btdownloadheadless.py",
        "bttrack.py",
        "btmakemetafile.py",
        "btlaunchmany.py",
        "btcompletedir.py",
        "btdownloadcurses.py",
        "btlaunchmanycurses.py",
        "btmakemetafile.py",
        "btreannounce.py",
        "btrename.py",
        "btshowmetainfo.py",
        "btcopyannounce.py",
        "btsethttpseeds.py",
    ],
)
