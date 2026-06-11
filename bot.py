import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Variables de configuración
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))
VERIFICATION_CHANNEL_ID = int(os.getenv('VERIFICATION_CHANNEL_ID'))
VERIFIED_ROLE_ID = int(os.getenv('VERIFIED_ROLE_ID'))

# Emoji para la reacción
VERIFICATION_EMOJI = "✅"

@bot.event
async def on_ready():
    print(f'{bot.user} se ha conectado a Discord!')
    print('------')

@bot.command(name='verificar')
async def send_verification(ctx):
    """Envía el embed de verificación al canal"""
    
    # Verificar que el comando se ejecute en el canal correcto
    if ctx.channel.id != VERIFICATION_CHANNEL_ID:
        await ctx.send("❌ Este comando solo se puede usar en el canal de verificación.")
        return
    
    # Crear el embed
    embed = discord.Embed(
        title="🌿 Bienvenido a 420 Kush Community 🌿",
        description="Para acceder al servidor, debes verificarte haciendo clic en la reacción ✅ de abajo.",
        color=discord.Color.green()
    )
    
    embed.add_field(
        name="📋 ¿Qué necesitas hacer?",
        value="Haz clic en la reacción ✅ para verificarte instantáneamente.",
        inline=False
    )
    
    embed.add_field(
        name="✨ Beneficios",
        value="• Acceso completo al servidor\n• Poder participar en canales\n• Interactuar con la comunidad",
        inline=False
    )
    
    embed.set_footer(
        text="420 Kush Community",
        icon_url="https://cdn-icons-png.flaticon.com/512/1995/1995467.png"
    )
    
    # Enviar el embed
    message = await ctx.send(embed=embed)
    
    # Añadir la reacción
    await message.add_reaction(VERIFICATION_EMOJI)
    
    await ctx.send("✅ Embed de verificación enviado correctamente!")

@bot.event
async def on_raw_reaction_add(payload):
    """Evento que se dispara cuando alguien añade una reacción"""
    
    # Verificar que sea en el canal correcto
    if payload.channel_id != VERIFICATION_CHANNEL_ID:
        return
    
    # Verificar que sea el emoji correcto
    if str(payload.emoji) != VERIFICATION_EMOJI:
        return
    
    # Obtener el servidor y el usuario
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    role = guild.get_role(VERIFIED_ROLE_ID)
    
    # Evitar que el bot se verifique a sí mismo
    if member.bot:
        return
    
    # Asignar el rol
    try:
        await member.add_roles(role)
        print(f"✅ {member.name} ha sido verificado")
    except Exception as e:
        print(f"❌ Error al verificar a {member.name}: {e}")

@bot.event
async def on_raw_reaction_remove(payload):
    """Evento que se dispara cuando alguien quita una reacción"""
    
    # Verificar que sea en el canal correcto
    if payload.channel_id != VERIFICATION_CHANNEL_ID:
        return
    
    # Verificar que sea el emoji correcto
    if str(payload.emoji) != VERIFICATION_EMOJI:
        return
    
    # Obtener el servidor y el usuario
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    role = guild.get_role(VERIFIED_ROLE_ID)
    
    # Evitar que el bot se desvifique a sí mismo
    if member.bot:
        return
    
    # Quitar el rol
    try:
        await member.remove_roles(role)
        print(f"❌ {member.name} ha sido desverificado")
    except Exception as e:
        print(f"❌ Error al desverificar a {member.name}: {e}")

# Ejecutar el bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
