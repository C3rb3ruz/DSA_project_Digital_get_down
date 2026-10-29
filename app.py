from flask import Flask
import mergesort
import quicksort

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/mergesort")
def run_mergesort():
    arr = [5, 2, 8, 1, 9]
    sorted_arr = mergesort.merge_sort(arr)
    return str(sorted_arr)


@app.route("/quicksort")
def run_quicksort():
    arr = [5, 2, 8, 1, 9]
    quicksort.quick_sort(arr, 0, len(arr) - 1)
    return str(arr)


if __name__ == "__main__":
    app.run(debug=True)