from mrjob.job import MRJob
from mrjob.step import MRStep

class MovieTagCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_tags,
                   reducer=self.reducer_count_tags)
        ]

    def mapper_get_tags(self, _, line):
        try:
            userID, movieID, tag, timestamp = line.split('\t')
            yield movieID, 1
        except Exception:
            # Ignorer les lignes mal formées
            pass

    def reducer_count_tags(self, movieID, counts):
        yield movieID, sum(counts)

if __name__ == '__main__':
    MovieTagCount.run()
