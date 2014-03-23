import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc
from operator import *

def get_subsidy(nCap, nMaxSubsidy, bnTarget):
    bnLowerBound = 0.01
    bnUpperBound = bnSubsidyLimit = nMaxSubsidy
    bnTargetLimit = 0x00000fffff000000000000000000000000000000000000000000000000000000

    while bnLowerBound + 0.01 <= bnUpperBound:
        bnMidValue = (bnLowerBound + bnUpperBound) / 2
        if pow(bnMidValue, nCap) * bnTargetLimit > pow(bnSubsidyLimit, nCap) * bnTarget:
            bnUpperBound = bnMidValue
        else:
            bnLowerBound = bnMidValue

    nSubsidy = round(bnMidValue, 2)

    if nSubsidy > bnMidValue:
        nSubsidy = nSubsidy - 0.01

    return int(nSubsidy * 1000000)

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(
    execoin=math.Object(
        P2P_PREFIX='fabfb5da'.decode('hex'),
        P2P_PORT=9989,
        ADDRESS_VERSION=33,
        RPC_PORT=9988,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'execoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('vtc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=45, # s
        SYMBOL='EXE',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Execoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Execoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.execoin'), 'execoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.execoin.net/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.execoin.net/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.execoin.net/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),

    execoin_zen=math.Object(
        P2P_PREFIX='fabfb5da'.decode('hex'),
        P2P_PORT=9989,
        ADDRESS_VERSION=33,
        RPC_PORT=9988,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'execoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('vtc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=45, # s
        SYMBOL='EXE',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'execoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/execoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.execoin'), 'execoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.execoin.net/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.execoin.net/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.execoin.net/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.1e8,
    ),
    
    namecoin=math.Object(
        P2P_PREFIX='f9beb4fe'.decode('hex'),
        P2P_PORT=8334,
        ADDRESS_VERSION=52,
        RPC_PORT=8332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'namecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='NMC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Namecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Namecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.namecoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.dot-bit.org/b/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.dot-bit.org/a/',
        TX_EXPLORER_URL_PREFIX='http://explorer.dot-bit.org/tx/',
        SANE_TARGET_RANGE=(2**256//2**32 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.2e8,
    ),
    namecoin_testnet=math.Object(
        P2P_PREFIX='fabfb5fe'.decode('hex'),
        P2P_PORT=18334,
        ADDRESS_VERSION=111,
        RPC_PORT=8332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'namecoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='tNMC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Namecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Namecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.namecoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://testnet.explorer.dot-bit.org/b/',
        ADDRESS_EXPLORER_URL_PREFIX='http://testnet.explorer.dot-bit.org/a/',
        TX_EXPLORER_URL_PREFIX='http://testnet.explorer.dot-bit.org/tx/',
        SANE_TARGET_RANGE=(2**256//2**32 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),

    terracoin=math.Object(
        P2P_PREFIX='42babe56'.decode('hex'),
        P2P_PORT=13333,
        ADDRESS_VERSION=0,
        RPC_PORT=13332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'terracoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*100000000 >> (height + 1)//1050000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=120, # s
        SYMBOL='TRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Terracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Terracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.terracoin'), 'terracoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    terracoin_testnet=math.Object(
        P2P_PREFIX='41babe56'.decode('hex'),
        P2P_PORT=23333,
        ADDRESS_VERSION=111,
        RPC_PORT=23332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'terracoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*100000000 >> (height + 1)//1050000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=120, # s
        SYMBOL='tTRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Terracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Terracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.terracoin'), 'terracoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),

    digitalcoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=7999,
        ADDRESS_VERSION=30,
        RPC_PORT=7998,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'digitalcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 15*100000000 >> (height + 1)//4730400,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=40, # s targetspacing
        SYMBOL='DGC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'digitalcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/digitalcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.digitalcoin'), 'digitalcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://dgc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://dgc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://dgc.cryptocoinexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    
    worldcoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=11081,
        ADDRESS_VERSION=73,
        RPC_PORT=11082,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'worldcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 64*100000000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=30, # s targetspacing
        SYMBOL='WDC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'worldcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/worldcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.worldcoin'), 'worldcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://wdc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://wdc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://wdc.cryptocoinexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    
    craftcoin=math.Object(
        P2P_PREFIX='fcd9b7dd'.decode('hex'),
        P2P_PORT=12124,
        ADDRESS_VERSION=57,
        RPC_PORT=12123,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'craftcoin address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 2*100000000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=60, # s targetspacing
        SYMBOL='CRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'craftcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/craftcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.craftcoin'), 'craftcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://crc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://crc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://crc.cryptocoinexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    casinocoin=math.Object(
        P2P_PREFIX='fac3b6da'.decode('hex'),
        P2P_PORT=47950,
        ADDRESS_VERSION=28,
        RPC_PORT=47970,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'casinocoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//3153600,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=30, # s targetspacing
        SYMBOL='CSC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'casinocoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/casinocoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.casinocoin'), 'casinocoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://casinocoin.mooo.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://casinocoin.mooo.com/address/',
        TX_EXPLORER_URL_PREFIX='http://casinocoin.mooo.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    anoncoin=math.Object(
        P2P_PREFIX='facabada'.decode('hex'),
        P2P_PORT=9377,
        ADDRESS_VERSION=23,
        RPC_PORT=9376,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'anoncoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 5*100000000 >> (height + 1)//306600,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=205, # s targetspacing
        SYMBOL='ANC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'anoncoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/anoncoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.anoncoin'), 'anoncoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://altexplorer.net/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://altexplorer.net/address/',
        TX_EXPLORER_URL_PREFIX='http://altexplorer.net/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    globalcoin=math.Object(
        P2P_PREFIX='fcd9b7dd'.decode('hex'),
        P2P_PORT=55789,
        ADDRESS_VERSION=15,
        RPC_PORT=55788,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'globalcoin address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 100*100000000 >> (height + 1)//288400,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=40, # s targetspacing
        SYMBOL='GLC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'globalcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/globalcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.globalcoin'), 'globalcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://blockchainx.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://blockchainx.com/address/',
        TX_EXPLORER_URL_PREFIX='http://blockchainx.com/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    nyancoin=math.Object(
        P2P_PREFIX='fcd9b7dd'.decode('hex'),
        P2P_PORT=33701,
        ADDRESS_VERSION=45,
        RPC_PORT=33700,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'nyancoin address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 337*100000000 >> (height + 1)//500000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=60, # s targetspacing
        SYMBOL='NYAN',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'nyancoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/nyancoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.nyancoin'), 'nyancoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://nyancha.in/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://nyancha.in/address/',
        TX_EXPLORER_URL_PREFIX='http://nyancha.in/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    potcoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=4200,
        ADDRESS_VERSION=55,
        RPC_PORT=42000,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'potcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 420*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=40, # s
        SYMBOL='POT',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'potcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/potcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.potcoin'), 'potcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://potchain.potcoin.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://potchain.potcoin.info/address/',
        TX_EXPLORER_URL_PREFIX='http://potchain.potcoin.info/transaction/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    dogecoin=math.Object(
        P2P_PREFIX='c0c0c0c0'.decode('hex'),
        P2P_PORT=22556,
        ADDRESS_VERSION=30,
        RPC_PORT=22555,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'dogecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 10000*100000000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=60, # s
        SYMBOL='DOGE',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'dogecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/dogecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dogecoin'), 'dogecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://dogechain.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://dogechain.info/address/',
        TX_EXPLORER_URL_PREFIX='http://dogechain.info/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
