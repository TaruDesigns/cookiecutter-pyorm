import sys



def main():
    system_major = sys.version_info.major
    required_major = 3 # Python major version. Only Python 3 is supported
    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
