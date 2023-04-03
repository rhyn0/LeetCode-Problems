# Standard Library
import doctest


class Codec:  # noqa: D101
    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings to a single string."""
        for index, string in enumerate(strs):
            strs[index] = f"{len(string):03d}{string}"

        return "".join(strs)

    def decode(self, encode_str: str) -> list[str]:
        """Decode a single string to a list of strings."""

        def _get_length(substr: str) -> int:
            return int(substr[:3])

        ret_list, decode_index = [], 0
        encode_str_len = len(encode_str)
        while decode_index < encode_str_len:
            curr_len = _get_length(encode_str[decode_index:])
            ret_list.append(encode_str[decode_index + 3 : decode_index + 3 + curr_len])
            decode_index += 3 + curr_len

        return ret_list


def main():
    """Encode and Decode Strings on LeetCode.

    This is a design question so do your best to come up with
    something that works in general cases.

    ====================================================

    Setup:
        >>> codec = Codec()

    Example 1:
        >>> msg = ["Hello","World"]
        >>> codec.decode(codec.encode(msg))
        ['Hello', 'World']

    Example 2:
        >>> msg = [""]
        >>> codec.decode(codec.encode(msg))
        ['']
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
