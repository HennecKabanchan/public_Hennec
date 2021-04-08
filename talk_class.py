import fennec_text

import random
import re
from datetime import datetime as dt
from datetime import time as hms  # hour minutes second
from pytz import timezone


class NotCommandError(Exception):  # main でelseに入ったときのための例外クラス
    pass


# Hello_hennecがしゃべるためのクラス
class Talk():
    def __init__(self, in_mes):  # input message object
        self.mes = in_mes

    # discordにメッセージを送信するメソッド
    def talk(self, comment):
        return self.mes.channel.send(f"{self.mes.author.mention} : {comment}")

    # 呼ばれたときに返事をするメソッド
    def hey_hennec(self, h_me):
        return self.talk(f"はーいよー{h_me}ですよー")

    def bye_hennec(self):
        return self.talk(f"はーいよー\n{random.choice(fennec_text.BYE_MES)}")

    def like_a_light(self):
        return self.talk(f"{random.choice(fennec_text.ARAI_MES)}")

    # エラーメッセージを送信するメソッド
    def err_talk(self, err):
        if ZeroDivisionError is err:
            return self.talk(f"{random.choice(fennec_text.ZERO_ERR_MES)}")
        else:
            return self.talk(f"{random.choice(fennec_text.ERR_MES)}")

    def tired_talk(self):
        return self.talk(f"{random.choice(fennec_text.TIRED_MES)}")

    def welcome_back_talk(self):
        return self.talk(f"{random.choice(fennec_text.WELCOME_BACK_MES)}")

    def energy_talk(self):
        return self.talk(f"{random.choice(fennec_text.ENERGY_MES)}")

    def what_time_talk(self):
        self.time_now = dt.now(timezone("Asia/Tokyo")).time()
        return self.talk(f"えーとねー\n今は{self.time_now}だよー")


