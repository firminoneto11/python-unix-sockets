import asyncio

SOCKET_PATH = "./sockets/server.sock"
ENCODING = "utf-8"


async def read_data(reader: asyncio.StreamReader) -> str:
    return (await reader.read()).decode(ENCODING)


async def send_data(writer: asyncio.StreamWriter, message: str) -> None:
    writer.write(message.encode(ENCODING))
    writer.write_eof()
    await writer.drain()


async def close_writer(writer: asyncio.StreamWriter) -> None:
    writer.close()
    await writer.wait_closed()
