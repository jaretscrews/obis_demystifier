#!/usr/local/bin/python3
import sys, argparse


def obis_dec_to_hex(obis):
    converted = ""
    for chunk in obis.split('.'):
        converted += hex(int(chunk))[2:]
    return converted


def obis_hex_to_dec(obis):
    converted = ""
    n = 2
    chunks = [obis[i:i + n] for i in range(0, len(obis), n)]
    for chunk in chunks:
        converted += str(int(chunk, 16)) + '.'

    return converted[:-1]


def convert_obis(obis):
    if '.' in obis:
        return obis_dec_to_hex(obis)
    else:
        return obis_hex_to_dec(obis)


def main(argv):
    parser = argparse.ArgumentParser("obis_demystifier")
    parser.add_argument("obis",
                        help="The obis that you want information on either in period separated decimal or hex",
                        type=str)
    args = parser.parse_args()
    converted = convert_obis(args.obis)
    print(converted)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv[1:])
