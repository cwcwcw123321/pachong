from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        'User-Agent': 'UserAgent().firefox'
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.read().decode())
    return response.read()


def save_html(filename,html_bytes):
    with open(filename,'wb') as f:
        f.write(html_bytes)


def main():
    content = input('请输入下载的内容')
    num = input('请输入下载多少页：')
    base_url='https://tieba.baidu.com/f?ie=utf-8&{}'
    for pn in range(int(num)):
        args = {
            'pn': pn * 50,
            'kw': content
        }
        file_name='第'+str(pn+1)+'页.html'
        args=urlencode(args)
        print('正在下载'+file_name)
        html_bytes=get_html(base_url.format(args))
        save_html(file_name,html_bytes)



if __name__ == '__main__':
    main()
