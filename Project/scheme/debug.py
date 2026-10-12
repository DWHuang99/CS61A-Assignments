import sys
from pathlib import Path

# # 从本文件的位置定位 reader 压缩包，不依赖调试器的工作目录。
sys.path.insert(0, str(Path(__file__).resolve().parent / 'scheme_reader'))

from scheme import scheme_eval, create_global_frame, read_line
env = create_global_frame()

scheme_eval(read_line("(define three-curry (lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))) ))"),env)
res = scheme_eval(read_line("three-curry"),env)
exp = read_line("(lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))))")
print(res)