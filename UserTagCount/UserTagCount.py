from mrjob.job import MRJob
from mrjob.step import MRStep

class UserTagCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_tags,
                   reducer=self.reducer_count_tags)
        ]

    def mapper_get_tags(self, _, line):
        try:
            userID, movieID, tag, timestamp = line.split(',')
            yield userID, 1
        except Exception:
            pass

    def reducer_count_tags(self, userID, counts):
        yield userID, sum(counts)

if __name__ == '__main__':
    UserTagCount.run()
