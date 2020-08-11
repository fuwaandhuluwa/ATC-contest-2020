

#   using cProfile library and snakeviz module visualization results

#  -------------------------------------------------------------
#  First step :
#       using cProfiler to run application
#  -------------------------------------------------------------

# import cProfile
#
# cProfile.run('run(readFileContent("C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/17.in"))',
#              filename='status.txt', sort='cumulative')


#  -------------------------------------------------------------
#  Second step:
#        using snakeviz tool to visualize the results and find
#        out which function takes up more resources
#  -------------------------------------------------------------

# below command must be used in shell
# snakeviz status.txt


# **************************************************************
#  Line_profiler:
#        using Line_profiler to analysis the results and find
#        out which statement takes up more resources
# **************************************************************
# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp_wrapper = lp(run)
# lp_wrapper(readFileContent("C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/1.in"))
# lp.print_stats()
# **************************************************************
# 优化思路：
#        1. adjacent 和判断是否为None占用15%的时间消耗，可以将其放在map初始化generateRoadMap()中一次性做完
#        2. 尽量使用减少函数调用
# **************************************************************
