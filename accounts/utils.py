def get_client_ip(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('HTTP_X_REAL_IP') or request.META.get(
        'REMOTE_ADDR')
    return client_ip
