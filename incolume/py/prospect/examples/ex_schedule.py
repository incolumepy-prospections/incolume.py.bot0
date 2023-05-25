"""Exemplo baseado em https://youtu.be/PAnrHMQBB-Y"""

__author__ = "@britodfbr"  # pragma: no cover

import time

import schedule


def fake_task(msg: str = "") -> None:
    msg = msg or "Tarefa importante!"
    print(msg)


# schedule.frequencia.escala.oque
schedule.every(5).seconds.do(fake_task)
schedule.every(1).minutes.do(fake_task)
schedule.every(1).hours.do(fake_task)
schedule.every(1).days.do(fake_task)
schedule.every().monday.do(fake_task)
schedule.every().thursday.do(fake_task)
schedule.every().day.at("09:00").do(fake_task)


def run():
    stop = 50
    while stop >= 0:
        schedule.run_pending()
        time.sleep(1)
        stop -= 1
