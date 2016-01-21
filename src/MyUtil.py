# -*- coding:utf-8 -*- 
import md5
import base64
app_key = "0307cafd710cab421a0310b134bd4e4c"
class MyUtils:
    def __init__(self):
        pass
        
    @staticmethod
    def getMD5(istr):
        m = md5.new()   
        m.update(istr)   
        return m.hexdigest()

    @staticmethod
    def encrypt(key , istr):
        md5Key = MyUtils.getMD5(key)
        buf = ""
        for i in range(0 , len(istr)):
            buf =buf+ chr(ord(md5Key[i%len(md5Key)])^ord(istr[i]))
        buf = base64.b64encode(buf)
        return buf

    @staticmethod
    def decrypt(key , istr):
        istr = base64.b64decode(istr)
        md5Key = MyUtils.getMD5(key)
        buf = ""
        for i in range(0 , len(istr)):
            buf =buf+ chr(ord(md5Key[i%len(md5Key)])^ord(istr[i]))
        return buf
    
        


if __name__ == "__main__":
    print MyUtils.decrypt(app_key,MyUtils.encrypt(app_key , "你好world\n{d:23}"))

