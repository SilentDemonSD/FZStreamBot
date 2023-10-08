from FZStream import Stream, LOGGER, Config
from pyrogram import idle
from pyrogram.filters import command, user
from os import path as ospath, execl
from asyncio import create_subprocess_exec
from sys import executable
from aiohttp.web import AppRunner, TCPSite
from FZStream.core.server import initiate_server

@Stream.on_message(command('restart') & user(Config.OWNER_ID))
async def restart(client, message):
    restart_message = await message.reply('<i>Restarting...</i>')
    await (await create_subprocess_exec('python3', 'update.py')).wait()
    with open(".restartmsg", "w") as f:
        f.write(f"{restart_message.chat.id}\n{restart_message.id}\n")
    execl(executable, executable, "-m", "FZStream")

async def restart():
    if ospath.isfile(".restartmsg"):
        with open(".restartmsg") as f:
            chat_id, msg_id = map(int, f)
        try:
            await Stream.edit_message_text(chat_id=chat_id, message_id=msg_id, text="<i>Restarted !</i>")
        except Exception as e:
            LOGGER.error(e)
            
async def run_server():
    app = AppRunner(await initiate_server())
    await app.setup()
    await TCPSite(app, Config.BIND_ADRESS, Config.PORT).start()
    LOGGER.info(f'FZ Server Connected at {Config.BIND_ADRESS}')

if __name__ == '__main__':
    Stream.start()
    Stream.loop.run_until_complete(restart())
    Stream.loop.run_until_complete(run_server())
    LOGGER.info('FZ Bot Started!')
    idle()
    Stream.stop()