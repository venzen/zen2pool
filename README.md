This is a modified version of forrestv's p2pool https://github.com/forrestv/p2pool
zen2pool is P2Pool node software and optimized for fast block-time altcoins 
based on the scrypt and scrypt-N algorithm


Linux
-------------------------

Requirements:
-------------------------
Generic:
* Bitcoin >=0.8.6
* Python 2.7
* Twisted >=10.0.0

Ubuntu Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web

In order to run zen2pool with scrypt-based altcoins, you would need to build and install
the ltc_scrypt module that includes the scrypt proof of work code that Litecoin and its 
clones use for hashes.

Install the scrypt modules. Even if you're not intending to mine Litecoin or Vertcoin,
these are the scrypt algorithms that all scrypt-based altcoins require:

    cd litecoin_scrypt
    sudo python setup.py install

    cd ../vertcoin_scrypt
    sudo python setup.py install

Running zen2pool:
-------------------------
To use zen2pool, you need at least 2 prerequisites:

1) a locally running instance of the altcoin daemon you want to mine.
2) configuration settings for the altcoin must be included in the files
	p2pool/networks.py and p2pool/bitcoin/networks.py

Once configured the relevant altcoin configuration can be invoked at runtime:

    python run_zen2pool.py --net myaltcoin

Then run your mining worker software, connecting to 127.0.0.1 on the worker port using
a wallet address as your username and any random password, e.g.:

    cgminer --scrypt -o http://127.0.0.1:8810 -u mywalletaddress -p randompassword

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward the p2p port (defined in networks.py) to the host running P2Pool.

Run for additional options.

    python run_zen2pool.py --help

Donations towards further development:
-------------------------
    1E3UUNxdZUzoA2RseKhXDCwiVCmPbxU69s

Official P2Pool wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

zen2pool Resource Library :
-------------------------
http://wp.me/p3EnMP-3lF

Notes for Windows:
=========================
Requirements:
-------------------------

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Scrypt module:
-------------
Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

------------------------

original P2Pool notes:

Sponsors:
---------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
* Thanks to forrestv who's hard work makes P2Pool possible

