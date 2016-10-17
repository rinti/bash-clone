def get_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        return ip.split(',')[0]
    return request.META.get('REMOTE_ADDR')
