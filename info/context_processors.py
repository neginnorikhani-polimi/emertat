def language_context(request):
    """
    Lightweight bilingual context based on the URL prefix.

    English pages use the normal paths, e.g. /about/.
    Persian pages use the same routes mounted below /fa/, e.g. /fa/about/.
    """
    path = request.path or "/"
    is_fa = path == "/fa/" or path.startswith("/fa/")

    if is_fa:
        switch_url = path[3:] or "/"
        if not switch_url.startswith("/"):
            switch_url = "/" + switch_url
    else:
        switch_url = "/fa/" if path == "/" else "/fa" + path

    return {
        "is_fa": is_fa,
        "language_switch_url": switch_url,
        "language_code": "fa" if is_fa else "en",
    }
