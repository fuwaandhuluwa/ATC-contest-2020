

#   python -m cProfile -s cumtime -o profile.status unit_test.py
#  -m cProfile: 进行热点分析的选项
#  -o profile.status: 输出的分析日志文件名，二进制格式
#  -s cumtime: 指按照消耗时间进行排序

# C:\Users\jiafu.li\AppData\Local\Programs\Python\Python38\python.exe -m cProfile -s cumtime -o profile.status unit_test.py
#
# python -c "import pstats; p=pstats.Stats('profile.status'); p.print_stats()"