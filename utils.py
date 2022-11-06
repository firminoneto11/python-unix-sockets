import asyncio

LIMIT: int = asyncio.streams._DEFAULT_LIMIT
MARKER = "_;;;"
SOCKET_PATH = "./sockets/server.sock"


async def read_data(reader: asyncio.StreamReader) -> str:
    blocks = []
    while 1:
        block = await reader.read(LIMIT)
        if block:
            message = block.decode()
            blocks.append(message)
            if MARKER in message:
                break
        break

    return "".join(blocks).replace(MARKER, "")


async def send_data(writer: asyncio.StreamWriter, message: str) -> None:
    final = message + MARKER
    writer.write(final.encode("utf-8"))
    await writer.drain()
