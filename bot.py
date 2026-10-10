import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def is_admin():
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)


@bot.command()
async def rules(ctx):
    e1 = discord.Embed(
        title="⬛ 📃 SERVER RULES",
        description=(
            "These rules keep the server **safe, organized, and enjoyable** for everyone. "
            "By being here, you agree to follow them.\n\n"
            "◼️ Staff may step in on situations not specifically listed if they disrupt "
            "the server or negatively affect the community."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e2 = discord.Embed(
        title="⬛ 🔹 THE BASICS",
        description=(
            "▫️ Keep messages in **English** so staff can moderate properly.\n"
            "▫️ Be respectful. Treat others how you'd want to be treated.\n"
            "▫️ Hate speech, harassment, bullying, discrimination, or targeting others will **not** be tolerated.\n"
            "▫️ No doxxing, threats, or intimidation — joke or not.\n"
            "▫️ Swearing is **not** allowed.\n"
            "▫️ Do not use alt accounts to avoid mutes or bans.\n"
            "▫️ No impersonating other members or staff."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e3 = discord.Embed(
        title="⬛ 🔹 STAY ON TOPIC",
        description=(
            "▫️ Use the correct channels.\n"
            "▫️ Keep image-only channels for their intended purpose.\n"
            "▫️ Builder/roleplayer requests belong in 🍬looking-for-group only.\n"
            "▫️ Linking/promoting your forum post may result in a warn.\n"
            "▫️ Heated arguments may be shut down by staff."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e4 = discord.Embed(
        title="⬛ 🔹 APPROPRIATE CONTENT",
        description=(
            "▫️ No NSFW, inappropriate, or illegal content.\n"
            "▫️ GIFs and images follow the same rules as messages.\n"
            "▫️ Off-server drama discussion will not be tolerated.\n"
            "▫️ Inappropriate nicknames, tags, or avatars are not allowed.\n"
            "▫️ Only Bloxburg and appropriate built-in activities may be streamed."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e5 = discord.Embed(
        title="⬛ 🔹 SAFETY",
        description=(
            "▫️ Do not share or ask for personal information.\n"
            "▫️ Do not encourage illegal or dangerous behavior.\n"
            "▫️ Report rule-breaking in ❗discord-reports.\n"
            "▫️ Share glitches or bugs only in No Access."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e6 = discord.Embed(
        title="⬛ 🔹 SPAMMING & PINGING",
        description=(
            "▫️ Don't spam messages, emojis, or stickers.\n"
            "▫️ Do not ping Community Managers, Developers, or Content Creators.\n"
            "▫️ Only ping staff for actual issues."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e7 = discord.Embed(
        title="⬛ 🔹 NO SELF-PROMO OR BEGGING",
        description=(
            "▫️ No advertising yourself or outside platforms unless permitted.\n"
            "▫️ No begging for in-game items, currency, Nitro, or perks."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e8 = discord.Embed(
        title="⬛ 🔹 DMs & PRIVATE MESSAGING",
        description=(
            "▫️ Staff are not required to respond to DMs. Use ❗discord-reports.\n"
            "▫️ Private DMs are outside our control — report to Discord directly."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    e9 = discord.Embed(
        description=(
            "⬛ Comply with **Discord's ToS** and **Roblox's ToS**."
        ),
        color=discord.Color.from_rgb(0, 0, 0)
    )
    for e in [e1, e2, e3, e4, e5, e6, e7, e8, e9]:
        await ctx.send(embed=e)


@bot.command()
@is_admin()
async def setimage(ctx, name: str):
    if not ctx.message.attachments:
        await ctx.send("❌ Attach an image with this command!")
        return
    att = ctx.message.attachments[0]
    if not att.content_type or not att.content_type.startswith("image/"):
        await ctx.send("❌ Not an image.")
        return
    ext = att.filename.split(".")[-1]
    await att.save(f"{name}.{ext}")
    await ctx.send(f"✅ Saved as `{name}`")


@bot.command()
async def image(ctx, name: str):
    import glob
    files = glob.glob(f"{name}.*")
    if files:
        await ctx.send(file=discord.File(files[0]))
    else:
        await ctx.send("❌ No image found.")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


bot.run(TOKEN)
