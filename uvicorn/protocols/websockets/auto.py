try:
    pass
except ImportError as exc:  # pragma: no cover
    try:
        pass
    except ImportError as exc:
        AutoWebSocketsProtocol = None
    else:
        from uvicorn.protocols.websockets.wsproto_impl import WSProtocol

        AutoWebSocketsProtocol = WSProtocol
else:
    from uvicorn.protocols.websockets.websockets_impl import WebSocketProtocol

    AutoWebSocketsProtocol = WebSocketProtocol
