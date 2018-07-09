import os

WINDOWS_TRADITIONAL_CHINESE_ENCODING = "cp950"


def is_utf8_encoding_file(file_path):
    try:
        with open(file_path, encoding="utf-8") as f:
            f.readline()
            return True
    except UnicodeDecodeError:
        return False


def read_file_content(file_path, encoding="utf-8"):
    with open(file_path, encoding=encoding) as f:
        content = f.read()
    return content


def write_file_in_utf8(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="A simple CLI tool for converting files to UTF-8")
    parser.add_argument(
        "root",
        type=str,
        help="The root directory"
    )
    parser.add_argument(
        "--source_encoding",
        default=WINDOWS_TRADITIONAL_CHINESE_ENCODING,
        help="The default encoding of the source files"
    )
    args = parser.parse_args()

    target_file_encoding = WINDOWS_TRADITIONAL_CHINESE_ENCODING
    for root, dirs, files in os.walk(args.root):
        for name in files:
            target_file = os.path.join(root, name)
            if not is_utf8_encoding_file(target_file):
                print("Incorrect encoding file: {}".format(target_file))
                raw_file_content = read_file_content(target_file, args.source_encoding)
                # A workaround for URL encoding in comments.
                raw_file_content = raw_file_content.replace("&lt;", "<")
                write_file_in_utf8(target_file, raw_file_content)
    print("Done")
