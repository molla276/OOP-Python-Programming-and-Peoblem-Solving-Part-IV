class Phone:
    color = 'black'
    features = {'camera', 'water', 'can be used as a hammer'}

    def call(self):
        print('ring ring ring')
    
    def send_sms(self, num,text):
        sms = f'sending sms {text} to {num}'
        return sms

my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01675560811','I missed you miss you')
print(sms)