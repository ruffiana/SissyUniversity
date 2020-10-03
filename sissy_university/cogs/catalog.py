from datetime import datetime, timedelta
import itertools
import logging
from pathlib import Path
import random
import re
import time

import discord
from discord.ext import commands



class Catalog(commands.Cog):
    """ Catalog cog for discord.py bot
    """
    COLOR_DEF = discord.Colour.from_rgb(240, 168, 192)
    URL_WEBSITE = "https://sissy-university.com/"
    URL_ICON = URL_WEBSITE + "img/logo.png"
    URL_IMAGE = URL_WEBSITE + "img/image{}.jpg"
    FOOTER = f"©2020 SISSY-UNIVERSITY.COM - ALL RIGHTS RESERVED."
    
    # PATH_BASE = Path(__file__).parent
    # PATH_DATA = PATH_BASE.parent / "data"
    # PATH_IMAGES = PATH_BASE.parent / "images"
    URL_IMAGE_TIERS = [
        "https://media.discordapp.net/attachments/760278456982044732/760629153938276352/tier_1.png",
        "https://media.discordapp.net/attachments/760278456982044732/760629157683003442/tier_2.png",
        "https://media.discordapp.net/attachments/760278456982044732/760629161286696980/tier_3.png",
        "https://media.discordapp.net/attachments/760278456982044732/760629164679495710/tier_4.png",
        "https://media.discordapp.net/attachments/760278456982044732/760629622806675456/tier_5.png",
    ]

    def __init__(self, bot):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)-15s %(message)s')

        self.bot = bot


    def _create_embed(self, ctx, obj, include_id=False):
        """
        Creates message/embed bundle for a challenge
        """
        msg = ""

        # if the obj has a 'tier' property, we want to add a lock emoji to the
        # title if it's locked for the user viewing it
        if hasattr(obj, "tier") and obj.locked:
            title = f":lock: {obj.name}"
        else:
            title = obj.name
        if include_id:
            title = f"{title} {obj.id}"

        # get and parse description for special text formatters
        desc = obj.description

        # get color for embed frame
        color = self.COLOR_DEF
        embed = discord.Embed(
            title=title,
            description=desc,
            color=color
            )

        # use author property to link back to sissy-university.com website
        embed.set_author(name="Sissy University", url=self.URL_WEBSITE, icon_url=self.URL_ICON)

        # add main image
        image = self.URL_IMAGE.format(obj.imgUrl)
        embed.set_image(url=image)

        # Add thumbnail tier
        if hasattr(obj, "tier") and obj.tier:
            idx = obj.tier - 1
            embed.set_thumbnail(url=self.URL_IMAGE_TIERS[idx])

        # Add fields
        if hasattr(obj, "prerequisites") and obj.prerequisites:
            _str = "\n".join([f"- {p.name}" for p in obj.prerequisites])
            embed.add_field(name="Prerequisites:", value=_str, inline=False)

        if hasattr(obj, "daily1") and obj.daily1:
            _str = f"- {obj.daily1}\n- {obj.daily2}"
            embed.add_field(name="Daily Tasks:", value=_str, inline=False)

        if hasattr(obj, "exam1") and obj.exam1:
            _str = f"- {obj.exam1}\n- {obj.exam2}"
            embed.add_field(name="Exam Options:", value=_str, inline=False)

        if hasattr(obj, "perk1") and obj.perk1:
            _str = f"- {obj.perk1}\n- {obj.perk2}"
            embed.add_field(name="Perks:", value=_str, inline=False)

        if hasattr(obj, "job1") and obj.job1:
            _str = f"- {obj.job1}\n- {obj.job2}"
            embed.add_field(name="Activities:", value=_str, inline=False)

        # set footer
        embed.set_footer(text=self.FOOTER, icon_url=self.URL_ICON)
        return msg, embed


    def _create_embed_list(self, ctx, data_type, data_collection):
        msg = ""
        title = data_type.capitalize()
        desc = f"Get information about a specific {data_type} by id or name:"
        color = self.COLOR_DEF
        embed = discord.Embed(
            title=title,
            description=desc,
            color=color
            )

        # use author property to link back to sissy-university.com website
        embed.set_author(name="Sissy University", url=self.URL_WEBSITE, icon_url=self.URL_ICON)

        items = data_collection.as_list()
        num_items = len(items)
        if num_items < 25:
            _str = "\n".join(items)
            embed.add_field(name=f"ID - Name:", value=_str, inline=False)
        else:
            _str = "\n".join(items[:(num_items // 2 )])
            embed.add_field(name=f"ID - Name:", value=_str, inline=True)
            _str = "\n".join(items[(num_items // 2 + 1):])
            embed.add_field(name=f"ID - Name:", value=_str, inline=True)

        # set footer
        embed.set_footer(text=self.FOOTER, icon_url=self.URL_ICON)
        return msg, embed


    def _get_data_and_create_view(self, ctx, data_type, *args, key_type="name"):
        user_id = str(ctx.message.author.id)
        data_collection = getattr(self.bot.controller, data_type)

        if len(args) == 0:
            _msg = f"`!{data_type}` command requires an id or name. (Use `!{data_type} list` to get a full list of {data_type}.)"
            return _msg, None
            
        if len(args) == 1 and args[0].lower() == 'list':
           return self._create_embed_list(ctx, data_type, data_collection)

        # single arg should either be a digit as class id or possibly 'list'     
        if len(args) == 1 and args[0].isdigit():
            obj = data_collection.get_by_property('id', int(args[0]))
        # multiple args are likely a class name
        else:
            value = " ".join(args)
            obj = data_collection.get_by_property(key_type, value)

        if not obj:
            key = " ".join(args)
            _msg = f"Could not find any {data_type} that matches \"{key}\"."
            return _msg, None

        else:
            include_id = data_type == 'courses'
            return self._create_embed(ctx, obj, include_id=include_id)


    @commands.command(aliases=['maj', 'majors'])
    async def major(self, ctx, *args):
        """
        Command to get and display information about a major
        """
        msg, embed = self._get_data_and_create_view(ctx, 'majors', *args)
        await ctx.channel.send(msg, embed=embed)


    @commands.command(aliases=['class', 'classes'])
    async def course(self, ctx, *args):
        """
        Command to get and display information about a course
        """
        msg, embed = self._get_data_and_create_view(ctx, 'courses', *args)
        await ctx.channel.send(msg, embed=embed)


    @commands.command(aliases=['clubs'])
    async def club(self, ctx, *args):
        """
        Command to get and display information about a club
        """
        msg, embed = self._get_data_and_create_view(ctx, 'clubs', *args)
        await ctx.channel.send(msg, embed=embed)


    @commands.command(aliases=['partners'])
    async def partner(self, ctx, *args):
        """
        Command to get and display information about a partner
        """
        msg, embed = self._get_data_and_create_view(ctx, 'partners', *args)
        await ctx.channel.send(msg, embed=embed)


    @commands.command(aliases=['punish'])
    async def punishment(self, ctx, *args):
        """
        Command to get and display information about a partner
        """
        msg, embed = self._get_data_and_create_view(ctx, 'punishments', *args)
        await ctx.channel.send(msg, embed=embed)



def setup(bot):
    bot.add_cog(Catalog(bot))


if __name__ == "__main__":
    pass
