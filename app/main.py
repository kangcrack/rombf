#Encrypt By Romi Afrizal (https://github.com/ROMI-AFRZL)

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))