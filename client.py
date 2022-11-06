import asyncio

from utils import SOCKET_PATH, read_data, send_data


async def keep_sending_to_unix_socket() -> None:
    message = "A simple text!"
    while True:
        reader, writer = await asyncio.open_unix_connection(SOCKET_PATH)

        await send_data(writer=writer, message=message)
        print(f"-> Sended message to the server at: {SOCKET_PATH!r}")

        response = await read_data(reader=reader)
        print(f"-> Received from server: {response!r}")

        writer.close()
        await writer.wait_closed()
        print("-> Closed the connection")
        await asyncio.sleep(2)


asyncio.run(keep_sending_to_unix_socket())
