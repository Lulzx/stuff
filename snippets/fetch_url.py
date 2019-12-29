def fetch_url(url, query):
    params = urlencode({'q': query})
    final = url.format(params)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
    response = opener.open(final).read().decode('utf-8')
    dict_response = json.loads(response)
    return dict_response
