from discord.ext import commands

import messages
import settings
from songs import lyrics as lyrics_search
from songs import soundcloud as sc
from songs import youtube

bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.content.lower().startswith(settings.COMMAND_PREFIX):
        await bot.process_commands(message)
    elif message.content.lower() == 'ping':
        await message.channel.send(messages.HELLO_RESPONSE)
    elif message.content.lower() == 'cancel':
        await message.channel.send(messages.HELLO_RESPONSE)
    # else:
    #     await message.channel.send(HELP)


@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(messages.SEARCH_PARAMETER_REQUIRED)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(error)
    else:
        await ctx.send(messages.INTERNAL_SERVER_ERROR)
        print(error)


@bot.command(pass_context=True)
async def search(ctx, *, keyword):
    output = youtube.list_videos(keyword)
    await ctx.send(output if output else messages.ERROR_404)


@bot.command(pass_context=True)
async def soundcloud(ctx, *, keyword):
    output = sc.list_videos(keyword)
    await ctx.send(output if output else messages.ERROR_404)


@bot.command(pass_context=True)
async def lyrics(ctx, *, keyword):
    output = lyrics_search.search(keyword)
    await ctx.send(output if output else messages.ERROR_404)


@bot.command(pass_context=True)
async def play(ctx, *, keyword):
    output = youtube.search(keyword)
    await ctx.send(f'{messages.YOUTUBE_WATCH_URL}?v={output[0]["id"]["videoId"]}' if output else messages.ERROR_404)


bot.run(settings.DISCORD_TOKEN)
