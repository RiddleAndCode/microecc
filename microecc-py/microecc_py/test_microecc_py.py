import pytest
import binascii
import hashlib
import re
# import os
from . import MicroECCPy

# LIBRARY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libmicroecc.so')


class TestMicroECCPy:

    def test__public_from_private(self):

        m = MicroECCPy()  # library_path=LIBRARY_PATH)

        public_key, private_key = m.get_random_keypair()

        public_key2 = m.get_public_from_private(private_key)

        assert(public_key == public_key2)

    def test__shared_secret(self):

        m = MicroECCPy()

        public_key1, private_key1 = m.get_random_keypair()
        public_key2, private_key2 = m.get_random_keypair()

        secret1 = m.generate_shared_secret(public_key1, private_key2)
        secret2 = m.generate_shared_secret(public_key2, private_key1)

        assert(secret1 == secret2)

    def test__compress__decompress(self):

        m = MicroECCPy()

        public_key, private_key = m.get_random_keypair()

        public_key_compressed = m.compress(public_key)

        assert(re.match('(02|03)[0-9A-F]+', public_key_compressed, re.I))

        public_key_uncompressed = m.decompress(public_key_compressed)

        assert(public_key_uncompressed == public_key)

    @pytest.mark.skip()
    def test__compress__decompress_with_04_prefix(self):

        m = MicroECCPy()

        public_key, private_key = m.get_random_keypair()

        # add "04" prefix
        public_key = f'04{public_key}'

        """
        04F609F1699260467E9A3E6005E10EFDC82E7FE56143D92F5AE4451949A4DCB 48ABC027B59D619B7735D3FEA0514278F97579BD1F6D4B3CAE55D07A00CF0CF85

        04F609F1699260467E9A3E6005E10EFDC82E7FE56143D92F5AE4451949A4DCB 4936FF220204BF065B0FFA269FBF1066FFB5CC3891FF836A5D419C839690901732B
        """

        public_key_compressed = m.compress(public_key)

        assert(re.match('(02|03)[0-9A-F]+', public_key_compressed, re.I))

        public_key_uncompressed = m.decompress(public_key_compressed)

        assert(public_key_uncompressed == public_key)

    def test__sign_and_verify(self):

        m = MicroECCPy()

        public_key, private_key = m.get_random_keypair()

        message = 'Hello, world!'
        challenge = hashlib.sha256(message.encode('utf8')).digest()
        signature = m.sign(private_key, message)

        challenge_ = binascii.hexlify(challenge).upper()

        assert(m.verify(public_key, challenge_, signature))

    def test__sign_and_not_valid(self):

        m = MicroECCPy()

        public_key, private_key = m.get_random_keypair()

        message = 'Hello, world!'
        signature = m.sign(private_key, message)

        message2 = 'Hello, world!!'
        challenge2 = hashlib.sha256(message2.encode('utf8')).digest()
        challenge_ = binascii.hexlify(challenge2).upper()

        assert(not m.verify(public_key, challenge_, signature))
