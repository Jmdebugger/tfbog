# -*- coding:utf-8 -*- 
import md5
import base64
app_key = "0307cafd710cab421a0310b134bd4e4c"
sig = "HUNQDgEbG19CRA8BBlMMVlUBV1IBVV1VCVcECAQDUlMDVgFRUlVbBg8FFQ1IQ1gARg0GCRJbPh0bFVBLQVwNXw8FEFtUVgxWCl8HDwVRSU1IQRYEQxIMCVcPURoIBFYEVVILUVxRChhkShVWQxFHFVIXAEMKGkcHSRZqTldHEVgJDxBbR1UXUxtKFVZDEVcIV0FfQwZZXVAPXw0AEEgfTEpDWgQEBlwXG1xMFUcOQABfPBEIXQRHXA1eAAAHGUBEDwUQW0daD1IMVgYHAVABWAVVXFcSTUcPVANcGggXWgdRVAJQVVAIUABQAQ4FQxhDWgAGCFRDX0QBXw0OAgVVCVdZClVRVQhXC18CARFNFgBDEzoXVRMWD1YIFwIQB0wBRE0QEwARVglMEl5YXUMOQwdbVUsIUVVEFURUW1FQEUJEWxA2DCRQRxVEWERsF1ETQAoKDxJbR1IXUhsKEBlARwMTQQgKDGYGVgJSFQlDBlEDQUlDVAQTD1oDalVdUQddRFsQIgoNVRVYAhcPA1ADTGdTVUMcQwQIXRRaUVZqC1VEWxBUUwZfBwxWUgVXVwNSVlMAQxxDFgNXAmpMW1gHE1xQBlRWUQBVAFUCGxEDVRVHBhcYEltHVwlWFxQQVwNSDQZADhAMXUcDVhsVURNVD1dBX0NzDgoKSQdRGAoFUwZLNQJRR04bDFQVXhUJQwBXA1NVVgFTV14BVAwNBBdOExEMUwJHWBtVCVYPBQFQAlULBQZDHEMRCVYKVlFWF1gTC0wEWV1UD1wBXhUbERJBEUMPDARCQ19EG0oXSEBaD14SCF0POg9cEVEJUxUJQ1MHER4Y"

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
    print MyUtils.decrypt(app_key,sig)

