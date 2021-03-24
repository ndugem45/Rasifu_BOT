from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
import random
import time

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='$')

# ======================================


act = [
  'Bikin mie ...',
  'Main Genshin ...',
  'Bersih" Guild Hall ...',
  'Bikin dekorasi ...',
  'Bayar listrik Guild ...',
  'Isi tandon air ...',
  'Kasih makan kucing ...',
  'Pergi kencan ...'
]
greeting = [
  'Yupp :3', 
  'yooo -_-', 
  'Yosh :D', 
  'Hmmmmmm',
  'Gmn gmn ?',
  'Yes, can i help u ? :)',
  'uhhh aku cape, ada apa ?',
  'Rasifu disini :)'
]
ask = [
  'siapa'
]
whitelist_member = [
  'EagleOne#0797',
  'ndugem45#1956'
]
gh = 715964928757858318
bot_room = 801652022025519125
bimbang = [
  'Hah, beneran ?',
  'Emmmm.. serius ?',
  'Yakin ga ?',
  'Eksekusi ?'
]
ask_for_wait = [
  'Tunggu ya ...',
  'Emm ....',
  'Wait ...',
  'Bentar.. bentar..'
]
cant_help = [
  'Maaf gabisa bantu :(',
  'Uhh maaf :(',
  'Duh maaf ya Rasifu gabisa :D',
  'Sepertinya aku gabisa :o',
  'Emmmm... aku belum diajarin :D',
  'Sorry, gatau mau jawab apa :D'
]
master_answ = [
  "Yes, master :)",
  "Im here master :D",
  "Can i help u, master :)"
]
ask_attention = [
  "Haloo haloo ...",
  "Hai semua :D",
  "Cek cek ... cek cek",
  "Ehemm, perhatian ...",
  "Tolong diperhatikan yak :)"
]


def notes():
  print('note dari lok')
  return """Oke buat yg baru join discord, Welcome to Calavera, guild yg santai tapi serius. Serius tapi santai.

  Weekly kalian dijamin aman di sini karna member2 lama udh pada bisa GB semua. Guild war juga kita aktif, so pastiin kalian ikut ya buat nambah jam terbang. Berikut jadwal war, setiap hari:

  Kamis, 21.00 WIB = War of emperium (WOE)
  Minggu, 21.00 WIB = War of crystal (WOC)

  Pastiin pas war kalian ada equip pvp ya (dmg to demi human). Jika berhalangan, mohon bantuannya untuk ijin di sini karena kita tidak memaksa kalian utk ikut war, tapi setidaknya hormati saudara kalian yang sudah effort jaga kastil.

  Untuk discord, tersedia room utk klinik, event, weekly info silakan dieksplor sendiri.  Voice juga tersedia jika butuh. Jika butuh GB, silakan tag member di sini supaya bisa diingatkan.

  Terima kasih sudah join. Play wise, banyak2in referensi youtube dan artikel, rajin2 baca."""


# ====================================



def welcome(name=""):
	return "welcome {}".format(name)

switcher = {
  'welcome': welcome(),
}


# ==========================================


@client.command(name='server')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'Server Name: {guild.name}')
	await context.send(f'Server Size: {len(guild.members)}')
	await context.send(f'Server Name: {guild.owner.display_name}')


@client.command(pass_context=True)
async def ras(ctx, *args):
  if not args:
      await ctx.channel.send(":o")
  else:
      func = switcher.get(str(args[0]).lower(), lambda: "-__-")
      await ctx.channel.send(func)

# =======================================

@client.event
async def on_ready():
  print("im alive master :)")

@client.event
async def on_member_update(before,after):
  print(before.name + " update")

@client.event
async def on_member_join(member):
  print(member.name + " join the club")
  await client.get_channel(bot_room).send(welcome(member.mention))
  time.sleep(0.5)
  await client.get_channel(bot_room).send("Aku ada info nih :3 \n ...")
  time.sleep(1)
  await client.get_channel(bot_room).send(notes())
  time.sleep(0.7)
  await client.get_channel(bot_room).send("Untuk list info yang bisa aku bantu ketik $help yak :D")


keep_alive()
client.run(os.getenv('TOKEN'))