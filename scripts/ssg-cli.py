from tqdm import tqdm
from fire import Fire

from ssg import syllable_tokenize

def _count_lines(file):
    with open(file, "r") as f:
        count = 0
        for l in f:
            count +=1

    return count

def main(path, output, sep="~"):
    total_lines = _count_lines(path)

    with open(path, "r") as fin, open(output, "w") as fout:
        for line in tqdm(fin, total=total_lines):
            line = line.strip()

            fout.write("%s\n" % sep.join(syllable_tokenize(line)))

if __name__ == "__main__":
    Fire(main)