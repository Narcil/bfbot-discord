import discord
from discord.ext import commands
from discord import app_commands
from cogs.llm_quiz import LangChainBot

class AnswerView(discord.ui.View):
    def __init__(self, bot_llm: LangChainBot, uid: int):
        super().__init__(timeout=60)
        self.llm = bot_llm
        self.uid = uid

    async def handle_answer(self, interaction: discord.Interaction, choice: str):
        try:
            await interaction.response.defer(ephemeral=True)
            for item in self.children:
                item.disabled = True
            await interaction.edit_original_response(view=self)
            response = await self.llm.generate_response(self.uid, f"I choose option {choice})")
            await interaction.followup.send(response, ephemeral=True)
        except Exception as e:
            print(f"Erreur handle_answer: {e}")

    @discord.ui.button(label="A", style=discord.ButtonStyle.primary)
    async def button_a(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, "A")

    @discord.ui.button(label="B", style=discord.ButtonStyle.primary)
    async def button_b(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, "B")

    @discord.ui.button(label="C", style=discord.ButtonStyle.primary)
    async def button_c(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, "C")

    @discord.ui.button(label="D", style=discord.ButtonStyle.primary)
    async def button_d(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, "D")

class Quiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.llm = LangChainBot()

    @app_commands.command(name='quiz', description='Generate a CompTIA Security+ question')
    async def quiz(self, interaction: discord.Interaction, theme: str):
        uid = interaction.user.id
        await interaction.response.defer(ephemeral=True)
        self.llm.reset_history(uid)
        response = await self.llm.generate_response(uid, theme)
        view = AnswerView(self.llm, uid)
        await interaction.followup.send(response, view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Quiz(bot))