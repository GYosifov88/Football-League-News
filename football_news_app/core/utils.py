def megabyte_to_bytes(mb):
    return mb * 1024 * 1024


def is_owner(request, obj):
    return request.user == obj.user


