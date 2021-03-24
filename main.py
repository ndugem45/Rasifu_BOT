from keep_alive import keep_alive
import discord
# from discord.ext.tasks import loop
from discord.ext import commands
import os
import asyncio
import random
import time
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Jakarta')
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='$', intents=intents)

# =================================================================================

def _welcome(name=""):
	return "welcome {}".format(name)
# ====================================================================

senpai = 392660789028454401
movie = [
  "Tukang bubur naik ojek",
  "Kucingku hilang diambil orang",
  "Cinta fitri spesial season",
  "Naga indosiar",
  "Yutub keluarga"
]
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
  'Yupp (*≧ω≦*)', 
  'yooo (￣ヘ￣)', 
  'Yosh ｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡', 
  'Hmmmmmm',
  'Gmn gmn ?',
  'Yes, can i help u ? 	(＠＾◡＾)',
  'uhhh aku cape, ada apa ?',
  'Rasifu disini ☆*:.｡.o(≧▽≦)o.｡.:*☆'
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
  'Maaf gabisa bantu (ノωヽ)',
  'Uhh maaf (╥﹏╥)',
  'Duh maaf ya Rasifu gabisa (シ_ _)シ',
  'Sepertinya aku gabisa (╯︵╰,)',
  'Emmmm... aku belum diajarin (O_O;)',
  'Sorry, gatau mau jawab apa (m;_ _)m'
]
master_answ = [
  "Yes, master (*^‿^*)",
  "Im here master ٩(◕‿◕)۶",
  "Can i help u, master (o˘◡˘o)"
]
ask_attention = [
  "Haloo haloo ...",
  "Hai semua ٩(◕‿◕)۶",
  "Cek cek ... cek cek",
  "Ehemm, perhatian ...",
  "Tolong diperhatikan yak (￣▽￣)"
]
ask_sorry = [
  "Umm, maafin Rasifu",
  "Im sorry",
  "Maaf ya",
  "Gomenasai"
]
reminder_hour = [
  '5','8','11','14','17','20'
]
react_anger = [
  "(＃`Д´)",
  "(・`ω´・)",
  "٩(╬ʘ益ʘ╬)۶",
  "((╬◣﹏◢))",
  "(╬ Ò﹏Ó)",
  "ヽ( `д´*)ノ",
  "↑_(ΦwΦ)Ψ",
  "(`ー´)",
  "ヾ(`ヘ´)ﾉﾞ"
]

# =============================================================================


def _welcome_greeting(user):
  print("fungsi welcome")
  return "Welcome home {} ( ´ ▽ ` )ﾉ".format(user)

def _leave_msg(nama):
  print("fungsi welcome")
  return "Yahh.. '{}' pergi meniggalkan kita .･ﾟﾟ･(／ω＼)･ﾟﾟ･.".format(nama)

async def _kik_member(ctx,args):
  print('fungsi kick')
  if any(str(ctx.author) in s for s in whitelist_member):
    if len(args) > 0:
      print("id target ", ctx.message.mentions[0].id)
      print("nama target ", ctx.message.mentions[0].name)
      await ctx.channel.send(random.choice(bimbang))
      time.sleep(2)
      await ctx.channel.send(random.choice(ask_for_wait))
      time.sleep(7)
      await ctx.channel.send("Ga berani (⁄⁄>⁄▽⁄<⁄⁄)")
    else:
      time.sleep(0.5)
      await ctx.channel.send("Jangan kasian (っ´ω`)ﾉ(╥ω╥)")
  else:
    time.sleep(0.5)
    await ctx.channel.send("(￣_￣)・・・")


