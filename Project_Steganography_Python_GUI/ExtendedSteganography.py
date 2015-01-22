import math
import sys
import re
import string
import base64
import os
from PIL import Image
from Crypto.Cipher import AES
import Steganography

class AesMessage(Steganography.Message):
    def __init__(self, **kwargs):
        if len(kwargs) == 3:
            if "filePath" not in kwargs:
                raise ValueError("Missing argument of filePath")
            elif kwargs["filePath"] == "":
                raise ValueError("filePath can not be Null")
            elif "messageType" not in kwargs:
                raise ValueError("Missing argument of messageType")
