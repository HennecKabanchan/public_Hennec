# main file

import dice_class
import talk_class
from talk_class import Talk
from talk_class import NotCommandError

import re
import discord


client = discord.Client()


# test_hennec TOKEN
# BOT_TOKEN = "NzUxNDMyMDE1NDMzMTcxMDY1.X1I_mQ.chRAjOVAZcMFtf2B85BlnpASPoU"
# Hello_hennec TOKEN
BOT_TOKEN = "NTYwODk3MDY3NDAxMjE2MDAx.XJ0WGQ.E39b-lyHAwv2yuwGOVGCqKibPik"


# 反応する言葉群
class Res_words():
    START_COMMAND = r"/h"
    HELP = r"/h help"
    DX3 = r"/hx"
    DICE = r"/h \d*[dDｄＤ]\d+"
    FACTIONAL_AND_NUM = r"!|[0-9]+"
    GREETS = r"おは|こんにち|ばん|おやす|こんち|きげん|機嫌|ちょうし|調子|げんき|元気"
    BYE = r"ばい|さよ"
    HENNEC = r"へねっく|ヘネック|へネック|ふぇねっく|フェネック"
    BARK = r"こゃーん"
    ARAISAN = r"アライ"
    TIRED = r"つか"
    WELCOME_BACK = r"おかえり"


@client.event
async def on_ready():
    print("じゅんびできたよー")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    print(f"message.content={message.content}")
    h_command = message.content
    if h_command.startswith(Res_words.START_COMMAND):
        h_command = re.sub(r"　", r" ", h_command)
        print("こまんどをうけとったよー")

        # Errorのときに動作が止まらないようにtryする
        try:
            # エラーメッセージを送信するために実体を作っておく
            err_mes = Talk(message)

            # ヘルプコマンド
            if re.match(Res_words.HELP, h_command):
                print("help")
                await message.channel.send(">>> {:<9} {:<30}ex.{}\n{:<11} {:<23}ex.{}".format(
                    "CoC etc.", "/h [個数]d[種類]", "/h 1d6+1d4+1", "DX3", "/hx [n]@[C値],[固定値]", "/hx 10@7,5"))

            # DX3のダイス計算
            elif re.match(Res_words.DX3, h_command):
                print("DX3")
                dx3d = dice_class.DX3(h_command)
                dx3_mes = Talk(message)
                await dx3_mes.talk(f"`DX3({h_command})` = {dx3d.format_dice[0]} = **{dx3d.format_dice[1]}**")

            # 普通のダイス計算
            elif re.match(Res_words.DICE, h_command) or re.search(Res_words.FACTIONAL_AND_NUM, h_command):
                print("dice")
                dice = dice_class.Ndn(h_command)
                # "の中に"を使うことができないため'を使用する
                dice_mes = Talk(message)
                await dice_mes.talk(f" `{dice.dices}` = {dice.format_dice} = **{eval(dice.format_dice.replace('^', '**'))}**")

            # しゃべるへねっく
            elif re.search(Res_words.GREETS, h_command):
                print("greet")
                gm_mes = talk_class.Greet(message)
                await gm_mes.send_greet(re.sub(r"#[0-9]*", "", str(message.author)))

            elif re.search(Res_words.BYE, h_command):
                print("byebye")
                gb_mes = talk_class.Talk(message)
                await gb_mes.bye_hennec()

            elif re.search(Res_words.HENNEC, h_command):
                print("reply")
                hennec_me = re.search(Res_words.HENNEC, message.content)
                reply = Talk(message)
                await reply.hey_hennec(hennec_me[0])

            elif re.search(Res_words.BARK, h_command):
                print("bark")
                bark = Talk(message)
                await bark.talk(f"こゃーん")

            elif re.search(Res_words.ARAISAN, h_command):
                print("らいくあらいと")
                lal = Talk(message)
                await lal.like_a_light()

            elif re.search(Res_words.TIRED, h_command):
                print("つかれた")
                tired = Talk(message)
                await tired.tired_talk()

            elif re.search(Res_words.WELCOME_BACK, h_command):
                print("おかえり")
                welcome_back = Talk(message)
                await welcome_back.tired_talk()

            else:
                print("else")
                raise NotCommandError("やってしまったねーアライさーん")

        except ZeroDivisionError as err:
            print("ZeroDivisionErrorだよー:", err)
            await err_mes.err_talk(ZeroDivisionError)
        except SyntaxError as err:
            print("SyntaxErrorだよー:", err)
            await err_mes.err_talk(SyntaxError)
        except ValueError as err:
            print("ValueErrorだよー:", err)
            await err_mes.err_talk(ValueError)
        except AttributeError as err:
            print("AttributeErrorだよー:", err)
            await err_mes.err_talk(AttributeError)
        except TypeError as err:
            print("TypeErrorだよー:", err)
            await err_mes.err_talk(TypeError)
        except NameError as err:
            print("NameErrorだよー:", err)
            await err_mes.err_talk(NameError)
        except NotCommandError as err:
            print("NotCommandErrorだよー:", err)
            await err_mes.err_talk(NotCommandError)

        print("end")


client.run(BOT_TOKEN)
