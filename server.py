import asyncio

from utils import SOCKET_PATH, read_data, send_data, close_writer


async def request_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    # print(writer._transport._extra)  # This contains every information about the sender
    # address = writer.get_extra_info("peername")  # Use this if you want just some keys of sender's information

    message = await read_data(reader=reader)
    print(f"-> Received {message!r} from client")

    # Do optional logic here with the received data

    await send_data(writer=writer, message="OK")
    print(f"-> Response sended")

    await close_writer(writer=writer)
    print("-> Connection closed")


async def serve() -> None:
    # asyncio.unix_events._UnixSelectorEventLoop  # Base Unix event loop type
    # addresses = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    # print(f"Serving on {addresses}")  # -> Use this to display where the socket is being served when using IP sockets

    server = await asyncio.start_unix_server(request_handler, SOCKET_PATH)
    print(f"Serving on this socket: {SOCKET_PATH!r}")
    try:
        await server.serve_forever()
    except:
        server.close()
        await server.wait_closed()


asyncio.run(serve())
