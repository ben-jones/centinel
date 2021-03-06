### Centinel

Centinel is a tool used to detect network interference and internet
censorship.

#### Install and usage
##### Debian
    $ sudo apt-get install python-pip libssl-dev swig python-dev libffi-dev tcpdump
    $ sudo pip install -U dnspython requests argparse m2crypto pyopenssl ndg-httpsclient pyasn1 pip
    $ sudo pip install centinel-dev
    $ centinel-dev

##### OSX
    $ sudo pip install centinel-dev
    $ centinel-dev

##### Latest development version
    * git clone https://github.com/projectbismark/centinel.git
    # install dnspython, requests
    * python centinel.py

#### Supported platforms

    * Linux/OS X
    * BISmark Routers
    * Android

### Acknowledgements

* Ben Jones
* Abbas Razaghpanah
* Sathya Gunasekaran
* Nick Feamster
* Phillipa Gill
* Sam Burnett
