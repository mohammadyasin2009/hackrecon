import requests
import random
import base64
import json
from datetime import datetime

def get_free_v2ray_configs():
    try:
        sources = [
            "https://raw.githubusercontent.com/freev2ray/freev2ray/master/README.md",
            "https://raw.githubusercontent.com/v2fly/free-servers/main/README.md",
            "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt"
        ]
        
        configs = []
        
        for url in sources:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    content = response.text
                    vmess_links = [line.strip() for line in content.split('\n') 
                                 if line.startswith('vmess://')]
                    
                    for link in vmess_links:
                        try:
                            b64 = link[8:]
                            padded = b64 + '=' * (4 - len(b64) % 4)
                            decoded = base64.b64decode(padded).decode('utf-8')
                            config = json.loads(decoded)
                            config['link'] = link
                            configs.append(config)
                        except:
                            continue
            except:
                continue
        
        return configs
    
    except Exception as e:
        print(f"khata dar daryaft kanfing ha {e}")
        return []

def generate_v2rayng_config(configs):
    """
    تولید کانفیگ مناسب برای V2RayNG
    """
    if not configs:
        return "kanfingi yaft nashod!"
    
    selected = random.choice(configs)
    config = {
        "v": "2",
        "ps": f"FreeServer-{datetime.now().strftime('%Y%m%d')}",
        "add": selected.get('add', ''),
        "port": selected.get('port', ''),
        "id": selected.get('id', ''),
        "aid": selected.get('aid', ''),
        "scy": selected.get('scy', 'auto'),
        "net": selected.get('net', 'tcp'),
        "type": selected.get('type', 'none'),
        "host": selected.get('host', ''),
        "path": selected.get('path', ''),
        "tls": selected.get('tls', ''),
        "sni": selected.get('sni', '')
    }
    

    json_str = json.dumps(config)
    b64 = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    vmess_link = f"vmess://{b64}"
    
    return vmess_link

def main():
    print("dar hal daryaft kanfing raygan.......")
    configs = get_free_v2ray_configs()
    
    if configs:
        print(f"\n tedad {len(configs)} kanfing peyda shod.")
        vmess_link = generate_v2rayng_config(configs)
        
        print("\nkanfing tolid shode baray shoma.")
        print(vmess_link)
        
        print("\nrahnemay vasl kardan kanfing:")
        print("1. v2rayng ra baz konid.")
        print("2. klick ray + bekonid.")
        print("3. 'Import from clipboard' ra entekhab konid")
        print("4.\ kanfing ra peyst konid.")
    else:
        print("kanfingi peyda nashod!")

if __name__ == "__main__":
    main()