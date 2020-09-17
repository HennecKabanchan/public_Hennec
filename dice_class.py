import random
import re
import math


# diceを扱うクラス
class Dice:
    def __init__(self, raw_command):
        self.dices = re.sub(r"/hx|/h| ", "", raw_command)


# 普通のダイスを扱うクラス
class Ndn(Dice):
    def __init__(self, h_com):
        super().__init__(h_com)
        self.format_dice = self.diceformula(self.dices)

    # 送信されたダイス込の文字列をevalで計算できる形にフォーマットしたものを返すメソッド
    def diceformula(self, mes):

        d_formula = mes

        for operand in re.split(r"[+\-*/^]", mes):
            print(f"operand={operand}")
            if re.search("[dDｄ]", operand):
                if re.fullmatch("[dDｄＤ][6６][6６]", operand):
                    print("d66")
                    d_formula = re.sub("[dDｄＤ][6６][6６]", "({})".format(
                        self.d66_dice(operand)), d_formula, 1)

                else:
                    print("ndn")
                    if re.fullmatch(r"[dDｄＤ]\d+", operand):
                        # d?のダイスだった場合1d?に変換する
                        d_formula = d_formula.replace(operand, "1"+operand)
                        operand = "1" + operand

                    d_formula = re.sub(
                        r"\d+[dDｄＤ]\d+", "({})".format(self.ndn_dice(operand)), d_formula, 1)

            elif "!" in operand:
                print("!")
                operand = operand[:-1]
                d_formula = re.sub(
                    r"\d+!", "({})".format(str(math.factorial(int(operand)))), d_formula, 1)

            print(f"d_formula={d_formula}")

        return d_formula

    # d66ダイスを振った結果を文字列で返すメソッド
    def d66_dice(self, d66):

        dice = ""

        for _ in range(2):
            dice += str(random.randint(1, 6))
        if int(dice[1]) < int(dice[0]):
            buf = str(dice[0])
            dice = dice[1:2]
            dice += buf
        print(f"dice={dice}")

        return dice

    # 普通のダイスを振った結果を文字列で返すメソッド
    def ndn_dice(self, ndn):
        dice = ""

        ndn_spl = re.split("[dDｄＤ]", ndn)  # [0]:num, [1]:dn

        for _ in range(int(ndn_spl[0])):
            dice += str(random.randint(1, int(ndn_spl[1]))) + "+"

        dice = dice[:-1]

        return dice


# DX3のダイスを扱うクラス
class DX3(Dice):
    def __init__(self, h_com):
        super().__init__(h_com)
        self.format_dice = self.dx3formula(self.dices)

    # DX3の判定ダイスの結果を文字列にして返すメソッド
    def dx3formula(self, ncrif_val):  # num:個数 critical:C値 fixed_value:固定値

        # [0]:num, [1]:critical, [2]:fixed_value
        ncrif_val_spl = re.split("[,@＠]", ncrif_val)
        dx3_formula = "("
        max_dice = 0  # 判定ダイスの最大値
        add_dice = 0  # 追加で振るダイスの個数
        rep_num = int(ncrif_val_spl[0])
        rep_count = 0  # 何回振りなおしたかをカウントする
        dx3o = 0  # dx3_out 達成値

        while 0 < rep_num:
            rep_num -= 1
            d10 = random.randint(1, 10)

            if max_dice < d10:
                max_dice = d10

            if d10 >= int(ncrif_val_spl[1]):
                add_dice += 1

            dx3_formula += str(d10) + ","

            if rep_num == 0:
                dx3_formula = dx3_formula[:-1]
                dx3_formula += ")+("

                if 0 < add_dice:
                    rep_num = add_dice
                    add_dice = 0
                    max_dice = 0
                    rep_count += 1
                    continue

        dx3_formula = dx3_formula[:-2]
        dx3_formula += "+" + ncrif_val_spl[2]
        print(f"rep_count{rep_count}")
        dx3o = rep_count*10 + max_dice + int(ncrif_val_spl[2])

        return dx3_formula, dx3o
