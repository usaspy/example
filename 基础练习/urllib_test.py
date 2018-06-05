import urllib

def get_request_lib3():
    http = urllib3.PoolManager()
    r = http.request('DELETE','http://116.62.164.196:8080/portal/index')
    print(r.status)
    print(r.data)

def login_email():
    header = "Host: mail.dhcc.com.cn" \
             "Connection: keep-alive" \
             "Content-Length: 220" \
             "Cache-Control: max-age=0" \
             "Origin: http://mail.dhcc.com.cn" \
             "Upgrade-Insecure-Requests: 1" \
             "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36" \
             "Content-Type: application/x-www-form-urlencoded" \
             "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" \
             "Referer: http://mail.dhcc.com.cn/user/?q=login" \
             "Accept-Encoding: gzip, deflate" \
             "Accept-Language: zh-CN,zh;q=0.8" \
             "Cookie: EMPHPSID=gsa8u64t52gb6bjelri4nvh187; empos=0; emLoginTo=storage; emLoginUser=zhanghongyf%40dhcc.com.cn"

    field = "q=login.do"

    form_data = "user=zhanghongyf%40dhcc.com.cn&password=Passw0rd%21%40%23123&login_ssl=0&auth_code=&go=http%3A%2F%2Fmail.dhcc.com.cn%2F%3Fq%3Dbase%26module%3Dstorage%26_data%3D&referer=http%3A%2F%2Fmail.dhcc.com.cn%2Fuser%2F%3Fq%3Dlogin"

    http = urllib3.PoolManager()
    r = http.request(
        'POST',
        '/user/?q=login.do',
        headers={
            header
        },
        fields={
            field
        },

    )
if __name__ == '__main__':
    get_request_lib3()