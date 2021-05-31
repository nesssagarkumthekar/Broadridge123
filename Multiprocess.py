from concurrent.futures import ProcessPoolExecutor, as_completed
import main as main
import time

with ProcessPoolExecutor(max_workers=4) as executor:
    start = time.time()
    futures = [ executor.submit(main.process_file(Fullname,Pcode), url) for url in URLs ]
    results = []
    for result in as_completed(futures):
        results.append(result)
    end = time.time()
    print("Time Taken: {:.6f}s".format(end-start))
