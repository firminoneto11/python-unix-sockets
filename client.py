import asyncio

from utils import SOCKET_PATH, read_data, send_data


async def connect_to_unix_socket():
    while True:
        message = await asyncio.to_thread(input, "Insert your message or press 'q' to exit: ")
        if message.lower() == "q":
            break
        reader, writer = await asyncio.open_unix_connection(SOCKET_PATH)

        print(f"-> Sending to server: {message!r}")
        await send_data(writer=writer, message=message)

        response = await read_data(reader=reader)
        print(f"-> Received from server: {response!r}")
    print("-> Closed the connection")
    writer.close()
    await writer.wait_closed()


async def keep_sending_to_unix_socket():
    while True:
        message = "A simple text!"

        reader, writer = await asyncio.open_unix_connection(SOCKET_PATH)

        print(f"-> Sending to server: {message!r}")
        await send_data(writer=writer, message=message)

        response = await read_data(reader=reader)
        print(f"-> Received from server: {response!r}")

        print("-> Closed the connection")
        writer.close()
        await writer.wait_closed()
        await asyncio.sleep(2)


# asyncio.run(connect_to_unix_socket())
asyncio.run(keep_sending_to_unix_socket())
