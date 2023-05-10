import sys

from compiler_project.compiler import Compiler

if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) == 1:
    print(
        """Usage: python main.py [options] [source file]
Options:
    -h,--help      show this help message
    -o,--output    output file name
    -t,--token     output token list
    --pretty       output pretty code
        """
    )
    exit(0)

compiler = Compiler()
if "-o" in sys.argv or "--output" in sys.argv:
    if "-o" in sys.argv:
        compiler.output_filename = sys.argv[sys.argv.index("-o") + 1]
        sys.argv.remove("-o")
    else:
        compiler.output_filename = sys.argv[sys.argv.index("--output") + 1]
        sys.argv.remove("--output")
    sys.argv.remove(compiler.output_filename)

if "-t" in sys.argv or "--token" in sys.argv:
    compiler.output_token = True
    try:
        sys.argv.remove("-t")
    except ValueError:
        sys.argv.remove("--token")

if "--pretty" in sys.argv:
    compiler.output_pretty = True
    sys.argv.remove("--pretty")

compiler.compile(sys.argv[-1])
