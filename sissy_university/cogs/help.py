import logging
import discord
from discord.ext import commands


class Custom_Help(commands.Cog):
    COLOR_DEF = discord.Colour.from_rgb(255, 127, 255)  # pink
    URL_WEBSITE = "https://sissy-university.com/"
    URL_ICON = URL_WEBSITE + "img/logo.png"
    URL_IMAGE = URL_WEBSITE + "img/image{}.jpg"
    FOOTER = f"©2020 SISSY-UNIVERSITY.COM - ALL RIGHTS RESERVED."
    URL_IMAGE_TIERS = [
        "https://cdn.discordapp.com/attachments/760278456982044732/760278572685590578/tier_1.png",
        "https://cdn.discordapp.com/attachments/760278456982044732/760278576506470420/tier_2.png",
        "https://cdn.discordapp.com/attachments/760278456982044732/760278580021297182/tier_3.png"
    ]

    def __init__(self, bot):
        super().__init__()
        logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
        self.bot = bot


    def get_general_help(self):
        msg = ""
        title = "Sissy-University Discord Bot Help"
        color = self.COLOR_DEF
        description = "All commands use '!' as a prefix.\nEx. `!club`"
        embed = discord.Embed(title=title, colour=color, description=description)

        # use author property to link back to sissy-university.com website
        embed.set_author(name="Sissy University", url=self.URL_WEBSITE, icon_url=self.URL_ICON)

        # url_thumbnail = getattr(self.bot, "thumbnail")
        # embed.set_thumbnail(url=url_thumbnail)

        # Add a field for each command
        fields = {
            "club": "Command to get nformation about a club.",
            "class": "Command to get nformation about a club.",
            "major": "Command to get nformation about a major.",
            "partner": "Command to get nformation about a parenter.",
            "punishment": "Command to get nformation about a punishment.",
        }
        for name, value in fields.items():
            embed.add_field(name=f"!{name}", value=value, inline=False)

        # set footer
        embed.set_footer(text=self.FOOTER, icon_url=self.URL_ICON)

        return msg, embed


    @commands.command(aliases=["h"])
    async def help(self, ctx, *args):
        if not args:
            msg, embed = self.get_general_help()
        else:
            # embeds = {
            #     'club': self.get_help_modify,
            #     'class': self.get_help_challenge
            # }
            # get_msg_embed = embeds.get(args)
            # msg, embed = get_msg_embed()
            msg, embed = None, None
            pass
        await ctx.send(msg, embed=embed)


def setup(bot):
    bot.add_cog(Custom_Help(bot))


if __name__ == "__main__":
    pass
