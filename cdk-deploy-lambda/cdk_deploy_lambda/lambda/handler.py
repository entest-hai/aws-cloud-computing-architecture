"""
Document string
"""


import json
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def single_thread_fft(sig):
    """
    single thread fft
    """


    start_time = datetime.now()
    for x in sig:
        np.fft.fft(x, axis=0)
    end_time = datetime.now()
    delta_time = end_time.timestamp() - start_time.timestamp()
    print("single thread running time {0} ms".format(delta_time * 1000))
    return delta_time


def multi_thread_fft(sig):
    """
    multi thread fft
    """


    start_time = datetime.now()
    with ThreadPoolExecutor(max_workers=4) as executor:
        for x in sig:
            executor.submit(np.fft.fft, x, axis=0)
    end_time = datetime.now()
    delta_time = end_time.timestamp() - start_time.timestamp()
    print("multi thread running time {0} ms".format(delta_time * 1000))
    return delta_time


def lambda_handler(event, context):
    """
    Lambda handler
    """


    # signal for one channel
    sig = [np.random.randint(0, 1000, (4098, 600)) for k in range(4)]
    # single thread
    single_thread_time = single_thread_fft(sig)
    # multi thread
    multi_thread_time = multi_thread_fft(sig)
    # response
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
         'body': json.dumps({'single thread': "{0}, multi thread: {1}".format(single_thread_time * 1000, multi_thread_time*1000)},
                            indent=4,
                            sort_keys=True,
                            default=str)
    }


if __name__=="__main__":
    lambdaReponse = lambda_handler(event=None, context=None)
    print(lambdaReponse)
