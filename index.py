import csv

from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch(["es:9200"])
    index = "nolan"

    if es.indices.exists(index):
        es.indices.delete(index)

    es.indices.create(
        index,
        body={
            "mappings": {
                "properties": {"RELEASE_DATE": {"type": "date", "format": "yyyyMMdd"}}
            }
        },
    )

    with open("data/sample.csv", encoding="UTF-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            es.index(index=index, id=row["ID"], body=row)
    print("Finished indexing")


if __name__ == "__main__":
    main()