def _notes():
  print('note dari lok')
  return """Yupp,.. buat yg baru join discord, Welcome to Calavera ya ♡( ◡‿◡ ) guild yg santai tapi serius. Serius tapi santai.

Weekly kalian dijamin aman di sini karna member-member lama udah pada bisa GB semua. Guild War juga kita aktif loh, so pastiin kalian ikut ya buat nambah jam terbang. Berikut jadwal war, setiap hari:

Kamis, 21.00 WIB = War of emperium (WOE)
Minggu, 21.00 WIB = War of crystal (WOC)

Pastiin pas war kalian ada equip pvp ya (DMG to Demi Human). Jika berhalangan, mohon bantuannya untuk ijin di sini karena kita tidak memaksa kalian untuk ikut war, tapi setidaknya hormati teman kita yang sudah effort jaga kastil :)

Terima kasih sudah join. Play wise, banyak2in referensi youtube dan artikel, rajin baca-baca dan kalau ada yang Rasifu bisa bantu ketik command $ras ＼(٥⁀▽⁀ )／

untuk yang belum bisa/pernah pakai Discord bisa liat informasi cara pakai Discord di room <#813860831556272138>"""

def _woe():
  print('note for woe')
  return """Selamat hari kamis member CALAVERA ヾ(*'▽'*)

Semoga hasil farming kalian hari ini luar biasa yak. Rasifu mau ingetin kalian nih, hari ini jadwal WOE lho. Yuk ikutan!

Mulainya pukul 21.00 WIB. Standby aja di guild hall dari pukul 20.30 WIB. Persiapkan equipment PVP kalian. Kalian bisa beli buff/potion di black cat cafe (posisi di guild hall dekat vending machine). Silakan bikin party dengan teman-temannya, bebas kok partynya.
Kalau ada yang belum tau apa itu WOE, Rasifu kasih video nih. Ditonton ya sampai habis:

https://www.youtube.com/watch?v=WrcTvyKHfd8&t=225s

**Terus, kenapa kalian harus ikut WOE sih?**
1. Kastil tuh rumah kalian lho, bukan hanya milik para lead. Masa kalian mau rumah kalian diserang sama tamu tak dikenal (╯︵╰,)

2. Menang atau kalah, kuat atau lemah, mendominasi atau didominasi player lawan, yang penting dengan partisipasi kalian bisa dapat honor proof (penting loh untuk perkembangan char kalian) (￢‿￢ )

3. Bangun solidaritas dengan member lain. Berjuang bersama bikin kita tambah solid gais ヽ(￣ω￣(。。 )ゝ

So, Rasifu percaya kalian yang hebat-hebat ini pasti bisa menjaga rumahnya dengan percaya diri. Selamat berjuang ya kawan-kawan CALAVERA (^_<)"""

def _woc():
  print('note for woc')
  return """Perhatian kepada seluruh member CALAVERA ヾ(*'▽'*)

Hari ini minggu, ada jadwal WOC (War Of Crystal) pukul 21.00 WIB. Bagi yang berada di luar area Indonesia Barat harap sesuaikan jam kalian.

Kumpul di guild hall pukul 20.30 WIB untuk briefing dan persiapan. Jika diperlukan, belanja buff & potion di black cat cafe yang ada di guild hall (posisi dekat vending machine), lalu siapkan juga equip PVP kalian (damage to demi human). Buff stone dari exchange disarankan beli wind dmg immunity, gunakan pet yang nambahin max HP atau penetration.

Bagi yang belum paham mekanisme WOC, bisa tonton video berikut sampai habis ya:

https://www.youtube.com/watch?v=C1sOqt-vTv0&t=352s

**Kenapa kalian harus ikut WOC ?**
1. Sebagai kompensasi WOE pada hari kamis, jika kita mendapatkan kastil satu, diijinkan ikut WOC untuk tambahan honor proof dan praying card (sekali lagi, ini penting untuk perkembangan char kalian) (¬‿¬ )

2. Sebagai bentuk solidaritas antar member guild untuk saling bahu membahu saat war, bisa mempererat pertemanan juga (; ω ; )ヾ(´∀`* )

3. Sebagai lahan latihan kalian juga PVP, terlepas dari menang atau kalah, didominasi atau mendominasi. Jam terbang menjadi salah satu parameter penting untuk char kalian (￣ε￣＠)

Silakan bersiap-siap, have fun, and always focus yak. Semangat (^_<)"""

