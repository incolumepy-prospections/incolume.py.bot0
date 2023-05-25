"""Exemplo baseado em https://youtu.be/PAnrHMQBB-Y"""

__author__ = "@britodfbr"  # pragma: no cover

import schedule
import time
import threading
import logging


def fake_task() -> None:
    msg = 'Tarefa executando na thread {}'.format(threading.current_thread())
    logging.debug(msg)
    print(msg)


def run_thread(job):
    job_trhead = threading.Thread(target=job)
    job_trhead.start()


# schedule.frequencia.escala.oque
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)
schedule.every(5).seconds.do(run_thread, fake_task)


def run():
    stop = 50

    while stop > 0:
        schedule.run_pending()
        time.sleep(1)
        stop -= 1
