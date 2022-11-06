import asyncio

from utils import read_data, send_data, SOCKET_PATH


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    message = await read_data(reader=reader)
    addr = writer.get_extra_info("peername")

    print(f"-> Received {message!r} from {addr!r}")

    # Do optional logic here

    print(f"-> Sending response...")
    await send_data(writer=writer, message="OK")

    print("-> Closing the connection")
    writer.close()


async def main():
    server = await asyncio.start_unix_server(handler, SOCKET_PATH)

    # asyncio.unix_events._UnixSelectorEventLoop

    loop = asyncio.get_running_loop()
    print(type(loop))

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    try:
        await server.serve_forever()
    except:
        server.close()
        await server.wait_closed()


asyncio.run(main())
