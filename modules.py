import argparse
def clname():
    parser = argparse.ArgumentParser(description='Please enter the name.')
    parser.add_argument("--name", metavar='name', required=True,
                    help='The name of the person playing the game')
    return parser.parse_args()

if __name__ == "__main__":
    clname()