def _monday():
  print("monday reminder")
  return """Hai member CALAVERA ヾ(*'▽'*)

Selamat hari senin semuanya, waaw ga kerasa udah awal minggu aja nih. Gimana weekend kalian dan WOC kemarin ?? seru ga ?

Rasifu mau kasih tau buat para member nih, buat yang belum tau mekanisme weekly di ragnarok mobile, setiap hari senin tuh ada weekly reset loh (¯ ¯٥)

Itu artinya kalian udah mulai bisa ambil lagi ET, VR, Purgatory, Ora, Thanatos, hadiahnya berjibun.

Buat kalian yang butuh bantuan/ menawarkan bantuan bisa komen ya di room <#801368159520555019> supaya chat di sini tidak ketutup. Tunggu apalagi, yuk weekly skrg, rasifu duduk aja (=^･ω･^=) """

def _wednesday():
  print("reminder every wednesday")
  return """Hai member CALAVERA ヾ(*'▽'*)

Selamat hari rabu semuanya, semoga hasil farming kalian memuaskan yak ( ◡‿◡ *)

Kalian tau ga setiap hari rabu tuh ada event lho.. Loh pada ga tau ya? sini Rasifu kasih tau hihi (=^･ω･^=)

Jadi kalau kalian cek kalender asisten, nah ada tuh di situ penjelasan hari rabu sedang event apa (ada ufo west gate, kafra battle). Setiap minggu event-nya ganti2, tapi selalu di hari rabu. Jadi jangan lupa untuk ikut event-nya gaes, seru lho rame + kalian bisa dapat hadiah flora star coin yang bisa ditukarkan dengan sejumlah hadiah menarik!

Event ini tidak butuh party kok, tapi kalau kalian mau bikin supaya makin solid, silakan bikin.

Tunggu apa lagi, yuk cek kalender kalian lalu standby sebelum jam 20.00 WIB karena eventnya hanya berlangsung 20.00-20.30 WIB saja.

Jangan sampai ketinggalan ya, (^_<)"""

def _room():
  return """FYI nih, di discord kita ada banyak room loh untuk klinik banyak hal ヾ(☆▽☆)

**Ada room untuk general purpose seperti :**
  - <#715964928757858318>   = ini room untuk kita semua ngobrol dan berkumpul
  - <#801368159520555019>   = kalian bisa request GB disini, tag petinggi juga ya (⌒ω⌒)
  - <#799242789128241163>   = room ini khusus untuk share info seputar event sejagad midgard (¬‿¬ )
  - <#719440896143261786>   = dsini info untuk weekly seperti ET, VR, Oracle
  - <#799194177668907039>   = yang ini jangan masuk, serius (⇀_⇀)
  - <#813794836846870558>   = Room ini ibarat modul kita bersama guys. Di dalam room ini terdapat banyak info-info penting yang terkadang bisa nyelametin kita dari kepala pusing lho. Penasaran? yuk cekidot langsung roomnya kk (^_^)
  - <#817758311272153118> = Bagi pecinta seni, pelaku seni, penikmat seni silakan mampir ke room ini untuk diskusi & sharing, siapa tau bisa tuker ilmu baru.
  - <#817301651001573376>  = Bagi para orang gabut yang butuh hiburan, silakan mampir ke room ini untuk main tebak-tebakan, siapa tau hari anda menjadi cerah. Buat yang punya tebak2an lucu, tebak2an porno, tebak2an ga lucu, tebak2an dark, atau cuma mau bantu jawab, silakan komen di room ini ya.
  - <#801652022025519125>   = ini room aku untuk belajar (◕‿◕)♡"""

