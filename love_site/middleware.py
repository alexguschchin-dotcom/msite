class DisableSecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Удаляем все мешающие заголовки безопасности
        headers_to_remove = [
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Referrer-Policy',
            'Permissions-Policy',
        ]
        for header in headers_to_remove:
            if header in response:
                del response[header]
        return response