import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c","--content",help="打印",action="store_true")
args = parser.parse_args()
if args.content:
    print(args.content)
else:
    print("无参数")