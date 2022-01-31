# ###################################################################################
#  Copyright ©2019-2020. Biorithm Pte Ltd. All Rights Reserved.
#  This software is the property of Biorithm Pte Ltd. It must not be copied, printed,
#  distributed, or reproduced in whole or in part or otherwise disclosed without
#  prior written consent from Biorithm.This document may follow best coding
#  practices for Python as suggested in https://www.python.org/dev/peps/pep-0008/.
#  Environment: Develop, Test
#  Filename:  lambda_handler.py
#  Original Author: TRAN MINH HAI
#  Date created: 18 JAN 2022
#  Purpose: to log things
#  Ref No      Date           Who            Detail
#  ------------------------------------------------------------------------------
# ###################################################################################
import json

def lambda_handler(event, context):
    # TODO implement
    sum = 0
    for m in range(100):
        for n in range(100):
            sum = sum + 1

    result = {
        "message": "Hello from Lambda!",
        "sum": "{0}".format(sum)
    }
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
