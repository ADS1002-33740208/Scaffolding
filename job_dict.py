class JobDictionary:
    def __init__(self):
        self.jobs = {}

    def __getitem__(self, key):
        return self.jobs[key]

    def __setitem__(self, key, value):
        self.jobs[key] = value

    def __delitem__(self, key):
        del self.jobs[key]

    def __contains__(self, key):
        return key in self.jobs

    def __iter__(self):
        return iter(self.jobs)

    def delete_job(self, job_name):
        if job_name in self.jobs:
            del self.jobs[job_name]

    def __len__(self):
        return len(self.jobs)
