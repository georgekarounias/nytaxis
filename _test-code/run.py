from mrjob.job import Q1MR
mr_job = Q1MR(args="<data.json")
with mr_job.make_runner() as runner:
    runner.run()
