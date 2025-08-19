import requests
import SignerPy
from typing import Dict, Any
import secrets

class TikTokAccountCreator:
    def __init__(self):
        self.csrf = secrets.token_hex(16)
        self.session = requests.Session()
        self.base_params = {
            "passport-sdk-version": "6031990",
            "device_platform": "android",
            "os": "android",
            "ssmix": "a",
            "cdid": "a90f0ed5-8028-413e-a00d-77e931779d00",
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "370805",
            "version_name": "37.8.5",
            "manifest_version_code": "2023708050",
            "update_version_code": "2023708050",
            "ab_version": "37.8.5",
            "resolution": "900*1600",
            "dpi": "240",
            "device_type": "NE2211",
            "device_brand": "OnePlus",
            "language": "en",
            "os_api": "28",
            "os_version": "9",
            "ac": "wifi",
            "is_pad": "0",
            "current_region": "TW",
            "app_type": "normal",
            "sys_region": "US",
            "last_install_time": "1752871588",
            "mcc_mnc": "46692",
            "timezone_name": "Asia/Baghdad",
            "carrier_region_v2": "466",
            "residence": "TW",
            "app_language": "en",
            "carrier_region": "TW",
            "timezone_offset": "10800",
            "host_abi": "arm64-v8a",
            "locale": "en-GB",
            "ac2": "wifi",
            "uoo": "0",
            "op_region": "TW",
            "build_number": "37.8.5",
            "region": "GB",
            "iid": "7528525992324908807",
            "device_id": "7528525775047132680",
            "openudid": "7a59d727a58ee91e",
            "support_webview": "1",
            "reg_store_region": "tw",
            "user_selected_region": "0",
            "okhttp_version": "4.2.210.6-tiktok",
            "use_store_region_cookie": "1",
            "app_version": "37.8.5"
        }
        
        self.base_headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'x-tt-pba-enable': "1",
            'x-bd-kmsv': "0",
            'x-tt-dm-status': "login=1;ct=1;rt=8",
            'x-tt-passport-csrf-token': self.csrf,
            'sdk-version': "2",
            'passport-sdk-settings': "x-tt-token",
            'passport-sdk-sign': "x-tt-token",
            'x-tt-bypass-dp': "1",
            'oec-vc-sdk-version': "3.0.5.i18n",
            'x-vc-bdturing-sdk-version': "2.3.8.i18n",
            'x-tt-request-tag': "n=0;nr=011;bg=0"
        }
        
        self.cookies = {
            "install_id": "7528525992324908807",
            "passport_csrf_token": self.csrf,
            "passport_csrf_token_default": self.csrf,
        }
        self.session.cookies.update(self.cookies)
    
    @staticmethod
    def xor_encrypt(string: str) -> str:
        return "".join([hex(ord(c) ^ 5)[2:] for c in string])
    
    def update_timestamps(self, params: Dict[str, Any]) -> Dict[str, Any]:
        import time
        current_time = int(time.time() * 1000)
        params["_rticket"] = str(current_time)
        params["ts"] = str(current_time // 1000)
        return params
    
    def send_code_request(self, email: str, password: str) -> Dict[str, Any]:
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"
        
        params = self.update_timestamps(self.base_params.copy())
        payload = {
            'rules_version': "v2",
            'password': self.xor_encrypt(password),
            'account_sdk_source': "app",
            'mix_mode': "1",
            'multi_login': "1",
            'type': "34",
            'email': self.xor_encrypt(email),
            'email_theme': "2"
        }
        
        signature = SignerPy.sign(params=params, payload=payload, cookie=self.cookies)
        
        headers = self.base_headers.copy()
        headers.update({
            'X-SS-STUB': signature['x-ss-stub'],
            'X-SS-REQ-TICKET': signature['x-ss-req-ticket'],
            'X-Ladon': signature['x-ladon'],
            'X-Khronos': signature['x-khronos'],
            'X-Argus': signature['x-argus'],
            'X-Gorgon': signature['x-gorgon'],
        })
        
        response = self.session.post(url, data=payload, headers=headers, params=params)
        return response.json()
    
    def verify_code(self, email: str, code: str, password: str) -> Dict[str, Any]:
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/register_verify_login/"
        
        params = self.update_timestamps(self.base_params.copy())
        payload = {
            'birthday': "2002-02-24",
            'fixed_mix_mode': "1",
            'code': self.xor_encrypt(code),
            'account_sdk_source': "app",
            'mix_mode': "1",
            'multi_login': "1",
            'type': "34",
            'email': self.xor_encrypt(email),
            'password': self.xor_encrypt(password)
        }
        
        signature = SignerPy.sign(params=params, payload=payload, cookie=self.cookies)
        
        headers = self.base_headers.copy()
        headers.update({
            'X-SS-STUB': signature['x-ss-stub'],
            'X-SS-REQ-TICKET': signature['x-ss-req-ticket'],
            'X-Ladon': signature['x-ladon'],
            'X-Khronos': signature['x-khronos'],
            'X-Argus': signature['x-argus'],
            'X-Gorgon': signature['x-gorgon'],
        })
        response = self.session.post(url, data=payload, headers=headers, params=params)
        return response.json()
    
    def save_account(self, email: str, password: str, response_data: Dict[str, Any]):
        try:
            session_id = response_data['data']['session_key']
            username = response_data['data']['name']
            
            with open("account.txt", "a", encoding="utf-8") as f:
                f.write(f"email: {email} | password: {password} | sessionid: {session_id} | username: {username}\n")
            
            with open("session.txt", "a", encoding="utf-8") as f:
                f.write(session_id + "\n")
                
            print(f"Account created successfully! Session ID: {session_id}")
        except Exception as e:
            print(e)

def main():
    creator = TikTokAccountCreator()
    email = input("[-] Enter email: ")
    password = input("[-] Enter password: ")
    
    print("[!] Sending verification code...")
    response = creator.send_code_request(email, password)
    
    if "email_ticket" in str(response):
        print("[!] Verification code sent successfully!")
    else:
        print("Error sending verification code:", response)
        return
    
    code = input("Enter verification code: ")
    print("[!] Verifying code and creating account...")
    
    response = creator.verify_code(email, code, password)
    if response.get('data') and 'session_key' in response['data']:
        creator.save_account(email, password, response)
    else:
        print("Account creation failed:", response)

if __name__ == "__main__":
    main()
