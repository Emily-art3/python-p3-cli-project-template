from lib.cli import parser
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    # Parse and handle CLI arguments
    parser.parse_args()