def _room2():
  return """
  **Ada room khusus untuk klinik masing-masing job seperti :**
  - <#796991088568303646>   = room khusus penyihir hebat, tapi kalo santet gabisa sepertinya ლ(¯ロ¯"ლ)
  - <#796991201513177090>   = ini room tempat kumpul pengguna panah, pisau ada juga sih. Tapi inget kalo tanya build harus siap modal |･ω･)
  - <#796991534729003029>   = nah ini room untuk asinan (/▿＼ ) para pencuri yang GG gitu lah
  - <#796991873511325696>   = yang satu ini room bebas stress, karena banyak kucing (^=◕ᴥ◕=^)
  - <#796992240991993876>   = stttt,.. disini tempat orang-orang suci (︶︹︺)
  - <#797004285459562537>   = yang ini gatau kepake engga, yang nunggu orang magang (っ˘̩╭╮˘̩)っ
  - <#797004473313525772>   = ini room untuk pedagang, tukang mesin, sama ilmuan gila ヽ(￣～￣　)ノ
  - <#800955828613808159>   = hmmmm,, ini room rada sepi soalnya build job ini untuk sultan katanya (￣ﾊ￣*)
  - <#811304917486272543>   = Room untuk job pecinta naruto/batman/tenchu. Inovasi terbaru pada episode 8 ini menyenangkan lho, char ninja lincah, animasinya seru, bisa ninjutsu juga...psst mountnya kodok loncat FYI
  - <#817653331513835520>  = Bagi player super novice, telah dibuka room klinik baru. Silakan mampir ke room ini kalau kalian ingin menjadi player yang tidak adil terhadap player lain. HIHIHI
  
Voice juga tersedia jika butuh loh. Kalau butuh GB, silakan tag member di sini supaya bisa diingatkan. Coba deh mampir ke room lain untuk liat-liat (^ω~)"""



async def _my_act():
    while True:
        await client.change_presence(activity = discord.Activity(
          type = discord.ActivityType.watching, 
          name = random.choice(movie)))
        await asyncio.sleep(7200)

def _check_event():
  today = datetime.now(tz=tz)
  if str(today.strftime("%A")).lower() == "wednesday":
    return """Kafra Battle/ Big Cat UFO event, mulai dari jam 20.00-20.30 WIB. Jadi, kalian gaboleh kelewat event satu ini yak karena di event ini kalian bisa dapetin Flora star coin yang bisa dituker banyak item bagus (^.~)☆"""

  elif str(today.strftime("%A")).lower() == "thursday":
    return """WOE (War Of Emperium), war antar guild buat dapetin kastil gitu. Mulai dari jam 21.00 sampai selesai, kalau udah punya kastil wajib dipertahanin \(￣ﾊ￣)

Di event ini kalian bisa dapet Pray card yang bisa dipakai untuk naikin serangan/ pertahanan kalian, dan ada juga honor proof yang bisa dituker dengan banyak item di Vending Machine dalam Guild Hall. So, jangan sampai ketinggalan yak (｡•̀ᴗ-)✧"""

  elif str(today.strftime("%A")).lower() == "sunday":
    return """WOC (War Of Crystal), ini tuh war anatar guild juga tapi hanya untuk yang punya kastil 1 di event WOE kemarin. Jadi hanya guild terpilih aja yang bisa war :D

Event dimulai jam 21.00 WIB sampai selesai, seperti WOE di event ini kalian juga akan dapat Pray Card sama Honor Proof. So, jangan sampai ketinggalan yak (^.~)"""

  elif str(today.strftime("%A")).lower() == "monday":
    return """Wah udah awal minggu nih (ﾉ´ з `)ノ

Seperti biasa semua dungeon akan di reset tiap awal minggu, jadi untuk hari ini banyak sekali aktifitas yang kalian bisa lakuin dan bisa kalian cek di menu asisten in game kalian 	( ´ ▽ ` ) 

- **Endless Tower (ET)**, dungeon 100 lantai yang bisa drop item rare bahkan equipment juga
- **Oracle**, dungeon kartu acak gitu nanti keluar monster sesuai kartu. Reward nya ada nolan card loh yang bisa kalian pakai untuk craft kartu di king poring
- **Thanatos Tower**, wah ini dungeon berat dan reward nya yang dicari itu bahan untuk rune. Kalian bisa dapet rune bagus dari dungeon ini
- **Valhalla Ruin**, dungeon di guild yang isinya 5 MVP/Mini dan reward nya mirip seperti di ET
- **Echoing Corridor (EC)**, ini dungeon yang makan waktu cukup lama tapi reward nya oke juga loh bisa dapet brave emblem
- **Battle Of Cake (BOC)**, ini dungeon yang makan CT kalian jadi pastikan CT nya hijau ya. Reward di reset tiap minggu bisa dapet kartu/ headware secara acak

semua weekly ini bisa kalian dapet info nya di room <#719440896143261786>, semangat hari senin (((o(*°▽°*)o)))"""

  else:
    return "Maaf ya ga ada event apapun hari ini (*_ _)人"

