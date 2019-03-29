#import uuid
import uuid


# generate a uuid in 32 hex numbers also capitalize all alphabets
# e.g. F0B4B8FAE59F11E89B0B88D7F6C60FA7
# return as string
def random_uuid():
    result = str(uuid.uuid1().hex).upper()
    return result
    print(result)


# make a UUID from a 16-byte string
# turn 16 bytes uuid to hex uuid string
# turn b'9\x9a\xc9>\xe5\xa1\x11\xe8\xb1\x06\x88\xd7\xf6\xc6\x0f\xa7' to  399AC93EE5A111E8B10688D7F6C60FA7
def bytes_to_hex(_16_bytes):
    _16_bytes_str = str(uuid.UUID(bytes=_16_bytes).hex.upper())
    return _16_bytes_str

result2 = random_uuid()
print(result2)