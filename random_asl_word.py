import random
import webbrowser
import json


def open_random_page(index_range: tuple , visited_filename: str):

    # Load list of visited indexes
    with open(visited_filename, 'r') as fp:
        obj = json.load(fp)
    visited = obj["visited"]

    # Open a random unvisited index
    index = random.randint(index_range[0], index_range[1])
    while index in visited:
        index = random.randint(index_range[0], index_range[1])
    webbrowser.open(f"https://www.handspeak.com/word/search/index.php?id={index}")

    # Save index as visited
    visited.append(index)
    with open(visited_filename, 'w') as fp:
        json.dump({"visited": visited}, fp)

def main():
    index_range = (0, 10341) # may change as website it updated
    # make sure file with contents {"visited":[]} exists
    filename = "random_asl_word_visited.json"
    open_random_page(index_range, filename)

if __name__ == "__main__":
    main()
