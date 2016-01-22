class Phone:
    
    def __init__(self):
        pass

    def installApp(app):
        if app not in self.apps:
            self.apps

    def uninstallApp(app):
        pass

    
        
    


class PhoneManager:
    @staticmethod
    def randomGenPhone():
        phone = Phone()
        phone.imei = "12333"
        phone.imsi = "xxxx"
        
        return phone
        

if __name__ == "__main__":
    phone = PhoneManager.randomGenPhone()
    
    print vars(phone)
    
