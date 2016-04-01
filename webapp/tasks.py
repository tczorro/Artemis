from __future__ import absolute_import
from celery import shared_task
from saddle.TransitionSearch import TransitionSearch
import horton as ht

@shared_task
def test(param):
    return "this is the task test {}".format(param)

@shared_task
def saddle_find_ts(path_react, path_produ, ratio, auto_ic):
    reactant = ht.IOData.from_file(path_react)
    product = ht.IOData.from_file(path_produ)
    ts_guess = TransitionSearch(reactant, product)
    if auto_ic:
        ts_guess.auto_ic_select_combine()
    else:
        return (False,)
    ts_guess.auto_ts_search(ratio=ratio)
    ts_treat = ts_guess.create_ts_treat()
    return (True, ts_treat)
