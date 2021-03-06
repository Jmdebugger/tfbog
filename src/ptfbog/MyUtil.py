# -*- coding:utf-8 -*- 
import md5
import base64
import urllib

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
        istr = urllib.quote(istr)
        istr = urllib.quote(istr)
        return buf

    @staticmethod
    def decrypt(key , istr):
        istr = urllib.unquote(istr)
        istr = urllib.unquote(istr)
        istr = base64.b64decode(istr)
        md5Key = MyUtils.getMD5(key)
        buf = ""
        for i in range(0 , len(istr)):
            buf =buf+ chr(ord(md5Key[i%len(md5Key)])^ord(istr[i]))
        return buf

    @staticmethod
    def sign(istr):
        return MyUtils.getMD5(istr)
    

if __name__ == "__main__":
    app_key = "0307cafd710cab421a0310b134bd4e4c"
    sig = "HUNQDgEbG19CRA8BBlMMVlUBV1IBVV1VCVcECAQDUlMDVgFRUlVbBg8FFQ1IQ1gARg0GCRJbPh0bFVBLQVwNXw8FEFtUVgxWCl8HDwVRSU1IQRYEQxIMCVcPURoIBFYEVVILUVxRChhkShVWQxFHFVIXAEMKGkcHSRZqTldHEVgJDxBbR1UXUxtKFVZDEVcIV0FfQwZZXVAPXw0AEEgfTEpDWgQEBlwXG1xMFUcOQABfPBEIXQRHXA1eAAAHGUBEDwUQW0daD1IMVgYHAVABWAVVXFcSTUcPVANcGggXWgdRVAJQVVAIUABQAQ4FQxhDWgAGCFRDX0QBXw0OAgVVCVdZClVRVQhXC18CARFNFgBDEzoXVRMWD1YIFwIQB0wBRE0QEwARVglMEl5YXUMOQwdbVUsIUVVEFURUW1FQEUJEWxA2DCRQRxVEWERsF1ETQAoKDxJbR1IXUhsKEBlARwMTQQgKDGYGVgJSFQlDBlEDQUlDVAQTD1oDalVdUQddRFsQIgoNVRVYAhcPA1ADTGdTVUMcQwQIXRRaUVZqC1VEWxBUUwZfBwxWUgVXVwNSVlMAQxxDFgNXAmpMW1gHE1xQBlRWUQBVAFUCGxEDVRVHBhcYEltHVwlWFxQQVwNSDQZADhAMXUcDVhsVURNVD1dBX0NzDgoKSQdRGAoFUwZLNQJRR04bDFQVXhUJQwBXA1NVVgFTV14BVAwNBBdOExEMUwJHWBtVCVYPBQFQAlULBQZDHEMRCVYKVlFWF1gTC0wEWV1UD1wBXhUbERJBEUMPDARCQ19EG0oXSEBaD14SCF0POg9cEVEJUxUJQ1MHER4Y"
    tjmod = "HUNQDgEbG19CRAAFB1MHUlAFUFQDUgBTDAACCgUNUFUCUFMFBlsOVQlfFQ1IQ1URQxARAEQER1xCRFRIQmoUVBQSWw4LQANHCkgEFR9DVRFDAAwFEltHUAFeAw4LDVoTG00QFQAQVAxXB0NSEVtvGhEQABJDCAoIUAIXAgMBVwJVWQtTU1YVR10TRVZHCFsPEVlUUQUcSR0bFVBLQVwNXw8FEFtUVgxWCl4OAwJVGENXFhcARAgKCBtcBEUeTkBCAxJBCAoMUAEbXAYDBlIHWQpXUFYcQwETSwdBUV1bQAtXHB4aRxFcFkoPWFlaBRZbAldQUgNZXFIAVRkaVkAQUBIIXQ9HWAgYZBsbFQdQVlEKWlQCBFEDAF9VUFpWAFBVVFYFVAQACV0LAwdVEVtPQ1ITFRJEABEDG1xOGlNFEm4QBEASDA1XRwNEAhkCTwBDH0EEEUACDAIbXBcOCg1UB19ZCkMYThsRXBRaXl0AQAQRWT4aEhIAFUoPWlZbUUALV1UHUlZaAFYIUBsVVxRGAEcKCg8SW1ReABtoRU8ZQFkDAFYEF0ADHhsSWENSDWsVWg4AQwpVUlQKURkaR1wGE1xDCldSVwlUCVQGAgpXAlgFQUlDWQwADxtcFwAEAlcBV1EAUFBbD1MAUBUbEQhXAloHR1sSWVxeD1YFDwoEWglSVQVQV1AAUA9EGxVSEUQ%252BRQYXElkOC0QDRAYWARdOExQEQQ4JF00MVggVDRFVDFEZW1VREk1HB1oFUEtBF1gTMQh0CEdOGwpKOUFSQRJdDl1BX0MET1FIC0QZGkRQEEIPDlw%252BBg1dABtcFQMAQxhDVwYTCFMEOgtWAlBUEA9AcgkOXhEEBhldCVcAGmdRBEMfQQQPVBMKD105XFwQD0AEUAVUA1BSXFddUAAEVlFRQx9BFgReBToSUAtQGggEVgRVUgpYUFoOSRsERVZdBRZbESAKDlwRBAIZXgUJBRg2AVZDHkMMD0oMG1wVAwVRBFEEUldTCFlXXwxQFxQQQg9QBUMIQ1VSCV0LVAYBB1lSAhFPRxVfDgkFUAIXAhADWglQVwtZXUAVR0oTR0dfCFETEVlHQxxDFRRWC1pMW1oMbgsERgkKBhtfGwFRFU4c"
    tjmod1 = "HUNQDgEbG19CRAAFB1MHUlAFUFQDUgBTDAACCgUNUFUCUFMFBlsOVQlfFQ1IQ1gARg0GCRJbPh0bFVBLQVwNXw8FEFtUVgxWCl4AAwFTSTwfQQQRQBIRB00DFwJJFwNBFj5EBBcRUApXRA0VAE8HQx9BBBFAAgwCG1wXDgoNVAdfWQpDGB9ESRsOUlZXBEZDCRhHFV8VBApmElxVVxdYBVNRBVJJQEwMXUQNFQtXA1QDUlVTAVRcUA9fAxoeFwtcAwgQW0daD1IMVgYHAVABWAVVXFcSTUcPWgVcXBAPQAlfWQRRVVUBVAFeAwMEUAZTClZTQxxDBBZJOUNdQEYLXghDCENXTAlHFURFUkAOWBRHCgoPEltHUgFWHwACBUAdRABRAgARSkcDRGBedQgWTREMFj5GBBcVUAlbGggXVh9STwBDSUBPAEsVXlhdPlcOVwZHWxJTVVYbShdcV0MLUgM%252BXw4BB1VHA0R0WFwNRABXQ11RAVZIMglWFxQQVAxVFA5bBToLXUcDRAIBVwdWVAMGVwUGVlYDCQMXFBBGB18CPkYICAcbXwhSAgQAWQNVAVBJQ1IAERJcFEwaCBdbAURNEAMEAVICSwlCWVdDDlEfQQcTUQ8BRANEdlddWRJQAkEKUVRVFDEJVhUbEQhZElpBX0MEV1VWCVEECgANWgNfVARDSUBOCFgFFQ0RUQRRC1FXUAZVXQBaRBkaRloNXQUIVkNfQFRID14PAQVYDFkRT0cSRREVClADRxoIF0AdRBFADggNTQxWCGhaVhVcDldBX0NXB0cbRA%253D%253D"
    tjmod2 = "HUNQDgEbG19CRAAFB1MHUlAFUFQDUgBTDAACCgUNUFUCUFMFBlsOVQlfFQ1IQ1URQxARAEQER1xCRFRIQmoUVBQSWw4LQANHCkgEFR9DVRFDAAwFEltHUAFeAw4LDVoTG00QFQAQVAxXB0NSEVtvGhEQABJDCAoIUAIXAgMBVwJVWQtTU1YVR10TRVZHCFsPEVlUUQUcSR0bFVBLQVwNXw8FEFtUVgxWCl4OAwJVGENXFhcARAgKCBtcBEUeTkBCAxJBCAoMUAEbXAYDBlIHWQpXUFYcQwETSwdBUV1bQAtXHB4aRxFcFkoPWFlaBRZbAldQUgNZXFIAVRkaVkAQUBIIXQ9HWAgYZBsbFQdQVlEKWlQCBFEDAF9VUFpWAFBVVFYFVAQACV0LAwdVEVtPQ1ITFRJEABEDG1xOGlNFEm4QBEASDA1XRwNEAhkCTwBDH0EEEUACDAIbXBcOCg1UB19ZCkMYThsRXBRaXl0AQAQRWT4aEhIAFUoPWlZbUUALV1UHUlZaAFYIUBsVVxRGAEcKCg8SW1ReABtoRU8ZQFkDAFYEF0ADHhsSWENSDWsVWg4AQwpVUlQKURkaR1wGE1xDCldSVwlUCVQGAgpXAlgFQUlDWQwADxtcFwAEAlcBV1EAUFBbD1MAUBUbEQhXAloHR1sSWVxeD1YFDwoEWglSVQVQV1AAUA9EGxVSEUQ%252BRQYXElkOC0QDRAYWARdOExQEQQ4JF00MVggVDRFVDFEZW1VREk1HB1oFUEtBF1gTMQh0CEdOGwpKOUFSQRJdDl1BX0MET1FIC0QZGkRQEEIPDlw%252BBg1dABtcFQMAQxhDVwYTCFMEOgtWAlBUEA9AcgkOXhEEBhldCVcAGmdRBEMfQQQPVBMKD105XFwQD0AEUAVUA1BSXFddUAAEVlFRQx9BFgReBToSUAtQGggEVgRVUgpYUFoOSRsERVZdBRZbESAKDlwRBAIZXgUJBRg2AVZDHkMMD0oMG1wVAwVRBFEEUldTCFlXXwxQFxQQQg9QBUMIQ1VSCV0LVAYBB1lSAhFPRxVfDgkFUAIXAhADWglQVwtZXUAVR0oTR0dfCFETEVlHQxxDFRRWC1pMW1oMbgsERgkKBhtfGwFRFU4c"
    tjmod3 = "HUNQDgEbG19CRAAFB1MHUlAFUFQDUgBTDAACCgUNUFUCUFMFBlsOVQlfFQ1IQ1URQxARAEQER1xCRFRIQmoUVBQSWw4LQANHCkgEFR9DVRFDAAwFEltHUAFeAw4LDVoTG00QFQAQVAxXB0NSEVtvGhEQABJDCAoIUAIXAgMBVwJVWQtWXFEVR10TRVZHCFsPEVlUHBwaRxVcFUZRXVsLVURbA1VQUQpdAF8ABR9DUBRBAhEIXw9HXA5eSGVPSE4TDgRTBQAQG19CRENYRwBYPkcKCAQSW1FRDlUMFBBAC1VEWxBZU1UMVQhWBQYGWAJXClVHTRIICANQRA8aCgNVBFZQAlNUVwBTD18BFR9DXQJQCgFDCkNdXwFQBQgFDVMJXlUGVlRQC1wMUBUbEQBEEWwVABNDCAoIG1wXCxwGQB1EE1cSCg5MEVAJWRUJQwBZA0ldUQBDSURYBVZdQUZAC0Q2WycMQBVHVhVoQVYTRwhcDUdbElVLUhdUFxQQQwdDFQhdDzoBVgFcRA0VB1IWTREHABdZAgA5VAlRXV4XWBMlDl0NFQNdRQFWBgAeNQRREU9HAF4FFwlQAmpRVhdYE1NXVgcHVwkACwIBAAAEBAQRT0cSVQ8BOU0PWF0QD1MFU1IBWFVSAVwVRFVFUg9QQwlBJg5fDRUHXUYNCAMCT2VWURBNRwtUFlBEDRUHVwRRA1RUUwJZXVQAUwMaHhcVXAcCEFtHUglVAVQFBgVVDAdQQUlDRA4KCloPURoIF1QJXlcEWF1aG0kbFUJHQw1dBEFBX0MSTUcWSwlYV0ZcDV85DFcVDQ1dRwNEUFERHEk%253D"
    tjmod4 = "HUNQDgEbG19CRAMGUVENWAIAUVFWBwNVXARRDQBRUAZRVFMDVVoLAAkEFQ1IQ1gARg0GCRJbPh0bFVBLQVwNXw8FEFtUVgxWCl4OBABQSTwfQQQRQBIRB00DFwJJFwNBFj5EBBcRUApXRA0VBk8FTwdBSUNRERUFUAIXAhADWglQVwtZXUBEGERKFV9WAFAEQUFfGhIVChJYCmpMW1gHE1xVBFhdUxVHTA9TFQlDDFcEVlVQAFNUUwBQAwEEF04TDwxXCEdYG10PUQIHAlEGUAZaU1cJV0dKGw9WW1tRQAtEWQtZU1IJUgFXDw8HVQNQAVFcVAZDSURYFkVnRFAQQg8OXENfQAtLCUQbFUEERw5fFhEIXw9HXBtSDQgYDVIBRE0QAAYBXBZKRA0VZAhyCBFPRw5DPhMDSxVcV1wXWBNSTwZPV0AVR08DRURaDlo%252BUAwBBBJbR1QJVhcUEFEHRw8CVz4IDV0AVUQNFXAOWw1DAgFBCFFUURQyBQgQGUBQCAVADgwGZgxdRA0VBldQB1FWVQQCBVNRCgMFXRAZQEIDD1Y%252BEQtUABtcBgMGUgdZClBWUxxDBwdNElBKSxdYE19WEE1HAFgGUgFFWEYPUEMJU0lDUhMECF1EDxpxWg1dFgBWQV1SCFIUMgcHEU0WCF4QDEMKQ1FQCVYFDwMHUAleUwtUU0AVR04LVlQRWxZRA1NdUwJQU1IBAFYaHhcWXgkNUQgBQANHVEsBDwtXAlgLW0dNEhIQFkkKXF1AF1gTRE0QERcNVApND1hZbAxRFVsMAUMKQwIAGxtI"
    md1 = "TkMCQxNtFQcUQQtfXxYCGlYcUhdIFAQVFjpcB1BDWRAHAFoDVFEAW1IDUFRUAA8LAAdVBV1VXAFT%250AXQlbAVlQURdNQUAXUxEWOUEWUVxEGgJQBlEGVw9VVFNQHUEGCQJcWwQPEVkQDk9QCloGBw0AAEMe%250ARkMBRBYMCQtuAAoFBhAPQ1sAQU8%253D%250A"
    
    print MyUtils.decrypt(app_key,tjmod)
    #print MyUtils.sign("we are together:parker love roosee!")