async def _check_schedule():
    print("--run schedule check--")
    while True:
        today = datetime.now(tz=tz)
        await client.get_user(senpai).send("--schedule check on {} @{}:{}--".format(str(today.strftime("%A")),str(today.strftime("%H")),str(today.strftime("%M"))))
        # print("day = {}".format(str(today.strftime("%A")).lower()))
        # print("hour = {}".format(int(today.strftime("%H"))))
        # print("minute = {}".format(int(today.strftime("%M"))))
        


        hour = today.strftime("%H")
        mi = int(today.strftime("%M"))

        if any(hour in s for s in reminder_hour) and mi < 3:
          if str(today.strftime("%A")).lower() == "wednesday":
              await client.get_user(senpai).send("--run wednesday reminder--")
              await client.get_channel(gh).send(_wednesday())

          elif str(today.strftime("%A")).lower() == "thursday":
              await client.get_user(senpai).send("--run woe reminder--")
              await client.get_channel(gh).send(_woe())

          elif str(today.strftime("%A")).lower() == "sunday":
              await client.get_user(senpai).send("--run woc reminder--")
              await client.get_channel(gh).send(_woc())

          elif str(today.strftime("%A")).lower() == "monday":
              await client.get_user(senpai).send("--run monday reminder--")
              await client.get_channel(gh).send(_monday())
              

        await asyncio.sleep(180)

def _apologize(ctx):
  person = " "
  if len(ctx.message.mentions) > 0:
    person = ctx.message.mentions[0].display_name.split(" ")
  return "{} {} m(_ _)m".format(random.choice(ask_sorry), person[0])

def _schedule():
  return """Jadwal GB lead & vice lead CALAVERA

Lead: Lockdown
Jam AFK: 07.00-19.00 WIB
Jam aktif: 20.00-23.00 WIB (kecuali hari senin)
Availability: VR, purga, et, boc, wasteland elite, ora normal, ora hard (jika tidak ada monster reflect)

Vice Lead: Frankova
Jam AFK: 07.00-22.00 WIB
Jam aktif: 23.00-00.00 WIB
Availability: VR, Purgatory, ET, Elite Wasteland, Oracle Normal

Vice Lead: Rashiva
AFK: 08.00 - 19.00
Aktif: 
- pasti aktif : senin, 06.00-07.00 -> 19.00 - sleep
- rada aktif: all day, 19.00 - bored
Service: BOC, ET, VR, EC f1-10, Elite


Notes: Kesempatan besar bagi kalian yang membutuhkan bantuan adalah setelah selesai WOE/WOC karena sebagian besar leads pasti akan on, dan bisa dimintakan bantuan"""


def _thank():
  return """asdasdsa"""
# =================================================================================



@client.event
async def on_ready():
    client.loop.create_task(_my_act())
    client.loop.create_task(_check_schedule())
    print('We have logged in as {0.user}'.format(client))
    await client.get_user(senpai).send("--im alive--")


@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await client.get_user(senpai).send("--{} join guild--".format(member.name))
    await client.get_channel(gh).send(_welcome_greeting(member.mention))
    time.sleep(0.5)
    await client.get_channel(gh).send("Aku ada info nih (^０^)ノ \n ...")
    time.sleep(1)
    await client.get_channel(gh).send(_notes())
    time.sleep(0.7)
    await client.get_channel(gh).send("Untuk list command yang bisa aku bantu ketik $help yak ♡＼(￣▽￣)／♡")
    time.sleep(1)
    await client.get_channel(gh).send("Ups, ada lagi ...")
    time.sleep(0.5)
    await client.get_channel(gh).send(_room())
    await client.get_channel(gh).send(_room2())

