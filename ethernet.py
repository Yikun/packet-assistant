import pcapy
import binascii


class Ethernet:

    def __init__(self):
        self.dev = None
        self.sendcnt = 0

    def devices(self):
        return pcapy.findalldevs()

    def open(self, device):
        self.dev = pcapy.open_live(str(device), 100, 1, 1000)

    def send(self, data):
        if self.dev:
            self.dev.sendpacket(data)
            self.sendcnt += 1
        else:
            print "Please open a device before send."

    def sendHex(self, hexstr):
        data = binascii.unhexlify(''.join(hexstr.split()))
        self.send(data)

    def address(self):
        return self.dev.getnet()

    def sendtimes(self):
        return self.sendcnt

if __name__ == '__main__':
    ethnet = Ethernet()
    # Get the first device of devices
    device = ethnet.devices()[0]
    print "First device: " + device
    # Open device
    ethnet.open(device)
    # Send the L2 Packet
    # Destination Address = 61:62:63:64:65:66
    # Source Address      = 67:68:69:6a:6b:6c
    # Protocol Type       = 0x6d6e
    ethnet.send("abcdefghijklmn")
    # equal to
    ethnet.sendHex("61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e")
    # Get address
    address = ethnet.address()
    print "Address: " + address
