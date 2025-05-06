from mrjob.job import MRJob
from mrjob.step import MRStep

class TagCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_tags,
                   reducer=self.reducer_count_tags)
        ]

    def mapper_get_tags(self, _, line):
        try:
            # Diviser la ligne en colonnes
            userID, movieID, tag, timestamp = line.split(',')
            # Émettre le tag et la valeur 1
            yield tag, 1
        except Exception:
            pass

    def reducer_count_tags(self, tag, counts):
        # Somme des occurrences pour chaque tag
        yield tag, sum(counts)

if __name__ == '__main__':
    TagCount.run()