@client.event
async def on_member_update(before,after):
    print("Recognized that " + before.name + " update")
    # if before.status is client.Status.offline and after.status is client.Status.online:
    #   await client.get_channel(bot_room).send("{} appear".format(before.display_name.split(" ")[0]))


@client.event
async def on_member_remove(member):
    await client.get_user(senpai).send("--{} leave guild--".format(member.name))
    print("Recognized that " + member.name + " left")
    time.sleep(0.5)
    await client.get_channel(gh).send(_leave_msg(member.name))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
      
    await client.process_commands(message)
    


# =====================================================


@client.group(
  pass_context=True,
  help="",
	brief="Panggil Rasifu untuk membantu",
  invoke_without_command=True,
)
async def ras(ctx):
  if str(ctx.author) == whitelist_member[0]:
    time.sleep(0.5)
    await ctx.channel.send("Yes, My Lord (*^‿^*)")
  elif str(ctx.author) == whitelist_member[1]:
    time.sleep(0.5)
    await ctx.channel.send(random.choice(master_answ))
  else:
    time.sleep(0.5)
    await ctx.channel.send(random.choice(greeting))

@ras.command(
  help="",
	brief="Rasifu bisa bantu ucapkan salam",
)
async def welcome(ctx):
  await ctx.channel.send(_notes())

@ras.command(
  help="",
	brief="Rasifu minta maaf",
)
async def apologize(ctx):
  await ctx.channel.send(_apologize(ctx))

@ras.group(
  pass_context=True,
  help="",
	brief="Rasifu bisa bantu untuk mengingatkan",
  invoke_without_command=True,
)
async def reminder(ctx):
  await ctx.channel.send("Reminder apaan 	(・・ ) ?")

@reminder.command()
async def woe(ctx):
  time.sleep(0.5)
  await ctx.channel.send(random.choice(ask_attention))
  time.sleep(0.8)
  await ctx.channel.send(_woe())

@reminder.command()
async def woc(ctx):
  time.sleep(0.5)
  await ctx.channel.send(random.choice(ask_attention))
  time.sleep(0.8)
  await ctx.channel.send(_woc())

@reminder.command()
async def wednesday(ctx):
  time.sleep(0.5)
  await ctx.channel.send(_wednesday())

@reminder.command()
async def monday(ctx):
  time.sleep(0.5)
  await ctx.channel.send(_monday())

@reminder.command()
async def check(ctx):
  time.sleep(0.5)
  await ctx.channel.send("Event untuk hari ini itu ...")
  time.sleep(0.5)
  await ctx.channel.send(random.choice(ask_for_wait))
  time.sleep(0.9)
  await ctx.channel.send(_check_event())

@ras.command(
  help="",
	brief="Rasifu bisa bantu usir pengganggu",
)
async def kick(ctx, *args):
  time.sleep(0.5)
  await _kik_member(ctx,args)

@ras.group(
  pass_context=True,
  help="",
	brief="Rasifu bisa bantu kasih informasi",
  invoke_without_command=True,
)
async def info(ctx):
  time.sleep(0.5)
  await ctx.channel.send("Mau info apa ? (⁀ᗢ⁀)")

@info.command()
async def room(ctx):
  time.sleep(0.5)
  await ctx.channel.send(_room())
  await ctx.channel.send(_room2())

@ras.group(
  pass_context=True,
  help="",
	brief="Rasifu bisa bantu kasih informasi jadwal",
  invoke_without_command=True,
)
async def jadwal(ctx):
  time.sleep(0.5)
  await ctx.channel.send("Mau jadwal apa ? (⁀ᗢ⁀)")

@jadwal.command()
async def gb(ctx):
  time.sleep(0.5)
  await ctx.channel.send(_schedule())

@ras.group(
  pass_context=True,
  help="",
	brief="Rasifu marah",
  invoke_without_command=True,
)
async def anger(ctx):
  person = " "
  if len(ctx.message.mentions) > 0:
    person = ctx.message.mentions[0].display_name.split(" ")
  time.sleep(0.5)
  await ctx.channel.send("{} {}".format(random.choice(react_anger), person[0]))




keep_alive()
client.run(os.getenv('TOKEN'))