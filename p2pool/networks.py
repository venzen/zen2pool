from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    bihthai=math.Object(
        PARENT=networks.nets['bihthai'],
        SHARE_PERIOD=3, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=100, # shares
        SPREAD=120, # blocks
        IDENTIFIER='112210f4b16c1cb1'.decode('hex'),
        PREFIX='112210f4b16c1cb1'.decode('hex'),
        P2P_PORT=11333,                         
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,                          
        WORKER_PORT=11331,                      
        BOOTSTRAP_ADDRS='',
        ANNOUNCE_CHANNEL='#p2pool-bth',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Bihthai to >=0.8.5.1!' if v < 80501 else None,
    ),

    execoin=math.Object(
        PARENT=networks.nets['execoin'],
        SHARE_PERIOD=9, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=40, # blocks
        IDENTIFIER='755F8AD0DD49380A'.decode('hex'),
        PREFIX='31357EF0ECB3C1BC'.decode('hex'),
        P2P_PORT=9172,                         
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,                          
        WORKER_PORT=9173,                      
        BOOTSTRAP_ADDRS='5.255.87.165'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-exe',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Execoin to >=0.8.5.1!' if v < 80501 else None,
    ),

    terracoin=math.Object(
        PARENT=networks.nets['terracoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//30, # shares
        REAL_CHAIN_LENGTH=24*60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='a41b2356a1b7d46e'.decode('hex'),
        PREFIX='5623b62178d2b9b3'.decode('hex'),
        P2P_PORT=9323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=9322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st 93.97.192.93 66.90.73.83 67.83.108.0 219.84.64.174 24.167.17.248 109.74.195.142 83.211.86.49 94.23.34.145 168.7.116.243 94.174.40.189:9344 89.79.79.195 portals94.ns01.us'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: 80002 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Terracoin to >= 0.8.0.2!' if v < 80002 else None,
    ),
    terracoin_testnet=math.Object(
        PARENT=networks.nets['terracoin_testnet'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//30, # shares
        REAL_CHAIN_LENGTH=60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='b41b2356a5b7d35d'.decode('hex'),
        PREFIX='1623b92172d2b8a2'.decode('hex'),
        P2P_PORT=19323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Terracoin to >= 0.8.0.1!' if v < 80001 else None,
    ),

    digitalcoin=math.Object(
        PARENT=networks.nets['digitalcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=45, # blocks
        IDENTIFIER='797EC5BC40AFA22E'.decode('hex'),
        PREFIX='23CD74AF85036A9F'.decode('hex'),
        P2P_PORT=23610,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8810,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-dgc',
        VERSION_CHECK=lambda v: True,
    ),
    
    worldcoin=math.Object(
        PARENT=networks.nets['worldcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=60, # blocks
        IDENTIFIER='5AE1DD1E84E6EC3A'.decode('hex'),
        PREFIX='43B80223C931E0A0'.decode('hex'),
        P2P_PORT=23620,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8820,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-wdc',
        VERSION_CHECK=lambda v: True,
    ),
    
    craftcoin=math.Object(
        PARENT=networks.nets['craftcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='755F8AD0DD49380A'.decode('hex'),
        PREFIX='31357EF0ECB3C1BC'.decode('hex'),
        P2P_PORT=23630,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8830,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-crc',
        VERSION_CHECK=lambda v: True,
    ),

    casinocoin=math.Object(
        PARENT=networks.nets['casinocoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=60, # blocks
        IDENTIFIER='5AE1F9AAEA359544'.decode('hex'),
        PREFIX='43DC544D48689C0D'.decode('hex'),
        P2P_PORT=23640,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8840,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com bigiron.homelinux.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-csc',
        VERSION_CHECK=lambda v: True,
    ),

    anoncoin=math.Object(
        PARENT=networks.nets['anoncoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=10, # blocks
        IDENTIFIER='40C08900F98B2AFA'.decode('hex'),
        PREFIX='43F8D4260E9F8E60'.decode('hex'),
        P2P_PORT=23650,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8850,
        BOOTSTRAP_ADDRS='xpool.net 5.255.87.165'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-anc',
        VERSION_CHECK=lambda v: True,
    ),

    globalcoin=math.Object(
        PARENT=networks.nets['globalcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=45, # blocks
        IDENTIFIER='5F0183D62F698832'.decode('hex'),
        PREFIX='52F8CF5955E02234'.decode('hex'),
        P2P_PORT=23660,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8860,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-glc',
        VERSION_CHECK=lambda v: True,
    ),

    nyancoin=math.Object(
        PARENT=networks.nets['nyancoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='5D4D5622297EE0E4'.decode('hex'),
        PREFIX='4DD804B010424A99'.decode('hex'),
        P2P_PORT=23670,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8870,
        BOOTSTRAP_ADDRS='xpool.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-nyan',
        VERSION_CHECK=lambda v: True,
    ),

    potcoin=math.Object(
        PARENT=networks.nets['potcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=10, # blocks
        IDENTIFIER='DDA1A1D3B2F68CDD'.decode('hex'),
        PREFIX='A2C3D4D541C11DDD'.decode('hex'),
        P2P_PORT=8420,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9420,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-pot',
        VERSION_CHECK=lambda v: True,
    ),

    dogecoin=math.Object(
        PARENT=networks.nets['dogecoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=10, # blocks
        IDENTIFIER='D0D1D2D3B2F68CD9'.decode('hex'),
        PREFIX='D0D3D4D541C11DD9'.decode('hex'),
        P2P_PORT=8555,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9555,
        BOOTSTRAP_ADDRS='p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
