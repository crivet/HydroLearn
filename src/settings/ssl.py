# ssl configuration
SECURE_SSL_REDIRECT = True
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = 'https://'
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000