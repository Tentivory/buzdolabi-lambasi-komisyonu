#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Lambasi Komisyonu — kapali kapinin resmi gozlemcisi."""

import argparse
import random
import time

KARARLAR = [
    "SONDU: Lamba, karanlikla anlasma imzaladi.",
    "SONMEDI: Lamba kapali kapida da mesai yapiyor, fazla mesai istemiyor.",
    "BELKI: Sensor ifade degistirdi, dosya ust yazıya gitti.",
    "CAY MOLASI: Karar, bardak bitince aciklanacak.",
    "YOGURT ITIRAZ ETTI: Isik yogurdu bozuyormus, lamba suclu bulundu, lamba kabul etmedi.",
]


def gozlem(kapi, tur):
    print("=" * 52)
    print(" BUZDOLABI LAMBASI KOMISYONU  |  OTURUM ACILDI")
    print("=" * 52)
    for n in range(1, tur + 1):
        print(f"\n--- tur {n}/{tur} ---")
        if kapi == "acik":
            print("Kapi acildi. Lamba: 'ben buradayim, sut de buradaydi.'")
            print("Durum: YANIK. Bu kismi kolaydi, komisyon yine de 4 dakika durdu.")
        else:
            print("Kapi kapandi. Gozlemci disarida kaldi. Bu bilimsel bir krizdir.")
            time.sleep(0.15)
            print("Ic ses (duyulmadi): tik.")
            karar = random.choice(KARARLAR)
            print(f"Tutanak: {karar}")
        if n != tur:
            print("Komisyon uyesi: 'bir tur daha, belki lamba bu sefer konusur.'")
    print("\nSONUC: Dosya kapatilmadi. Dosya buzluga kaldirildi.")
    print("Cikis kodu: 0 (lamba da 0 watt iddia ediyor, inanmiyoruz)")


def main():
    p = argparse.ArgumentParser(description="Kapali dolap lambasi resmi sorusturma araci")
    p.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    p.add_argument("--tur", type=int, default=3)
    args = p.parse_args()
    if args.tur < 1:
        print("Tur 1'den kucuk olamaz. Komisyon en az bir kez cay ister.")
        raise SystemExit(2)
    gozlem(args.kapi, args.tur)


if __name__ == "__main__":
    main()
