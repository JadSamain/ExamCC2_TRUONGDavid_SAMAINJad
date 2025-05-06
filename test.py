from mrjob.job import MRJob
from mrjob.step import MRStep

class TagsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_tags,
                   reducer=self.reducer_count_tags)
        ]

    def mapper_get_tags(self, _, line):
        # Skip the header line
        if line.startswith("userId"):
            return

        # Print the line for debugging
        print(f"Processing line: {line}")

        # Split the line by commas
        parts = line.split(',')

        # Check if the line has the expected number of parts
        if len(parts) != 4:
            print(f"Unexpected format: {line}")
            return

        (userID, movieID, tag, timestamp) = parts
        yield tag, 1

    def reducer_count_tags(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsBreakdown.run()
