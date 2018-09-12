
                            # 仅用该文件进行代码保存 #



# 7.3 Splash 负责均衡配置

# 多台机器 多个服务器 多个任务

### 配置负载均衡
'''
http {
    upstream splash {
        least_conn;# 适用于请求处理时间长短不一造成服务器过载的情况;无状态的服务
        server 41.159.27.223:8050;
        server 192.168.99.100:8050;
        server 55.54.94.01:8050;
        server 94.94.91.62:8050;
    }
    server {
        listen 8050;
        location / {
            proxy_pass http://splash;
        }
    }
}


# 配置权重
    upstream splash {
        server 41.159.27.223:8050 weight=4;
        server 192.168.99.100:8050 weight=2;
        server 55.54.94.01:8050 weight=6;
        server 94.94.91.62:8050 weight=1;
    }

# IP散列负载均衡；有状态的服务
    upstream splash {
        ip_hash
        server 41.159.27.223:8050 weight=4;
        server 192.168.99.100:8050 weight=2;
        server 55.54.94.01:8050 weight=6;
        server 94.94.91.62:8050 weight=1;
    }


### 配置认证
http {
    upstream splash {
        least_conn;
        server 41.159.27.223:8050;
        server 192.168.99.100:8050;
        server 55.54.94.01:8050;
        server 94.94.91.62:8050;
    }
    server {
        listen 8050;
        location / {
            proxy_pass http://splash;
            auth_basic "Restricted";
            auth_basic_user_file /etc/nginx/comf.d/.htpasswd;
        }
    }
}
# 需要使用htpasswd命令创建一个用户名为admin 的文件
htpasswd -c .htpasswd admin
# 提示输入密码后，输入两次后会生成密码文件
# 配置完成后，重启一下Nginx服务
sudo nginx -s reload
'''


###### 测试
# 看看是否会切换IP
import requests
from urllib.parse import quote
import re

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return treat.as_string(response.body)
end
'''

url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)
response = requests.get(url, auth=('admin', 'admin'))
ip = re.search('(\d+.\d+\.\d+\.\d+)',response.text).group(1)
print(ip)
