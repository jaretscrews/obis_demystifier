#!/usr/local/bin/python3
import os
import sys, argparse


def obis_dec_to_hex(obis):
    converted = ""
    obis = obis.replace(':', '.')
    obis = obis.replace('-', '.')
    for chunk in obis.split('.'):
        temp = hex(int(chunk))[2:]
        if len(temp) == 1:
            temp = '0' + temp
        converted += temp
    return converted


def obis_hex_to_dec(obis):
    if len(obis) != 10:
        raise AttributeError("Hex obis should be 10 chars long!")
    converted = ""

    converted += str(int(obis[0:2], 16)) + '-'
    converted += str(int(obis[2:4], 16)) + ':'
    converted += str(int(obis[4:6], 16)) + '.'
    converted += str(int(obis[6:8], 16)) + '.'
    converted += str(int(obis[8:10], 16))

    return converted


def convert_obis(obis):
    if '.' in obis:
        return obis_dec_to_hex(obis)
    else:
        return obis_hex_to_dec(obis)


def main():
    parser = argparse.ArgumentParser("obis_demystifier")
    parser.add_argument("obis",
                        help="The obis that you want information on either in period separated decimal or hex",
                        type=str)
    args = parser.parse_args()
    try:
        converted = convert_obis(args.obis)
        print("Converted OBIS: " + converted)
    except AttributeError as err:
        print(err)
        exit(os.EX_USAGE)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
