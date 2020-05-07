class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # request.meta['proxy']="http://ip:port"
        request.meta['proxy']='http://222.95.144.31:3000'



        # request.meta['proxy']='http://user:password@ip:port'
