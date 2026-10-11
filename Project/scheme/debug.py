import sys
from pathlib import Path

# # 从本文件的位置定位 reader 压缩包，不依赖调试器的工作目录。
sys.path.insert(0, str(Path(__file__).resolve().parent / 'scheme_reader'))

from scheme import scheme_eval, create_global_frame, read_line
env = create_global_frame()
exp2 = read_line("(define x 10)")
scheme_eval(exp2,env)

res1 = scheme_eval(read_line("x"),env)
print(res1)
scheme_eval(read_line("(define y x)"),env)
scheme_eval(read_line("(define x 20)"),env)
y = scheme_eval(read_line("y"),env)
print(y)

