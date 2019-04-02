import gzip, shutil

def decompress(n):
    with gzip.open(n, 'r') as f_in, open('farm_0.uc', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def compress(n):
    with open(n, 'rb') as f_in:
        with gzip.open('Events.json', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


decompress('farm_0.data')