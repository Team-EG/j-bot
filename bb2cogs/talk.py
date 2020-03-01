import discord
import random
from discord.ext import commands
from time import strftime, localtime


class Talk(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def 안녕(self, ctx):
        await ctx.send('안녕하세요!')

    @commands.command(pass_context=True)
    async def 정보(self, ctx):
        servers = len(self.client.guilds)
        users = len(set(self.client.get_all_members()))
        embed = discord.Embed(title='제이봇', description='by eunwoo1104#9600, V1 / R 2020-02-09',
                              colour=discord.Color.red())
        embed.add_field(name='들어와있는 서버수', value=f'{servers}개')
        embed.add_field(name='같이 있는 유저수', value=f'{users}명', inline=False)
        embed.add_field(name='버그 신고는?', value='eunwoo1104#9600으로 DM 보내주세요!')

        await ctx.send(embed=embed)

    @commands.command()
    async def 크레딧(self, ctx):
        url = f"https://jebserver.iptime.org/credit/"
        embed = discord.Embed(title="제이봇 크레딧", description=f"링크를 눌러보세요.", colour=discord.Colour(0xffffff),
                              url=f"{url}")
        await ctx.send(embed=embed)

    @commands.command()
    async def 아무말(self, ctx):
        responses = ['아무말',
                     '아아무말',
                     '아아아무말',
                     '아아아아무말',
                     '말무아']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def 유저정보(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title='유저정보', description=f'{member}', color=member.color)

        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='유저 ID', value=member.id)
        embed.add_field(name='서버 닉네임', value=member.display_name, inline=False)
        embed.add_field(name='계정이 생성된 날짜', value=member.created_at.strftime("%Y %B %d %a"))
        embed.add_field(name='서버에 들어온 날짜', value=member.joined_at.strftime("%Y %B %d %a"), inline=False)
        embed.add_field(name='역할', value=member.top_role.mention)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def 네이버검색(self, ctx, *, search=None):
        result = search.replace(" ", "+")
        embed = discord.Embed(title="네이버 검색 결과", description=f"'{search}'의 검색 결과입니다.", colour=discord.Color.green(),
                              url=f"https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={result}")
        embed.set_thumbnail(url="https://ssl.pstatic.net/sstatic/search/common/og_v3.png")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def 구글검색(self, ctx, *, search=None):
        result = search.replace(" ", "+")
        url = f"https://www.google.com/search?q={result}&oq={result}&aqs=chrome..69i57j69i60j69i61.3020j0j8&sourceid=chrome&ie=UTF-8"
        embed = discord.Embed(title="구글 검색 결과", description=f"'{search}'의 검색 결과입니다.", colour=discord.Colour(0xffffff),
                              url=f"{url}")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def 나무위키(self, ctx, *, search=None):
        result = search.replace(" ", "%20")
        url = f"https://namu.wiki/w/{result}"
        embed = discord.Embed(title="나무위키 검색 결과", description=f"'{search}'의 검색 결과입니다.",
                              colour=discord.Color.dark_green(),
                              url=f"{url}")
        embed.set_thumbnail(
            url="https://w.namu.la/s/7744b80f6fa5262190bba52da210a8cdd2cb03c7d040c0be25274eade7de04ef4cb04ade767dc11bd6ea3d4164885d4e0608304200f5ad1380629c484bcd29c3365bb1c18531fdf9615491322081e9531d7c834467270a173fff1b840bc85626")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def 유튜브검색(self, ctx, *, search=None):
        result = search.replace(" ", "+")
        embed = discord.Embed(title="유튜브 검색 결과", description=f"'{search}'의 검색 결과입니다.", colour=discord.Color.red(),
                              url=f"https://www.youtube.com/results?search_query={result}")
        embed.set_thumbnail(url="https://www.youtube.com/yts/img/yt_1200-vflhSIVnY.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def 서버정보(self, ctx):
        embed = discord.Embed(title='서버정보', colour=discord.Color.red())
        embed.set_author(name=f'{ctx.guild.name}', icon_url=ctx.guild.icon_url)
        embed.add_field(name='소유자', value=f'{ctx.guild.owner.display_name}')
        embed.add_field(name='유저수', value=f'{ctx.guild.member_count}명', inline=False)
        embed.add_field(name='서버가 생성된 날짜', value=f'{ctx.guild.created_at.strftime("%Y-%m-%d %I:%M:%S %p")}')
        embed.add_field(name='역할수', value=str(len(ctx.guild.roles)) + '개', inline=False)
        embed.add_field(name='서버 위치', value=f'{ctx.guild.region}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Talk(client))

    # embed 탬플릿 (앞에 #을 지우고 사용하세요)
    # embed.add_field(name='', value='')
    # embed.add_field(name='', value='', inline=False)
