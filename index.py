import discord, asyncio, random

client = discord.Client()

token = "token"

@client.event
async def on_ready():
    print('봇이 실행되었습니다.')

@client.event
async def on_message(message):
    select = []
    clear = []

    if message.content.startswith("$결정"):
        answer = 0
        while answer == 0:
            await message.channel.send("어떤 결정이 필요하십니까?")
            fchoice = await client.wait_for("message")
            if fchoice.content.startswith("선택"):
                schoice = fchoice.content.replace("선택 ","")
                select.append(schoice)
            else:
                await message.channel.send("답변 예시(선택 콜라,선택 사이다)")
            await message.channel.send("추가 결정이 있으십니까? Y/N")
            tchoice = await client.wait_for("message")
            if tchoice.content.startswith("n"):
                answer = 1
            elif tchoice.content.startswith("N"):
                answer = 1
            elif tchoice.content.startswith("y"):
                answer = 0
            elif tchoice.content.startswith("Y"):
                answer = 0
            else:
                await message.channel.send("입력 오류 발생 자동적으로 Y 선택")
                answer = 0
        lchoice = random.choice(select)
        await message.channel.send(lchoice)
        select = clear

    

client.run('token')