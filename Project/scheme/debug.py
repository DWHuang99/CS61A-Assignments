# import sys
# from pathlib import Path

# # 从本文件的位置定位 reader 压缩包，不依赖调试器的工作目录。
# sys.path.insert(0, str(Path(__file__).resolve().parent / 'scheme_reader'))

from scheme import scheme_eval, create_global_frame, read_line
env = create_global_frame()
# exp = read_line("(define x 5)")
# exp = read_line("(define ((x (+ 6 5))(y 2)(z 3)))")
# exp = read_line("(define ((x 5)(y 6)) )")
# exp2 = read_line("(let ((x (+ 6 5))(y 2)(z 3))(+ x 3))")
# exp2 = read_line("(let ((x 5)(y 6))(+ x 3))")
exp2 = read_line("(+ 6 5)")
# scheme_eval(exp,env)
scheme_eval(exp2,env)
print(exp2)