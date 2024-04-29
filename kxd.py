import requests
import re
import os
import json

# 假设你的环境变量中的cookies是以字符串形式提供的，需要转换为JSON格式
# 从环境变量中获取cookies字符串
cookies_str = str(os.environ.get("kxdck"))
'''

cookies 格式示例：


    {"G1NZ_2132_saltkey": "",
    "G1NZ_2132_lastvisit": "",
    "G1NZ_2132_sid": "",
    "G1NZ_2132_pc_size_c": "",
    "G1NZ_2132_popadv": "",
    "G1NZ_2132_ulastactivity": "",
    "G1NZ_2132_auth": "",
    "G1NZ_2132_lastcheckfeed": "",
    "G1NZ_2132_lip": "",
    "G1NZ_2132_connect_is_bind": "0",
    "G1NZ_2132_nofavfid": "",
    "G1NZ_2132_myrepeat_rr": "",
    "G1NZ_2132_dsu_amuppered": "",
    "G1NZ_2132_dsu_amupper": "",
    "G1NZ_2132_lastact": ""}


'''
# 将cookies字符串转换为字典
cookies_dict = json.loads(cookies_str)

# 构建请求所需的URL、headers和cookies
burp0_url = "https://www.kxdao.net:443/plugin.php?id=dsu_amupper&ppersubmit=true&formhash=22c9dcd7&infloat=yes&handlekey=dsu_amupper&inajax=1&ajaxtarget=fwin_content_dsu_amupper"
burp0_headers = {
    # ... 你的headers ...
}
burp0_cookies = cookies_dict

# 发送请求
a = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

# 尝试从响应中提取签到信息
match = re.search(r"errorhandle_dsu_amupper\('(.*)', \{\}\)", a.text)
if match:
    extracted_text = match.group(1)
    print(extracted_text)  # 输出签到结果
else:
    print("签到失败")