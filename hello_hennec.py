import hen_func
import fennec_text

client = hen_func.discord.Client()


@client.event
async def on_ready():
    print("ろぐいんしたよー")


@client.event
async def on_message(message):
    if client.user == message.author:
        return

    h_command = message.content
    if h_command.startswith("/h"):
        print("こまんどをうけとったよー")
        print(f"h_command={h_command}")

        try:

            if h_command.startswith("/ht help") or h_command.startswith("/ht　help"):
                await message.channel.send(f"やーやーフェネックなのさー\n私ができることをちょっと紹介するよー\n/h って打つとーダイスを含めた計算ができるよー\n例えばー…")
                testcommand = f"{hen_func.random.randint(1,20)}" + "d" + f"{hen_func.random.randint(1,20)}" + \
                    "+" + \
                    f"d{hen_func.random.randint(10,100)}" + \
                    "-" + f"{hen_func.random.randint(1,10)}"
                tst_f = hen_func.diceformula(testcommand)
                await message.channel.send(f"/h {testcommand}")
                await message.channel.send(f"<@560897067401216001> : `{testcommand}` = {tst_f} = **{eval(tst_f.replace('^', '**'))}**")
                await message.channel.send("こんな感じだねー")

                await message.channel.send("ほかにはー\n/hx って打つとDX3の判定ができるよー")
                testcommand = f"{hen_func.random.randint(5,20)}" + "@" + f"{hen_func.random.randint(7,10)}" + \
                    "," + \
                    f"{hen_func.random.randint(0,10)}"
                tst_f_dx3 = hen_func.dx3formula(testcommand)
                await message.channel.send(f"/hx {testcommand}")
                await message.channel.send(f"<@560897067401216001> : `DX3({testcommand})` = {tst_f_dx3[0]} = **{tst_f_dx3[1]}**")
                await message.channel.send("こんなふうにー[ダイスの個数]@[C値],[固定値]って打ってねー")

                await message.channel.send("まーコマンドはアライさんみたいにごーかいに打ってもだいじょうぶだからあんしんしてねー")

                await message.channel.send("それじゃあまたねー")

            elif h_command.startswith("/h help") or h_command.startswith("/h　help"):
                await message.channel.send(">>> {:<9} {:<30}ex.{}\n{:<11} {:<23}ex.{}".format("CoC etc.", "/h [個数]d[種類]", "/h 1d6+1d4+1", "DX3", "/hx [n]@[C値],[固定値]", "/hx 10@7,5"))

            elif h_command.startswith("/hx"):
                h_command = hen_func.com_replace(h_command)
                dx3f = hen_func.dx3formula(h_command)
                print(f"dx3f={dx3f}")
                await message.channel.send(f"{message.author.mention} : `DX3({h_command})` = {dx3f[0]} = **{dx3f[1]}**")

            else:
                h_command = hen_func.com_replace(h_command)
                df = hen_func.diceformula(h_command)
                # "の中に"を使うことができないため'を使用する
                await message.channel.send(f"{message.author.mention} : `{h_command}` = {df} = **{eval(df.replace('^', '**'))}**")

        except ZeroDivisionError as err:
            print("ZeroDivisionErrorだよー:", err)
            await message.channel.send(f"{message.author.mention} : {hen_func.random.choice(fennec_text.zero_err_mes)}")
        except SyntaxError as err:
            print("SyntaxErrorだよー:", err)
            await message.channel.send(f"{message.author.mention} : {hen_func.random.choice(fennec_text.err_mes)}")
        except ValueError as err:
            print("ValueErrorだよー:", err)
            await message.channel.send(f"{message.author.mention} : {hen_func.random.choice(fennec_text.err_mes)}")
        except NameError as err:
            print("NameErrorだよー:", err)
            await message.channel.send(f"{message.author.mention} : {hen_func.random.choice(fennec_text.err_mes)}")

client.run("TOKENを入力してね")
