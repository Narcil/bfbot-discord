import discord
from discord.ext import commands
from discord import app_commands  # 1. Added this import

class myCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.ekillibre = "https://platform.ekillibre.com/fr/qr/ZGFmNWU5Y2EtNTYyNC00OTk3LWExYzYtNTRlNTg1YTkzMjA4.9JXZeGTUhvadtqeWyCoLwGGEY_yUAaov3GAkgXaJRuk"

    @commands.Cog.listener()
    async def on_ready(self):
        print("Scheduler pause On")

    @app_commands.command(name="sandwich", description="Ekillibre")
    async def sandwich(self, interaction: discord.Interaction):
        await interaction.response.send_message("Sandwich")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(myCog(bot))