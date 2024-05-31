#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> crypto util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> CrypUtil
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64


class CrypUtil:
    """
    _crypto module_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def random_bytes(cls, bit_num: int = 16) -> bytes:
        """
        _return random bytes_

        Args:
            bit_num (int, optional): _bits of num_. Defaults to 16.

        Returns:
            bytes: _nothing_
        """
        if isinstance(bit_num, int) is False:
            bit_num = 16
            
        return Random.new().read(bit_num)
    
    @classmethod
    def md5_digest(cls, src_bytes: bytes = b"") -> bytes:
        """
        _md5 digest_

        Args:
            src_bytes (bytes, optional): _source bytes_. Defaults to b"".

        Returns:
            bytes: _bytes. Defaults to b""_
        """
        if isinstance(src_bytes, bytes) is False:
            src_bytes = b""

        return hashlib.md5(src_bytes).digest()
    
    @classmethod
    def md5_hexdigest(cls, src_bytes: bytes = b"") -> bytes:
        """
        _md5 hexdigest_

        Args:
            src_bytes (bytes, optional): _source bytes_. Defaults to b"".

        Returns:
            bytes: _bytes. Defaults to b""_
        """
        if isinstance(src_bytes, bytes) is False:
            src_bytes = b""

        return hashlib.md5(src_bytes).hexdigest()
    
    @classmethod
    def base64_encode(cls, src_bytes: bytes = b"") -> bytes:
        """
        _base64 encode_

        Args:
            src_bytes (bytes, optional): _source bytes_. Defaults to b"".

        Returns:
            bytes: _bytes. Defaults to b""_
        """
        if isinstance(src_bytes, bytes) is False:
            src_bytes = b""

        return base64.b64encode(src_bytes)
        
    @classmethod
    def base64_decode(cls, src_str: str = "") -> bytes:
        """
        _base64 decode_

        Args:
            src_str (str, optional): _source string_. Defaults to "".

        Returns:
            bytes: _bytes. Defaults to b""_
        """
        if isinstance(src_str, str) is False:
            src_str = ""

        return base64.b64decode(src_str)
    
    @classmethod
    def pad_data(cls, src_bytes: bytes = b"") -> bytes:
        """
        _padding data_

        Args:
            src_bytes (bytes, optional): _source bytes_. Defaults to b"".

        Returns:
            bytes: _bytes. Defaults to b""_
        """
        if isinstance(src_bytes, bytes) is False:
            src_bytes = b""

        return pad(src_bytes, AES.block_size)
    
    @classmethod
    def unpad_data(cls, src_bytes: bytes = b"") -> bytes:
        """
        _unpadding data_

        Args:
            src_bytes (bytes, optional): _source bytes_. Defaults to b"".

        Returns:
            bytes: _bytes. Defaults to b""_
        """
        if isinstance(src_bytes, bytes) is False:
            src_bytes = b""

        return unpad(src_bytes, AES.block_size)
    
    @classmethod
    def ecb_mode(cls, src_key: bytes = b"") -> object:
        """
        _ecb mode_

        Args:
            src_key (bytes, optional): _encrypt key_. Defaults to b"".

        Returns:
            object: _nothing_
        """
        if isinstance(src_key, bytes) is False:
            src_key = b""

        return AES.new(key=src_key, mode=AES.MODE_ECB)
    
    @classmethod
    def cbc_mode(cls, src_key: bytes = b"", src_iv: bytes = b"") -> object:
        """
        _cbc mode_

        Args:
            src_key (bytes, optional): _encrypt key_. Defaults to b"".
            src_iv (bytes, optional): _encrypt iv_. Defaults to b"".

        Returns:
            object: _nothing_
        """
        if isinstance(src_key, bytes) is False:
            src_key = b""
        if isinstance(src_iv, bytes) is False:
            src_iv = b""

        return AES.new(key=src_key, mode=AES.MODE_CBC, iv=src_iv)
    
    @classmethod
    def encrypt_account(cls, src_data: str = "", src_key: str = "") -> str:
        """
        _encrypt account_

        Args:
            src_data (str, optional): _encrypt string_. Defaults to "".
            src_key (str, optional): _encrypt key_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            src_data = str(src_data)
            src_key = str(src_key)
            if len(src_key) != 16:
                src_key = "0011001100110011"

            padding_data = cls.pad_data(src_data.encode("utf-8"))
            aes_ecb = cls.ecb_mode(src_key.encode("utf-8"))
            encrypt_data = aes_ecb.encrypt(padding_data)
            bytes_data = cls.base64_encode(encrypt_data)

            return bytes_data.decode("utf-8")

        except Exception:
            
            return ""
            
    @classmethod
    def decrypt_account(cls, src_data: str = "", src_key: str = "") -> str:
        """
        _decrypt account_

        Args:
            src_data (str, optional): _decrypt string_. Defaults to "".
            src_key (str, optional): _decrypt key_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            src_data = str(src_data)
            src_key = str(src_key)
            if len(src_key) != 16:
                src_key = "0011001100110011"

            bytes_data = cls.base64_decode(src_data.encode("utf-8"))
            aes_ecb = cls.ecb_mode(src_key.encode("utf-8"))
            decrypt_data = aes_ecb.decrypt(bytes_data)
            unpadding_data = cls.unpad_data(decrypt_data)

            return unpadding_data.decode("utf-8")
        
        except Exception:
            
            return ""

