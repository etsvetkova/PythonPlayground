
import os
import tempfile
import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-key','--key',nargs='?')
parser.add_argument('-val','--val', nargs='+', default=False)

args = parser.parse_args(sys.argv[1:])

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'r') as f:
    print("fj")
    data = json.load(f)

    if not args.val :
        value = str(data.get(args.key,"None")).strip('[]')
        value = value.replace("'","")
        print(value)
    else:
        data[args.key] = args.val
        print(data)

        with open(storage_path, 'w') as f:
            f.write(json.dumps(data, ensure_ascii=False))





