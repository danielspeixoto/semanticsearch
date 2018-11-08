import evaluate
import semantics
from get import PickleRepository

repo = PickleRepository('.')
data = repo.all()

initial_map = 0
semantics_map = 0

for search in data:
    source = search['retrieved']
    query = search['query']
    correct = search['expected'][0]['id']
    initial_map += evaluate.map(correct, source)

    reordered = semantics.search(source, query)

    semantics_map += evaluate.map(correct, reordered)

initial_map /= len(data)
semantics_map /= len(data)

# Mean Average Precision
print("Map")
print("Initial: %.2f X Semantics: %.2f" % (initial_map, semantics_map))
