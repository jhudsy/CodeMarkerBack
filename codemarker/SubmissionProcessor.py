from codemarker.models import Submission
from subprocess import Popen, PIPE, STDOUT
from django.core import serializers
import random
import time
import json


def processSubmission(submission_id):
    submission = Submission.objects.get(pk=submission_id)
    submission.status = "in_progress"
    submission.save()

    num1 = random.randint(0, 9999999999)
    num2 = random.randint(0, 9999999999)

    start_time = time.time()

    p = Popen(['python', './uploads/' + str(submission.filename)], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data = p.communicate(input=str.encode(str(num1) + "\n" + str(num2)))[0]

    if (float(stdout_data) == float(num1 + num2)):
        submission.result = "pass"
    else:
        submission.result = "fail"

    submission.status = "complete"
    submission.timeTaken = time.time() - start_time

    if submission.timeTaken < 0.01:
        submission.marks = 100
    elif submission.timeTaken < 0.02:
        submission.marks = 90
    elif submission.timeTaken < 0.025:
        submission.marks = 85
    elif submission.timeTaken < 0.03:
        submission.marks = 80
    elif submission.timeTaken < 0.04:
        submission.marks = 70
    elif submission.timeTaken < 0.05:
        submission.marks = 60
    else:
        submission.marks = 10

    submission.save()

    data = serializers.serialize('json', [submission, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])

    return data



