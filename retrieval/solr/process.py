
import os

def processResults():
    foldername = os.getcwd()
    files = os.listdir(foldername)
    files = [x for x in files if x.endswith(".raw")]
    files.sort()

    results = {}
    for filename in files:
        # get the query number from the file name
        parts = filename[1:].split('_')
        query = int(parts[0])
        system = parts[1][:-4]
        if system not in results:
            results[system] = {}
        if query not in results[system]:
            results[system][query] = []
        with open(foldername + "/" + filename, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith('"id"'):
                    docid = line[8:-5]
                    results[system][query].append(docid)

    for system in results: 
        with open(foldername + "/" + system + ".out", "w") as out:
            queries = list(results[system].keys())
            queries.sort()
            for query in queries:
                docids = results[system][query]
                for i, docid in enumerate(docids):
                    print('{} Q0 {} {} 0 solr'.format(query, docid, i+1),
                          file=out)


if __name__ == '__main__':
    """
    Run this in the results folder!
    """
    processResults()