# 挨拶のためのクラス
class Greet(Talk):
    def __init__(self, h_com):
        super().__init__(h_com)

    # morning greet
    M_GREETS = {
        "gn": fennec_text.Ohayo_fennec.GOOD_NIGHT_MES,
        "bt": fennec_text.Ohayo_fennec.BAD_TIME_MES,
        "em": fennec_text.Ohayo_fennec.EARLY_MORNING_MES,
        "mo": fennec_text.Ohayo_fennec.MORNING_MES,
        "lm": fennec_text.Ohayo_fennec.LATE_MORNING_MES,
        "lu": fennec_text.Ohayo_fennec.LUNCH_MES,
        "na": fennec_text.Ohayo_fennec.NAP_TIME_MES,
        "ev": fennec_text.Ohayo_fennec.EVENING_MES,
        "di": fennec_text.Ohayo_fennec.DINNER_MES
    }
    # hello greet
    H_GREETS = {
        "gn": fennec_text.Konniti_fennec.GOOD_NIGHT_MES,
        "bt": fennec_text.Konniti_fennec.BAD_TIME_MES,
        "em": fennec_text.Konniti_fennec.EARLY_MORNING_MES,
        "mo": fennec_text.Konniti_fennec.MORNING_MES,
        "lm": fennec_text.Konniti_fennec.LATE_MORNING_MES,
        "lu": fennec_text.Konniti_fennec.LUNCH_MES,
        "na": fennec_text.Konniti_fennec.NAP_TIME_MES,
        "ev": fennec_text.Konniti_fennec.EVENING_MES,
        "di": fennec_text.Konniti_fennec.DINNER_MES
    }
    # good evening greet
    E_GREETS = {
        "gn": fennec_text.Konban_fennec.GOOD_NIGHT_MES,
        "bt": fennec_text.Konban_fennec.BAD_TIME_MES,
        "em": fennec_text.Konban_fennec.EARLY_MORNING_MES,
        "mo": fennec_text.Konban_fennec.MORNING_MES,
        "lm": fennec_text.Konban_fennec.LATE_MORNING_MES,
        "lu": fennec_text.Konban_fennec.LUNCH_MES,
        "na": fennec_text.Konban_fennec.NAP_TIME_MES,
        "ev": fennec_text.Konban_fennec.EVENING_MES,
        "di": fennec_text.Konban_fennec.DINNER_MES
    }
    # good night greet
    N_GREETS = {
        "gn": fennec_text.Oyasumi_fennec.GOOD_NIGHT_MES,
        "bt": fennec_text.Oyasumi_fennec.BAD_TIME_MES,
        "em": fennec_text.Oyasumi_fennec.EARLY_MORNING_MES,
        "mo": fennec_text.Oyasumi_fennec.MORNING_MES,
        "lm": fennec_text.Oyasumi_fennec.LATE_MORNING_MES,
        "lu": fennec_text.Oyasumi_fennec.LUNCH_MES,
        "na": fennec_text.Oyasumi_fennec.NAP_TIME_MES,
        "ev": fennec_text.Oyasumi_fennec.EVENING_MES,
        "di": fennec_text.Oyasumi_fennec.DINNER_MES
    }

    GOOD_NIGHT = [hms(21), hms(23, 59, 59), hms(0)]
    BAD_TIME = hms(1)
    EARLY_MORNING = hms(3)
    MORNING = hms(6)
    LATE_MORNING = hms(9)
    LUNCH = hms(11)
    NAP_TIME = hms(14)
    EVENING = hms(17)
    DINNER = hms(19)

    def send_greet(self, author_name):
        self.time_now = dt.now(timezone("Asia/Tokyo")).time()
        # 時間テスト用
        # self.time_now = hms(14)

        # 21時から23時59分59秒;good night:gn
        if Greet.GOOD_NIGHT[0] <= self.time_now and self.time_now <= Greet.GOOD_NIGHT[1]:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー\nもうおやすみだねー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['gn'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにちはー\nもうすぐおやすみの時間だねー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['gn'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['gn'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['gn'])}")

        # 0時から1時;good night:gn
        elif Greet.GOOD_NIGHT[2] <= self.time_now and self.time_now < Greet.BAD_TIME:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー\nもうおやすみの時間かなー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['gn'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにちはー\nもうおやすみだねー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['gn'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['gn'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['gn'])}")

        # 1時から3時;bad time:bt
        elif Greet.BAD_TIME <= self.time_now and self.time_now < Greet.EARLY_MORNING:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おやおやー？{author_name}だねー 今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['bt'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"あらあらー？{author_name}だー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['bt'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['bt'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['bt'])}")

        # 3時から6時;early morning:em
        elif Greet.EARLY_MORNING <= self.time_now and self.time_now < Greet.MORNING:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['em'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにち…おっとと…\n今の時間だとおはようかなー？{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['em'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['em'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['em'])}")

        # 6時から9時;morning:mo
        elif Greet.MORNING <= self.time_now and self.time_now < Greet.LATE_MORNING:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー…{author_name}ー 今はー{self.time_now.strftime('%H:%M')}だねー…\nふぁあ…アライさんの朝ごはん用意しなきゃねー\n{random.choice(Greet.M_GREETS['mo'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こーんにちはー{author_name}ー\n…あーおはよーかなー？ \n今は{self.time_now.strftime('%H:%M')}だよー…\n{random.choice(Greet.H_GREETS['mo'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['mo'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['mo'])}")

        # 9時から11時;late morning:lm
        elif Greet.LATE_MORNING <= self.time_now and self.time_now < Greet.LUNCH:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー{author_name}ー 今はもう{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['lm'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにちは、{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n今日はいい天気かなー？\nどうだろーなー？\n{random.choice(Greet.H_GREETS['lm'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['lm'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['lm'])}")

        # 11時から14時;lunch:lu
        elif Greet.LUNCH <= self.time_now and self.time_now < Greet.NAP_TIME:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー\nもうこんにちはの時間かな？{author_name}ー 今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['lu'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こーんにちはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\nお昼ごはんはたべたかい？\n私はじゃぱりまんを食べたよー\n{random.choice(Greet.H_GREETS['lu'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['lu'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['lu'])}")

        # 14時から17時;nap time:na
        elif Greet.NAP_TIME <= self.time_now and self.time_now < Greet.EVENING:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよう{author_name}ー\nもうじき夕方になるねー\n今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['na'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにちはだねー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['na'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['na'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['na'])}")

        # 17時から19時;evening:ev
        elif Greet.EVENING <= self.time_now and self.time_now < Greet.DINNER:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー\nおっと、今の時間はこんばんはかなー？{author_name}ー\n今はもう{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['ev'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにちは{author_name}ー\nもうそろそろこんばんはでもいいかな？\n今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['ev'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.E_GREETS['ev'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"{random.choice(Greet.N_GREETS['ev'])}\nおやすみー{author_name}ー")

        # 19時から21時;dinner:di
        elif Greet.DINNER <= self.time_now and self.time_now < Greet.GOOD_NIGHT[0]:
            if "gm" == self.wtgreet(self.mes.content):
                return self.talk(f"おはよー{author_name}ー\nもうこんばんはだねー\n 今は{self.time_now.strftime('%H:%M')}だねー\n{random.choice(Greet.M_GREETS['di'])}")
            elif "he" == self.wtgreet(self.mes.content):
                return self.talk(f"こんにちはー{author_name}ー\nもうお昼は終わっちゃったけどねー\n 今は{self.time_now.strftime('%H:%M')}だよー\n{random.choice(Greet.H_GREETS['di'])}")
            elif "ge" == self.wtgreet(self.mes.content):
                return self.talk(f"こんばんはー{author_name}ー 今は{self.time_now.strftime('%H:%M')}だよー\nもう夕飯は食べたかい？\n{random.choice(Greet.E_GREETS['di'])}")
            elif "gn" == self.wtgreet(self.mes.content):
                return self.talk(f"おやー？\n今日は早寝だねー\nおやすみ{author_name}ー\n{random.choice(Greet.N_GREETS['di'])}")

        print("err time or not common greets")
        return self.talk(f"やあやあ{author_name}ー 今は{self.time_now.strftime('%H:%M')}さー")

    def wtgreet(self, greet):  # What greet
        if re.search(r"おは", greet):
            return "gm"
        elif re.search(r"こんにち", greet):
            return "he"
        elif re.search(r"ばん", greet):
            return "ge"
        elif re.search(r"おやすみ", greet):
            return "gn"
