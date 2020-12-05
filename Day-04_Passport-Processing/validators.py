import re


def _validate_byr(value):
    return 1920 <= int(value) <= 2002


def _validate_iyr(value):
    return 2010 <= int(value) <= 2020


def _validate_eyr(value):
    return 2020 <= int(value) <= 2030


def _validate_hgt(value):
    val = value[:-2]
    unit = value[-2:]
    if unit == 'cm':
        return 150 <= int(val) <= 193
    elif unit == 'in':
        return 59 <= int(val) <= 76
    return False


def _validate_hcl(value):
    return bool(re.compile('^[#]{1}[0-9a-f]{6}$').search(value))


def _validate_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def _validate_pid(value):
    return bool(re.compile('^[0-9]{9}$').search(value))


def _validate_cid(value):
    return True


def validate(key, value):
    return eval(f'_validate_{key}("{value}")')
