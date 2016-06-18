#!/usr/bin/env python
import dns.resolver
import netifaces
import socket


def do_dns_lookup(fqdn):
    """
    Do an A record lookup and return the first result.
    If no result is find, return False.
    """

    lookup = False
    try:
        lookup = dns.resolver.query(fqdn, 'A')
    except:
        return False

    if lookup:
        for r in lookup:
            return r


def get_iface_ip(iface):
    addrs = netifaces.ifaddresses(iface)
    return addrs[netifaces.AF_INET][0]['addr']


def main():
    fqdn = socket.getfqdn()
    dns_response = do_dns_lookup(fqdn)
    eth0_ip = get_iface_ip('eth0')

    if dns_response == eth0_ip:
        print True
    else:
        print False


if __name__ == "__main__":
    main()
