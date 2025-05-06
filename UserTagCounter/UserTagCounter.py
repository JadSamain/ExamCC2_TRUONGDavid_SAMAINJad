from mrjob.job import MRJob
from mrjob.step import MRStep

class UserMovieTagCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_user_movie_tags,
                   reducer=self.reducer_count_user_movie_tags)
        ]

    def mapper_get_user_movie_tags(self, _, line):
        try:
            userID, movieID, tag, timestamp = line.split(',')
            yield (userID, movieID), 1
        except Exception:
            pass

    def reducer_count_user_movie_tags(self, user_movie, counts):
        yield user_movie, sum(counts)

if __name__ == '__main__':
    UserMovieTagCount.run()
