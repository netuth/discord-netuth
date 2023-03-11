import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.command()
@has_permissions(administrator=True)
async def kicknorole(ctx: commands.Context):
    members = ctx.guild.members

    for member in members:
        if len(member.roles) == 1:
            await member.kick()
            print(member.name)
    await ctx.reply('Done!')
@bot.command()
@has_permissions(administrator=True)
async def cer(ctx: commands.Context,arg1):
    channels = ctx.guild.text_channels

    for member in ctx.channel.members:
        if len(member.roles) < 2:
            print(member.name)
            tempname=member.name
            await member.edit(nick=arg1)
            await member.add_roles(bot.get_guild(1044531480623325264).get_role(1080776455941799976),reason="인증봇 자동부여")
            await member.remove_roles(bot.get_guild(1044531480623325264).get_role(1083440572875948113),reason="인증봇 자동제거")
            await ctx.reply(str(tempname)+"님 인증 성공! 닉네임 변경 : "+tempname+" -> "+str(member.nick))








bot.run('MTA4MzM2MzY3MTY0MTY5MDIxMg.GFEd9C.zo_Qyl8yjxmU-cbwcX_2kHOTQPyvPevYSPSv9Y')