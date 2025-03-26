# -*- coding: utf-8 -*-
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
            # Diviser la ligne en colonnes
            userID, movieID, tag, timestamp = line.split(',')
            # Émettre la paire (userID, movieID) et la valeur 1
            yield (userID, movieID), 1
        except Exception:
            pass

    def reducer_count_user_movie_tags(self, user_movie, counts):
        # Somme des occurrences pour chaque paire (userID, movieID)
        yield user_movie, sum(counts)

if __name__ == '__main__':
    UserMovieTagCount.run()
