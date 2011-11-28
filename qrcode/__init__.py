from qrcode.main import QRCode
from qrcode.constants import *


def run_example(data="http://www.lincolnloop.com", *args, **kwargs):
    """
    Build an example QR Code and display it.
    """
    qr = QRCode(*args, **kwargs)
    qr.add_data(data)

    im = qr.make_image()
    im.show()


if __name__ == '__main__':
    import sys
    run_example(*sys.argv[1:])
